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

import java.awt.*;

import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeCellRenderer;

import org.opendaylight.yangtools.yang.model.api.*;

/**
 * The render for the JTree rows.
 * @author Devin Avery
 *
 */
public class YangModulesTreeCellRenderer extends DefaultTreeCellRenderer {

//    Would like to have unique icons in the future...
//    private static final Icon MODULE_ICON = new ImageIcon( "src/main/resources/icons/module.png" );
//    private static final Icon IMPORTS_ICON = new ImageIcon( "src/main/resources/icons/imports.png" );
//    private static final Icon ATTRIBUTE_ICON = new ImageIcon( "src/main/resources/icons/attribute.png" );
//    private static final Icon ATTRIBUTE_AUG_ICON = new ImageIcon( "src/main/resources/icons/attribute_augment.png" );
//    private static final Icon CONTAINER_ICON = new ImageIcon( "src/main/resources/icons/container.png" );
//    private static final Icon CONTAINER_AUG_ICON = new ImageIcon( "src/main/resources/icons/container_augment.png" );

    private final JPanel panel = new JPanel();
   // private final DefaultTreeCellRenderer label = new DefaultTreeCellRenderer();

    public YangModulesTreeCellRenderer()
    {
//        panel.setLayout( new TableLayout( new double[][]{
//                { TableLayout.PREFERRED, TableLayout.FILL },
//                {TableLayout.FILL }
//        }));
//        panel.add( this, "0,0" );
//        panel.add( label, "1,0" );
//        label.setLeafIcon( null );
//        label.setOpenIcon( null );
//        panel.setBorder( BorderFactory.createLineBorder( Color.BLUE ));
//        label.setClosedIcon( null );

    }



    @Override
    public void setMaximumSize(Dimension maximumSize) {
        // TODO Auto-generated method stub
        super.setMaximumSize(maximumSize);
        panel.setMaximumSize(maximumSize);
    }

    @Override
    public void setPreferredSize(Dimension preferredSize) {
        super.setPreferredSize(preferredSize);
        panel.setPreferredSize(preferredSize);
    }


    @Override
    public Component getTreeCellRendererComponent(JTree tree, Object value, boolean selected,
            boolean expanded, boolean leaf, int row, boolean hasFocus) {
        DefaultMutableTreeNode node = (DefaultMutableTreeNode) value;
        Object o = node.getUserObject();

        boolean isAugment = false;

        String label = "";
        String title = Constants.getMostSpecificClassName( o );
        if( title == null )
        {
            title = "";
        }
        else
        {
            title += ":";
        }
        if( o instanceof Module )
        {
            Module mod = (Module)o;
            label = mod.getName();
        }
        else if( o instanceof ModuleImport )
        {
            ModuleImport modImport = (ModuleImport)o;
            label = modImport.getModuleName();
        }
        else if( o instanceof SchemaNode )
        {
            SchemaNode sn = (SchemaNode)o;
            label = sn.getQName().getLocalName();

            if( o instanceof DataSchemaNode )
            {
                DataSchemaNode dsn = (DataSchemaNode)o;
                isAugment = dsn.isAugmenting();
            }
        }
        else
        {
            if( !( o instanceof String ) )
            {
                title = o.getClass().getSimpleName() + ":";
            }
            label = String.valueOf( o );
            setOpenIcon( getDefaultOpenIcon() );
            setClosedIcon( getDefaultClosedIcon() );
            setLeafIcon( getDefaultLeafIcon() );
        }
        JLabel c = (JLabel)super.getTreeCellRendererComponent( tree, title + label, selected, expanded, leaf, row, hasFocus);
        if( isAugment )
        {
            c.setForeground( Color.GRAY );
        }
        else
        {
            c.setForeground( Color.BLACK );
        }
        return c;
    }

    private void setIcons(Icon moduleIcon) {
        setOpenIcon( moduleIcon );
        setClosedIcon( moduleIcon );
        setLeafIcon( moduleIcon );
    }

}
