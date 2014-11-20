YANG
=====

This repository contains a collection of YANG modules:

  * IETF standards-track YANG modules
  * Open Daylight open source YANG modules
  * Vendor specific YANG modules
  * Open source YANG tools

***

Directory Structure
-------------------

The following directories are maintained [license note in brackets]:

  **yang/experimental**: contains experimental YANG modules [any]

  **yang/experimental/ietf**: experimental modules intended for IETF submission [1]

  **yang/experimental/odp**: experimental modules intended for OpenDaylight submission [2]

  **yang/standard**: contains standards-track YANG modules [any]

  **yang/standard/ietf**: standard IETF YANG modules [1]

  **yang/standard/ietf/DRAFT**: work-in-progress IETF YANG modules [1]

  **yang/standard/ietf/RFC**: completed IETF YANG modules [1]

  **yang/standard/odp**: published modues for OpenDaylight [2]

  **yang/tools**: open source software tools [any]

  **yang/tools/yang_viewer**: YANG browser written in Java [2]

  **yang/vendor**: contains vendor-specific YANG modules [any]

  **yang/vendor/brocade** : Brocade YANG modules [3] 

  **yang/vendor/netconfcentral**: Netconf Central YANG modules [3]

  **yang/vendor/yumaworks**: YumaWorks YANG modules [3]

***

License Information
-------------------

####[1]  **IETF Trust License  (Note Well)**:

   * All files contained within this sub-directory are considered to be IETF Contributions.
   * All issues entered into the trouble ticket system for this directory are considered to be IETF Contributions.
   * All pull requests submitted for this directory are considered to be IETF Contributions.
   * All IETF Contributions are submitted under the terms of the [IETF Note Well statement](http://www.ietf.org/about/note-well.html)
   * All IETF Contributions are subject to the requirements and provisions of [BCP 78](http://tools.ietf.org/rfc/bcp/bcp78.txt) and [BCP 79](http://tools.ietf.org/rfc/bcp/bcp79.txt).

####[2]  **OpenDaylight Eclipse License**:

   * All files contained within this sub-directory are provided under the terms of the [Eclipse Public License](https://www.eclipse.org/legal/epl-v10.html):


####[3]  **Vendor Specific License**:

  * All files contained within this sub-directory are provided under the terms of a license specified by the vendor that owns the YANG modules.

***

Submission Procedure
--------------------

1.	Head over to [Gerrithub](http://review.gerrithub.io)

2.	Sign on with your GitHub user and authorize the application.

3.	Click on the drop down by your user name and select Settings.

4.	Click on Watched Projects and click Browse.

5.	Filter and select YangModels/yang.

6.	Select the notifications you want to receive.

7.	Upload your SSH public key.

8.	git clone ssh://<username>@review.gerrithub.io:29418/YangModels/yang

9.	Change/add any file.

10.	Run git add <changed/added file>

11.	Run git commit and add a test comment

12.	Run git-review(git-review is a separate package in Unix that needs to be installed and configured)

13.	In the gerrithub.io website, add a reviewer or wait for one of us to review it automatically every day and merge it .

14.    If there are any issues, send email to tnadeau at brocade.com and kkoushik at brocade.com.    If there are any issues, send email to tnadeau at brocade.com and kkoushik at brocade.com.    If there are any issues, send email to tnadeau at brocade.com and kkoushik at brocade.com

