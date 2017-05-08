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
package org.brocade.yangviewer;

import java.awt.Color;

import javax.swing.*;
import javax.swing.event.TreeSelectionEvent;
import javax.swing.event.TreeSelectionListener;
import javax.swing.table.TableCellRenderer;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.TreePath;

import org.brocade.yangviewer.table.impl.ClassLevelTableModel;
import org.brocade.yangviewer.table.impl.ObjectValueCellRenderer;
import org.brocade.yangviewer.tree.impl.YangViewerTree;
import org.brocade.yangviewer.tree.interfaces.StatusListener;

import info.clearthought.layout.TableLayout;

/**
 * Main method -- sets up the gui and relates the GUI objects and underlying
 * models etc together.
 *
 * @author Devin Avery
 *
 */
public class Main {

    public static void main(String[] args) {

        try
        {
            JFrame frame = new JFrame( "Yang Viewer" );
            frame.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );

            frame.setLayout( new TableLayout( new double[][]{
                    {
                        TableLayout.FILL
                    },
                    {
                        TableLayout.FILL
                    }

            }));


            ClassLevelTableModel tableModel = new ClassLevelTableModel( null, false );

            final JTable table = createDetailTable( tableModel );

            JPanel treePanel = new JPanel( new TableLayout( new double[][]{
                    {
                        TableLayout.FILL
                    },
                    {
                        TableLayout.FILL, GUIConstants.PAD, 40
                    }
            }));

            JLabel statusLabel = new JLabel( " ");

            YangViewerTree tree = createJTree(tableModel, statusLabel, treePanel );

            treePanel.add( createScrollPane( tree ), "0,0" );
            treePanel.add( new JScrollPane( statusLabel ), "0,2" );

            JPanel rootPanel = new JPanel();
            rootPanel.setLayout( new TableLayout( new double[][]{
                    { TableLayout.FILL },
                    { TableLayout.FILL }
            }));


            JSplitPane splitPane = new JSplitPane( JSplitPane.HORIZONTAL_SPLIT,
                                       treePanel,
                                       createScrollPane( table ) );

            rootPanel.add( splitPane, "0,0" );
            frame.add( rootPanel, "0,0" );
            splitPane.setDividerLocation( 200 );

            frame.setSize( 800, 600);
            frame.setLocationRelativeTo( null );

            frame.setVisible( true );
        }
        catch( Exception e )
        {
            e.printStackTrace();
        }
    }

    private static YangViewerTree createJTree(final ClassLevelTableModel classLevelTableModel, final JLabel statusLabel, final JPanel treePanel) {
        YangViewerTree tree = new YangViewerTree( new StatusListener() {

            @Override
            public void setStatus(String status, boolean isError ) {
                statusLabel.setText( status );
                statusLabel.setToolTipText( status );
                if( isError )
                {
                    treePanel.setBorder( BorderFactory.createLineBorder( Color.RED ) );
                }
                else
                {
                    treePanel.setBorder( BorderFactory.createEmptyBorder() );
                }
            }
        });

    	//you can add files OOB like...
        //        tree.onAdd( Collections.singleton(
        //                new File( "path..to..some..yang.." ) ));
        tree.addTreeSelectionListener( new TreeSelectionListener() {

            @Override
            public void valueChanged(TreeSelectionEvent e) {
                TreePath path = e.getPath();
                if( path != null )
                {
                    DefaultMutableTreeNode node =
                            (DefaultMutableTreeNode)path.getLastPathComponent();
                    Object userObj = node.getUserObject();
                    classLevelTableModel.setObjectToShow( userObj );
                }
            }
        });
        return tree;
    }

    private static JTable createDetailTable( ClassLevelTableModel tableModel ) {
        final ObjectValueCellRenderer renderer = new ObjectValueCellRenderer();

        final JTable table = new JTable( tableModel )
        {
            @Override
            public TableCellRenderer getDefaultRenderer(Class<?> columnClass) {
                return renderer;
            }
        };
        table.setPreferredScrollableViewportSize( table.getPreferredSize());
        table.setFillsViewportHeight( true );
        return table;
    }

    private static JScrollPane createScrollPane(JComponent tree) {
        JScrollPane jScrollPane = new JScrollPane( tree,
                        JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,
                        JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);
        return jScrollPane;
    }

}
