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

import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.TreeNode;

import org.brocade.yangviewer.tree.interfaces.FilterableTreeModel;
import org.brocade.yangviewer.tree.interfaces.FilterableTreeModel.Filter;

/**
 * A filter which uses class type to decide what to show/hide.
 * @author Devin Avery
 *
 */
public class FilterByType implements Filter {

    private final Set<Class<?>> clazzesToFilter = new HashSet<Class<?>>();

    private volatile FilterableTreeModel modelToRefreshOnUpdate;

    public FilterByType( FilterableTreeModel model )
    {
        this.modelToRefreshOnUpdate = model;
    }

    public void setModelToRefreshOnUpdate( FilterableTreeModel model )
    {
        this.modelToRefreshOnUpdate = model;
    }

    public void addFilterObjectsLike( Class<?> clazz )
    {
        synchronized( clazzesToFilter )
        {
            clazzesToFilter.add( clazz );
        }
        updateModel();
    }

    public void toggleFilter( Class<?> clazz ){
        synchronized( clazzesToFilter )
        {
            if( !clazzesToFilter.add( clazz ) )
            {
                clazzesToFilter.remove( clazz );
            }
        }
        updateModel();
    }

    private void updateModel() {
        FilterableTreeModel model = modelToRefreshOnUpdate;
        if( model != null )
        {
            model.filterUpdated();
        }
    }

    public void removeFilterObjectsLike( Collection<Class<?>> clazz )
    {
        synchronized( clazzesToFilter )
        {
            clazzesToFilter.removeAll( clazz );
        }
        updateModel();
    }

    public Set<Class<?>> getClassesToFilter()
    {
        synchronized( clazzesToFilter )
        {
            return new HashSet<Class<?>>( clazzesToFilter );
        }
    }

    @Override
    public boolean shouldInclude(TreeNode[] path) {
        synchronized( clazzesToFilter )
        {
            if( path.length > 0 )
            {
                DefaultMutableTreeNode treeNode = (DefaultMutableTreeNode)path[path.length-1];
                Object userObject = treeNode.getUserObject();
                Class<?> userClass = userObject.getClass();
                for( Class<?> toFilter : clazzesToFilter )
                {
                    if( toFilter.isAssignableFrom( userClass ) )
                    {
                        return false;
                    }
                }
            }
        }
        return true;
    }

}
