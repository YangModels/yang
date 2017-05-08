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

import java.io.File;
import java.util.Collection;
import java.util.Set;

import javax.swing.tree.*;

import org.apache.commons.collections.CollectionUtils;
import org.brocade.yangviewer.tree.interfaces.YangModuleToTreeModuleCompiler;
import org.opendaylight.yangtools.yang.model.api.*;
import org.opendaylight.yangtools.yang.model.parser.api.YangContextParser;
import org.opendaylight.yangtools.yang.parser.impl.YangParserImpl;

/**
 * Responsible for compiling a collection of files into a TreeModel which can be displayed in a
 * JTree.
 *
 * Uses the OpenDaylight yang parser as the basis for compiling a model.
 *
 * @author Devin Avery
 *
 */
public class YangModuleToTreeModuleCompilerImpl implements YangModuleToTreeModuleCompiler{

    @Override
    public TreeModel buildYangModels(Collection<File> files) {
        YangContextParser parser = new YangParserImpl();
        Collection<Module> modules = parser.parseYangModelsMapped( files ).values();
        return setUpModules( modules );
    }

    private TreeModel setUpModules( Collection<Module> modules )
    {
        DefaultMutableTreeNode rootNode = new DefaultMutableTreeNode( "Yang Modules" );

        YangModuleToTreeModuleCompilerImpl helper = new YangModuleToTreeModuleCompilerImpl();
        for( Module module : modules )
        {
            rootNode.add( helper.toTreeNode(module) );
        }

        return new DefaultTreeModel( rootNode );

    }

    private DefaultMutableTreeNode toTreeNode(Module module) {
        DefaultMutableTreeNode moduleNode = new DefaultMutableTreeNode(module);

        processImports(module.getImports(), moduleNode);

        processDataSchemaNode( module.getChildNodes(), moduleNode);

        processRPC( module.getRpcs(), moduleNode );

        return moduleNode;
    }

    private void processRPC(Set<RpcDefinition> rpcs, DefaultMutableTreeNode moduleNode) {
        if( CollectionUtils.isEmpty( rpcs ) )
        {
            return;
        }
        for( RpcDefinition rpc : rpcs )
        {
            DefaultMutableTreeNode rpcNode = createNode( moduleNode, rpc );
            ContainerSchemaNode input = rpc.getInput();
            if( input != null )
            {
                DefaultMutableTreeNode inputNode = createNode( rpcNode, input );
                processDataSchemaNode(  input.getChildNodes(), inputNode );
            }
            ContainerSchemaNode output = rpc.getOutput();
            if( output != null )
            {
                DefaultMutableTreeNode outputNode = createNode( rpcNode, output );
                processDataSchemaNode( output.getChildNodes(), outputNode );
            }
        }
    }

    private void processImports(Set<ModuleImport> imports, DefaultMutableTreeNode parent) {
        if (CollectionUtils.isEmpty(imports)) {
            return;
        }
        for (ModuleImport mImport : imports) {
            createNode(parent, mImport);
        }
    }

    private void processDataSchemaNode(Collection<DataSchemaNode> childNodes,
            DefaultMutableTreeNode parent) {

        if( childNodes != null )
        {
            for (DataSchemaNode node : childNodes) {
                DefaultMutableTreeNode tnode = createNode(parent, node);

                if (node instanceof ContainerSchemaNode) {
                    ContainerSchemaNode schemaNode = (ContainerSchemaNode) node;
                    processDataSchemaNode(schemaNode.getChildNodes(), tnode);
                }
            }
        }
    }

    private DefaultMutableTreeNode createNode(DefaultMutableTreeNode parent, Object child) {
        DefaultMutableTreeNode modNode = new DefaultMutableTreeNode(child);
        parent.add(modNode);
        return modNode;
    }

}
