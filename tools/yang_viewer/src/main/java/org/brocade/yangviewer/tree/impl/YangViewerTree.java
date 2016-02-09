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

import java.awt.event.*;
import java.io.File;
import java.util.*;

import javax.swing.*;
import javax.swing.tree.*;

import org.brocade.yangviewer.tree.interfaces.*;
import org.brocade.yangviewer.util.ProgressDialog;
import org.brocade.yangviewer.util.StatusProgressListener;
import org.opendaylight.yangtools.yang.model.api.Module;
import org.opendaylight.yangtools.yang.model.parser.api.YangContextParser;
import org.opendaylight.yangtools.yang.parser.impl.YangParserImpl;

/**
 * Defines the actual JTree gui component where one can add yangs etc.
 * This essentially wires the model to the GUI object along with D&D etc.
 * @author Devin Avery
 *
 */
public class YangViewerTree extends JTree implements FileDropTransferListener {

    private final ObjectValueCompiler compiler = new YangObjectValueTreeNodeCompiler(); // new YangModuleToTreeModuleCompilerImpl();

    private final Collection<File> files = new HashSet<>();

    private final FilterByType filter = new FilterByType( null );

    private final StatusListener status;
    public YangViewerTree( StatusListener statusListener )
    {
        this.status = statusListener;

        FilterableTreeModel buildYangModels =
                            compiler.compile( "Drop .yang files here to compile.", null );
        filter.setModelToRefreshOnUpdate( buildYangModels );
        buildYangModels.setFilter( filter );
        this.setModel( buildYangModels);
        this.setDropMode( DropMode.ON_OR_INSERT );
        this.setTransferHandler(  new YangViewModelTransferHandler( this ) );
        this.setCellRenderer( new YangModulesTreeCellRenderer() );

        this.addMouseListener( new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if( e.isPopupTrigger() )
                {
                    TreePath selPath = YangViewerTree.this.getPathForLocation(e.getX(), e.getY());
                    YangViewerTree.this.setSelectionPath( selPath );
                    showRightClickMenu( selPath, e.getX(), e.getY() );
                }
            }
        });

    }

    private void showRightClickMenu( TreePath path, int x, int y )
    {
        if( path != null )
        {
            final Object lastPathComponent = ((DefaultMutableTreeNode)path.getLastPathComponent()).getUserObject();

            JPopupMenu popUp = new JPopupMenu();

            if( lastPathComponent instanceof File || lastPathComponent instanceof Module )
            {
                JMenuItem remove = new JMenuItem( "Remove This Module" );
                remove.addActionListener( new ActionListener() {

                    @Override
                    public void actionPerformed(ActionEvent e) {
                        File file = null;
                        if( lastPathComponent instanceof File )
                        {
                            file = (File)lastPathComponent;
                        }
                        else
                        {
                            Module module = (Module)lastPathComponent;
                            file = new File( module.getModuleSourcePath() );
                        }
                        onRemove( Collections.singleton( file ) );
                    }
                });
                popUp.add( remove );
            }

            JMenuItem removeAll = new JMenuItem( "Remove All Modules" );
            removeAll.addActionListener( new ActionListener() {

                @Override
                public void actionPerformed(ActionEvent e) {
                    synchronized( files )
                    {
                        onRemove( files );
                    }
                }
            });
            popUp.add( removeAll );

            popUp.addSeparator();

            Set<Class<?>> filteredClazzes = filter.getClassesToFilter();

            for( Class<?> c : Constants.CLASS_ORDER )
            {
                boolean isFiltered = filteredClazzes.contains( c );
                final Class<?> fc = c;
                JCheckBoxMenuItem menu =
                        new JCheckBoxMenuItem( (isFiltered?"Show ":"Hide ") +
                                                                Constants.CLASS_TO_NAME.get( c ) );
                menu.setSelected( isFiltered );
                menu.addActionListener( new ActionListener() {

                    @Override
                    public void actionPerformed(ActionEvent e) {
                         filter.toggleFilter( fc );
                    }
                });
                popUp.add( menu );
            }

            popUp.show( YangViewerTree.this, x, y );
        }
    }

    private Collection<Module> compile( Collection<File> files )
    {
        YangContextParser parser = new YangParserImpl();
        Collection<Module> modules = parser.parseYangModelsMapped( files ).values();
        return modules;
    }

    @Override
    public void onAdd(Collection<File> files) {
        synchronized( this.files )
        {
            this.files.addAll( files );
        }
        compileAndSetModelOnSeperateThread();
    }

    private void compileAndSetModelOnSeperateThread() {
        final StatusProgressListener status =
                ProgressDialog.createDialogAndShow( this, "Compile Yang", "Compiling. Please wait..." );
        Runnable r = new Runnable()
        {
            @Override
            public void run() {
                Collection<File> files;
                synchronized( YangViewerTree.this.files )
                {
                    files = new TreeSet<File>( YangViewerTree.this.files ) ;
                }
                try
                {
                    Collection<Module> modules = compile( files );

                    FilterableTreeModel treeModel = compiler.compile( "Yang Definitions",  modules );
                    treeModel.setFilter( filter );
                    filter.setModelToRefreshOnUpdate( treeModel );
                    setModel( treeModel );
                    YangViewerTree.this.status.setStatus( "Compiled successfully.", false );

                }
                catch( Exception e )
                {
                    DefaultMutableTreeNode root = new DefaultMutableTreeNode( "Yang Files" );
                    for( File f : files )
                    {
                        root.add( new DefaultMutableTreeNode( f ) );
                    }
                    setModel( new DefaultTreeModel( root ) );
                    onException( e );
                }
                finally {
                    status.setDone();
                }
            }
        };
        new Thread( r, "Compile Yang Files" ).start();
    }

    @Override
    public void onException(Exception e){
        status.setStatus( e.getMessage(), true );
        e.printStackTrace();
    };

    @Override
    public void onRemove(java.util.Collection<File> files) {
        synchronized( this.files )
        {
            this.files.removeAll( files );
        }
        compileAndSetModelOnSeperateThread();
    };
}
