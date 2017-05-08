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

import java.awt.datatransfer.*;
import java.io.File;
import java.io.IOException;
import java.util.List;

import javax.swing.TransferHandler;

import org.brocade.yangviewer.tree.interfaces.FileDropTransferListener;

/**
 * Defines the Drag & Drop (D&D) model for the JTree
 * @author Devin Avery
 *
 */
public class YangViewModelTransferHandler extends TransferHandler {

    private final FileDropTransferListener dropListener;

    public YangViewModelTransferHandler( FileDropTransferListener dropListener )
    {
        this.dropListener = dropListener;
    }

    @Override
    public boolean canImport(TransferSupport support) {
        if( !support.isDataFlavorSupported( DataFlavor.javaFileListFlavor ) ||
            !support.isDrop())
        {
            return false;
        }
        return true;
    }

    @Override
    public boolean importData(TransferSupport support) {
        if( !canImport( support ) )
        {
            return false;
        }

        Transferable transferable = support.getTransferable();

        try {
            List<File> files =
                    (List<File>) transferable.getTransferData( DataFlavor.javaFileListFlavor );
            dropListener.onAdd(  files );
            return true;
        } catch (ClassCastException | UnsupportedFlavorException | IOException e) {
            dropListener.onException( e );
            return false;
        }
    }
}
