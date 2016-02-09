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

import java.util.*;

import org.opendaylight.yangtools.yang.model.api.*;

/**
 * Defines constants used through the tree model where we define what to
 * display and in what order to display it.
 *
 * @author Devin Avery
 *
 */
public class Constants {
    public static final Map<Class<?>, String> CLASS_TO_NAME = Collections.unmodifiableMap( new HashMap<Class<?>, String>(){
        {
            put( Module.class, "Module" );
            put( ModuleImport.class, "Import" );
            put( ContainerSchemaNode.class, "Container" );
            put( LeafSchemaNode.class, "Leaf" );
            put( RpcDefinition.class, "RPC" );
            put( IdentitySchemaNode.class, "Identity" );
            put( TypeDefinition.class, "Type" );
            put( NotificationDefinition.class, "Notification" );
            put( SchemaNode.class, "Schema" );
        }
    });

    public static final List<Class<?>> CLASS_ORDER = Collections.unmodifiableList( new LinkedList<Class<?>>(){
        {
            add( Module.class );
            add( ModuleImport.class );
            add( ContainerSchemaNode.class );
            add( LeafSchemaNode.class );
            add( RpcDefinition.class );
            add( IdentitySchemaNode.class );
            add( TypeDefinition.class );
            add( NotificationDefinition.class );
            add( SchemaNode.class );
        }
    });

    public static String getMostSpecificClassName( Object o )
    {
        return CLASS_TO_NAME.get( getMostSpecificImplementingClass( o ) );
    }
    public static Class<?> getMostSpecificImplementingClass( Object o )
    {
        if( o == null )
        {
            return null;
        }

        Class<?> objClass = o.getClass();
        for( Class<?> c : CLASS_ORDER )
        {
            if( c.isAssignableFrom( objClass ) )
            {
                return c;
            }
        }
        return null;
    }
}
