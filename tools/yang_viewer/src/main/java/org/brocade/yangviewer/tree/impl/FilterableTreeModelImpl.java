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

import javax.swing.tree.*;

import org.brocade.yangviewer.tree.interfaces.FilterableTreeModel;

/**
 * Defines a tree model for the GUI tree component which is filterable.
 * @author Devin Avery
 *
 */
public class FilterableTreeModelImpl extends DefaultTreeModel implements FilterableTreeModel{

    private final DefaultMutableTreeNode trueRoot;
    private volatile Filter filter;

    public FilterableTreeModelImpl(DefaultMutableTreeNode root) {
        super( filter( null, root ) );
        this.filter = filter;
        trueRoot = root;
    }

    public FilterableTreeModelImpl(DefaultMutableTreeNode root, Filter filter ) {
        super( filter( filter, root ) );
        this.filter = filter;
        trueRoot = root;
    }

    @Override
    public void filterUpdated()
    {
        setRoot( filter( filter, trueRoot ) );
        reload();
    }

    @Override
    public void setFilter(Filter filter) {
        this.filter = filter;
        filterUpdated();
    }

    private static TreeNode filter(Filter filter, DefaultMutableTreeNode root) {

        if( filter == null )
        {
            return root;
        }
        DefaultMutableTreeNode node = new DefaultMutableTreeNode( root.getUserObject() );

        for( int i = 0; i < root.getChildCount(); i++ )
        {
            DefaultMutableTreeNode childTree = buildNodeIfNotFiltered( filter, (DefaultMutableTreeNode)root.getChildAt( i ) );
            if( childTree != null )
            {
                node.add( childTree );
            }
        }

        return node;
    }

    private static DefaultMutableTreeNode buildNodeIfNotFiltered(Filter filter,
            DefaultMutableTreeNode thisRealNode) {

        DefaultMutableTreeNode thisFilteredNode = null;
        if( filter.shouldInclude( thisRealNode.getPath() ) )
        {
            thisFilteredNode = new DefaultMutableTreeNode( thisRealNode.getUserObject() );
        }
        if( thisFilteredNode != null )
        {
            for( int i = 0; i < thisRealNode.getChildCount(); i++ )
            {
                DefaultMutableTreeNode childNode = buildNodeIfNotFiltered( filter,
                                               (DefaultMutableTreeNode)thisRealNode.getChildAt( i ) );
                if( childNode != null )
                {
                    if( thisFilteredNode == null )
                    {
                        thisFilteredNode = new DefaultMutableTreeNode( thisRealNode.getUserObject() );
                    }
                    thisFilteredNode.add( childNode );
                }
            }
        }
        return thisFilteredNode;
    }



}
