[![Build Status](https://travis-ci.org/YangModels/yang.svg)](https://travis-ci.org/YangModels/yang)

YANG
=====

This repository contains a collection of YANG modules:

  * IETF standards-track YANG modules
  * Open Daylight open source YANG modules
  * IEEE experimental YANG modules
  * Vendor specific YANG modules
  * Open source YANG tools

***
## Slack Group and Channels
 [To Subscribe and Browse Click Here](https://yangmodels.slack.com)

## Models Directory Structure

The following directories are maintained for YANG models [license note in brackets]:

  **yang/experimental**: contains experimental YANG modules [any]

  **yang/experimental/ieee**: experimental modules intended for IEEE submission [3]

  **yang/experimental/ietf**: experimental modules intended for IETF submission [1]

  **yang/experimental/odp**: experimental modules intended for OpenDaylight submission [2]

  **yang/standard**: contains standards-track YANG modules [any]

  **yang/standard/ietf**: standard IETF YANG modules [1]

  **yang/standard/ietf/DRAFT**: work-in-progress IETF YANG modules [1]

  **yang/standard/ietf/RFC**: completed IETF YANG modules [1]

  **yang/standard/odp**: published modues for OpenDaylight [2]


  **yang/vendor**: contains vendor-specific YANG modules [any]

  **yang/vendor/brocade**: Brocade YANG modules [4]
  
  **yang/vendor/cisco**: Cisco YANG modules [4] 

  **yang/vendor/netconfcentral**: Netconf Central YANG modules [4]

  **yang/vendor/yumaworks**: YumaWorks YANG modules [4]

## Tools Directory Structure

The following directories are maintained for tools [license note in brackets]:

  **yang/tools**: open source software tools [any]

  **yang/tools/xym**: YANG model extractor tool, submodule (```git clone --resursive``` to include) [5]

  **yang/tools/yang_viewer**: YANG browser written in Java [2]


## License Information

### [1] IETF Trust License  (Note Well):

   * All files contained within this sub-directory are considered to be IETF Contributions.
   * All issues entered into the trouble ticket system for this directory are considered to be IETF Contributions.
   * All pull requests submitted for this directory are considered to be IETF Contributions.
   * All IETF Contributions are submitted under the terms of the [IETF Note Well statement](http://www.ietf.org/about/note-well.html)
   * All IETF Contributions are subject to the requirements and provisions of [BCP 78](http://tools.ietf.org/rfc/bcp/bcp78.txt) and [BCP 79](http://tools.ietf.org/rfc/bcp/bcp79.txt).

### [2] OpenDaylight Eclipse License:

   * All files contained within this sub-directory are provided under the terms of the [Eclipse Public License](https://www.eclipse.org/legal/epl-v10.html):

### [3] IEEE License:

   * All files contained within this sub-directory are considered to be intended as IEEE Contributions.
   * All issues entered into the trouble ticket system for this directory are considered to be intended as IEEE Contributions.
   * All pull requests submitted for this directory are considered to be intended as IEEE Contributions.
   * All contributions to IEEE standards development (whether for an individual or entity standard) shall meet the requirements outlined in the [IEEE-SA Copyright Policy](https://standards.ieee.org/develop/policies/bylaws/sect6-7.html#7)
   * Copyright release for YANG modules: Users may freely reproduce the YANG modules contained under /experimental/ieee/ so that they can be used for their intended purpose.

### [4]  Vendor Specific License:

  * All files contained within this sub-directory are provided under the terms of a license specified by the vendor that owns the YANG modules.

### [5] Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


## Submission Procedure

Send us a git pull request with latest changes. When doing a pull request, please post the pyang output to show that your changes build cleanly.

If there are any issues, send email to tnadeau at brocade.com and kkoushik at brocade.com
