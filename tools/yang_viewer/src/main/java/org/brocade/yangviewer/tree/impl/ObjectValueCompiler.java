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
package org.brocade.yangviewer.tree.impl;

import java.lang.reflect.Method;
import java.util.*;

import javax.swing.tree.DefaultMutableTreeNode;

import org.apache.commons.lang3.ArrayUtils;
import org.brocade.yangviewer.tree.interfaces.FilterableTreeModel;

/**
 * Provides functionality which builds up tree models from a given object / children.
 * Children are determined based on the objects getter/setter methods and can
 * be further customized by derived implementations.
 * @author Devin Avery
 *
 */
public class ObjectValueCompiler{

    public FilterableTreeModel compile( Object root, Collection<?> children)
    {
        DefaultMutableTreeNode rootNode = new DefaultMutableTreeNode( root );
        if( children != null )
        {
            for( Object child : children )
            {
                createNode( rootNode, child, new HashSet<>() );
            }
        }
        return new FilterableTreeModelImpl( rootNode );
    }

    private boolean createNode( DefaultMutableTreeNode parent,
                                Object comp, Set<Object> alreadyProcessed ) {
        if( comp instanceof Collection )
        {
          //infinite loop checking
            if( !alreadyProcessed.add( comp ) )
            {
                if( comp instanceof Collection )
                {
                    return true;
                }
            }
            for( Object o : (Collection)comp )
            {
                createNode( parent, o, alreadyProcessed );
            }
            return true;
        }
        else if( shouldInclude( comp, parent.getUserObject() ) )
        {
            //infinite loop checking
            if( !alreadyProcessed.add( comp ) )
            {
                return true;
            }
            DefaultMutableTreeNode root = new DefaultMutableTreeNode( comp );
            parent.add( root );
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
                        try
                        {
                            Object result = m.invoke( comp );
                            createNode( root, result, alreadyProcessed );
                        }catch( Exception e )
                        {
                            e.printStackTrace();
                        }
                    }
                }
            }
            return true;
        }
//        if( comp != null )
//        {
//            System.out.println( "Skipping " + comp.getClass().getSimpleName() );
//        }
        return true;
    }

    protected boolean shouldInclude(Object comp, Object userObject) {
        return comp != null;
    }


}
