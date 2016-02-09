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
package org.brocade.yangviewer.util;

import java.awt.*;
import java.math.RoundingMode;
import java.text.DecimalFormat;

import javax.swing.*;

import org.brocade.yangviewer.GUIConstants;

import info.clearthought.layout.TableLayout;

/**
 * A generic ProgressDialog GUI component. This allows external entities to update
 * its status, change message etc all while displaying a growing or interderminate
 * status.
 *
 * @author Devin Avery
 *
 */
public class ProgressDialog extends JDialog implements StatusProgressListener {

    private JLabel messageLbl;
    private JProgressBar progressBar;
    private volatile String message = "";
    private volatile int progress = ProgressListener.INDETERMINATE;
    private volatile int max = ProgressListener.INDETERMINATE;
    private boolean isDone = false;
    private final Object visibleLock = new Object();

    public ProgressDialog ( Frame parent, String title, String message )
    {
        super( parent, title, true );
        init( message , parent );
    }

    public ProgressDialog(Dialog parent, String title, String initMessage) {
        super( parent, title, true );
        init( message, parent );
    }

    private void init(String message, Component parent ) {
        this.message = message;
        JPanel messagePanel = new JPanel( new TableLayout( new double[][]{
                { GUIConstants.BORDER, TableLayout.FILL, GUIConstants.BORDER },
                { GUIConstants.BORDER,
                  TableLayout.FILL, GUIConstants.PAD,
                  TableLayout.FILL,
                  GUIConstants.BORDER}
        }));

        messageLbl = new JLabel( message );
        progressBar = new JProgressBar();
        progressBar.setIndeterminate( true );
        messagePanel.add( messageLbl, "1,1" );
        messagePanel.add( progressBar, "1,3" );

        Container contentPane = getContentPane();

        contentPane.setLayout(new BorderLayout());
        contentPane.add(messagePanel, BorderLayout.CENTER);
        setResizable(false);
        pack();

        Dimension packedSize = getSize();
        Dimension newSize = new Dimension( Math.min( Math.max( packedSize.width, 300 ), 500 ),
                                           Math.min( Math.max( packedSize.height, 100 ), 300 ) );
        setSize( newSize );
        setLocationRelativeTo(parent);
        setModalityType( ModalityType.APPLICATION_MODAL );
    }

    @Override
    public void setProgress(int value) {
        if( value == ProgressListener.INDETERMINATE )
        {
            this.progress = value;
            setMaxProgress( value );
        }
        else
        {
            progressBar.setValue( value );
            updateMessageText();
        }
    }

    @Override
    public void setMaxProgress(int value) {
        max = value;
        if( value == INDETERMINATE )
        {
            progressBar.setIndeterminate( true );
        }
        else
        {
            progressBar.setIndeterminate( false );
            progressBar.setMaximum( value );
        }
        updateMessageText();
    }

    @Override
    public void setDone() {
        setProgress( max );
        setVisible( false );
    }

    @Override
    public void setVisible(boolean b) {

        boolean setVisible = false;
        synchronized( visibleLock )
        {
            if( isDone == false )
            {
                setVisible = true;
            }

            if( b == false )
            {
                isDone = true;
            }
        }

        if( setVisible )
        {
            super.setVisible( b );
        }
    }

    @Override
    public void updateMessage(String message) {
        this.message = message;
        updateMessageText();
    }

    private void updateMessageText() {
        SwingUtilities.invokeLater( new Runnable(){
            @Override
            public void run() {
                String progressStr = "";
                if( progress != ProgressListener.INDETERMINATE &&
                    max != ProgressListener.INDETERMINATE && max > 0 )
                {
                    DecimalFormat format = new DecimalFormat( "#.##% ");
                    format.setRoundingMode( RoundingMode.HALF_UP );
                    progressStr = format.format( (double)progress / (double)max );
                }
                messageLbl.setText( progressStr + ProgressDialog.this.message );
            }
        });
    }

    public static StatusProgressListener createDialogAndShow( Component parent, String title, String initMessage )
    {
        final ProgressDialog dialog;

        Window window = SwingUtilities.windowForComponent(parent);
        if (window instanceof Frame) {
            dialog = new ProgressDialog((Frame)window, title, initMessage);
        } else {
            dialog = new ProgressDialog((Dialog)window, title, initMessage);
        }

        SwingUtilities.invokeLater( new Runnable(){
          @Override
            public void run() {
              dialog.setVisible( true );
            }
        });

        return dialog;
    }
}
