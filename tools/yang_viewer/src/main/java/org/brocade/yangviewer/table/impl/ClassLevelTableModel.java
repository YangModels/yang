/**
* Copyright (c) 2016, Brocade Communications Systems, Inc.
* All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions are met:
*
* * Redistributions of source code must retain the above copyright notice, this
*   list of conditions and the following disclaimer.
*
* * Redistributions in binary form must reproduce the above copyright notice,
*   this list of conditions and the following disclaimer in the documentation
*   and/or other materials provided with the distribution.
*
* * Neither the name of Brocade nor the names of its
*   contributors may be used to endorse or promote products derived from
*   this software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
* AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
* DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
* FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
* DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
* SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
* CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
* OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
* OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*
*/
package org.brocade.yangviewer.table.impl;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.*;

import javax.swing.table.AbstractTableModel;

import org.apache.commons.lang3.ArrayUtils;
import org.apache.commons.lang3.StringUtils;
import org.apache.commons.lang3.tuple.Pair;

/**
 * Defines a table model for the GUI Table component which dynamically extracts
 * values from the getters of a class.
 *
 * @author Devin Avery
 *
 */
public class ClassLevelTableModel extends AbstractTableModel {

    private Object obj;

    private final static String [] TITLES= { "Name", "Value" };

    private final List<Pair<String, Method>> methods;

    private final Object lock = new Object();

    private final boolean showListAttributes;
    public ClassLevelTableModel( Object objToShow, boolean showListAttributes )
    {
        this.obj = objToShow;
        this.showListAttributes = showListAttributes;
        methods = compileMethods( objToShow, showListAttributes);
    }

    public void setObjectToShow( Object objToShow )
    {
        List<Pair<String,Method>> methods = compileMethods( objToShow, showListAttributes);
        synchronized( lock )
        {
            this.obj = objToShow;
            this.methods.clear();
            this.methods.addAll( methods );
        }
        fireTableDataChanged();
    }

    private List<Pair<String,Method>> compileMethods(Object comp, boolean showListAttributes) {
        if( comp == null )
        {
            return new ArrayList<Pair<String,Method>>();
        }
        List<Pair<String,Method>> getters = new LinkedList<>();
        Class<?> clazz = comp.getClass();
        for( Class<?> supInterface : clazz.getInterfaces() )
        {
            for( Method m : supInterface.getMethods() )
            {

                if( ArrayUtils.isEmpty( m.getParameterTypes() ) &&
                    ( m.getName().startsWith( "get" ) || m.getName().startsWith( "is" ) ) &&
                    m.getReturnType() != null &&
                    !m.getReturnType().equals( Void.class )
                    )
                {
                    String name;
                    if( m.getName().startsWith( "get" ) )
                    {
                        name = getName( "get", m.getName() );
                    }
                    else
                    {
                        name = getName( "is", m.getName() );
                    }

                    if( showListAttributes ||
                        !(Collection.class.isAssignableFrom( m.getReturnType() ) ) )
                    {
                        getters.add( Pair.of( name, m) );
                    }
                }
            }
        }
        return getters;
    }

    private String getName(String string, String name) {

        return StringUtils.join(
                StringUtils.splitByCharacterTypeCamelCase( name.substring( string.length() ) ),
                " " );
    }

    @Override
    public String getColumnName(int column) {
        return TITLES[column];
    }

    @Override
    public int getRowCount() {

        synchronized( lock )
        {
            return methods.size();
        }
    }

    @Override
    public int getColumnCount() {
        return TITLES.length;
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        synchronized( lock )
        {
            Pair<String,Method> method = methods.get( rowIndex );
            if( columnIndex == 0 )
            {
                return method.getLeft();
            }
            else
            {
                try {
                    Method right = method.getRight();
                    return right.invoke( obj );
                } catch (IllegalAccessException | IllegalArgumentException |
                         InvocationTargetException e) {
                    e.printStackTrace();
                    return e;
                }
            }
        }
    }

}
