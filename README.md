[![Build Status](https://travis-ci.org/YangModels/yang.svg)](https://travis-ci.org/YangModels/yang)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [YANG](#yang)
- [Contribution Procedures](#contribution-procedures)
  - [Direct Contributions](#direct-contributions)
  - [Contributions Via Submodules](#contributions-via-submodules)
  - [Travis CI Jobs](#travis-ci-jobs)
- [Slack Group and Channels](#slack-group-and-channels)
- [Models Directory Structure](#models-directory-structure)
- [Tools Directory Structure](#tools-directory-structure)
- [License Notes](#license-notes)
- [Code of Conduct](#Code-of-Conduct)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

YANG
=====

This repository contains a collection of YANG modules:

  * IETF standards-track YANG modules
  * OpenDaylight open source YANG modules
  * IEEE experimental YANG modules
  * Broadband Forum standard YANG modules
  * Vendor-specific YANG modules
  * Open source YANG tools

# Contribution Procedures

## Direct Contributions

This is the preferred method of contribution. With this approach you pick where your models will reside in the directory hierarchy, and manage the files mainly in your own fork of the main repository, submitting a pull request when you wish to make public updated models.  All push requests must be reviewed by at least one of the repository's Committers, so when pushing a PR, please assign it to one of the committers.

You can find a tutorial here for how to do push requests. Note that there are at least two different approaches to how to do Pull Requests: using a shell/commandline or using the web interface, so if you do not find what you need below, look elsewhere or ask the committers for pointers.

https://yangsu.github.io/pull-request-tutorial/

By convention, there should also be a `check.sh` script provided by the contributors, which should be referenced from the [`travis.yml`](https://github.com/YangModels/yang/blob/master/.travis.yml) file for CI builds. Multiple examples are already in place to copy and modify as required.


## Contributions Via Submodules

Standards bodies or vendors may also provide models to the main repository via a git submodule. Examples of this can be see under [https://github.com/YangModels/yang/tree/master/standard](https://github.com/YangModels/yang/tree/master/standard), with the BBF and MEF submodules. By convention, if a submodule is used, there should also be an equivalent `check.sh` provided by the contributors, which should be referenced from the [`travis.yml`](https://github.com/YangModels/yang/blob/master/.travis.yml) file for CI builds. An example of this may be found [in the BBF's submodule](https://github.com/BroadbandForum/yang), and a sample invocation [here](https://github.com/YangModels/yang/blob/b8ad913fb4cc20ca21b59da1bd8df5cc2927a8e1/.travis.yml#L17).

Direct contributions to the top level of the repository are not encouraged; instead each "organization" should create a top-level folder as described above.


## A summary of the suggested process is:

1. Create a fork of [https://github.com/YangModels/yang](https://github.com/YangModels/yang)
1. Enable Travis on your fork
1. Add your source git repository as a submodule to your fork:
    - Clone your fork
    - cd into vendor or standards directory (depending on the source of your models)
    - `git submodule add https://github.com/<owner>/<repository>.git <name>`
1. Add appropriate entry to the `.travis.yml` file to check your models.
1. Note: this requires a call to a `check.sh` script provided by the contributors, which should be referenced from the [`travis.yml`](https://github.com/YangModels/yang/blob/master/.travis.yml) file for CI builds. Multiple examples are already in place to copy and modify as required, but in general, one is present at the top-most level of each major submodule area.
1. Commit changes to your fork
1. Test the Travis CI run of your fork as well as test it by running the testall.sh script from the top level directory.
 
After you've verified that the submodule addition and module checking is working ok, submit a PR to the main repository. This will take the latest commit from your repository and make it available as a submodule.

Subsequently, when an updated set of models needs to be released, fork, clone, update submodule, commit and submit PR, also ensuring that Travis is again enabled on your fork to allow pre-pull request checks.

All Pull Requests must be reviewed and as such one of the repository's Committers must review the request prior to actually committing the request.  Changes may be suggested during this process, so patience is requested during this process.


## Travis CI Jobs

In general, pull requests will not be accepted without `check.sh` scripts being in place and a clean Travis CI build being achieved. As can be seen from existing check scipts, all of which use `pyang` today, the bar is set fairly low. The minimum requirement is that the models contributed compile correctly such that `pyang` plugins such as the tree plugin will function correctly, and the schema tree is available for interrogation and tasks such as code generation.

As noted above, the check scripts today depend on `pyang`, and, as of writing, this tool does not support validation of content such as regular expressions or XPath constraints. **As such, models available in this repository may not be accepted by tools that perform more complete semantic validation.** An example of such a tool is the OpenDaylight controller.

# Slack Group and Channels

[To Subscribe and Browse Click Here](https://yangmodels.slack.com)

# Models Directory Structure

The following directories are maintained for YANG models [license note in brackets]:

- **yang/experimental**: contains experimental YANG modules [any]
- **yang/experimental/ietf**: experimental modules intended for IETF submission [1]
- **yang/experimental/odp**: experimental modules intended for OpenDaylight submission [2]
- **yang/standard**: contains standards-track YANG modules [any]
- **yang/standard/ieee**: standard modules (published or drafts) intended for IEEE submission [3]
- **yang/standard/ietf**: standard IETF YANG modules [1]
- **yang/standard/ietf/DRAFT**: work-in-progress IETF YANG modules [1]
- **yang/standard/ietf/RFC**: completed IETF YANG modules [1]
- **yang/standard/odp**: published modules for OpenDaylight [2]
- **yang/standard/bbf/draft**: draft Broadband Forum YANG modules [6]
- **yang/standard/bbf/standard**: standard Broadband Forum YANG modules [6]
- **yang/vendor**: contains vendor-specific YANG modules [any]
- **yang/vendor/cisco**: Cisco YANG modules [4] 
- **yang/vendor/netconfcentral**: Netconf Central YANG modules [4]
- **yang/vendor/yumaworks**: YumaWorks YANG modules [4]

# Tools Directory Structure

The following directories are maintained for tools [license note in brackets]:

- **yang/tools**: open source software tools [any]
- **yang/tools/xym**: YANG model extractor tool, submodule (```git clone --resursive``` to include) [5]
- **yang/tools/yang_viewer**: YANG browser written in Java [2]


# License Notes

**[1] IETF Trust License  (Note Well):**

   * All files contained within this sub-directory are considered to be IETF Contributions.
   * All issues entered into the trouble ticket system for this directory are considered to be IETF Contributions.
   * All pull requests submitted for this directory are considered to be IETF Contributions.
   * All IETF Contributions are submitted under the terms of the [IETF Note Well statement](http://www.ietf.org/about/note-well.html)
   * All IETF Contributions are subject to the requirements and provisions of [BCP 78](http://tools.ietf.org/rfc/bcp/bcp78.txt) and [BCP 79](http://tools.ietf.org/rfc/bcp/bcp79.txt).

**[2] OpenDaylight Eclipse License:**

   * All files contained within this sub-directory are provided under the terms of the [Eclipse Public License](https://www.eclipse.org/legal/epl-v10.html):

**[3] IEEE License:**

   * All files contained within this sub-directory are considered to be intended as IEEE Contributions.
   * All issues entered into the trouble ticket system for this directory are considered to be intended as IEEE Contributions.
   * All pull requests submitted for this directory are considered to be intended as IEEE Contributions.
   * All contributions to IEEE standards development (whether for an individual or entity standard) shall meet the requirements outlined in the [IEEE-SA Copyright Policy](https://standards.ieee.org/develop/policies/bylaws/sect6-7.html#7)
   * Copyright release for YANG modules: Users may freely reproduce the YANG modules contained under /standard/ieee/ so that they can be used for their intended purpose.

**[4]  Vendor Specific License:**

  * All files contained within this sub-directory are provided under the terms of a license specified by the vendor that owns the YANG modules.

**[5]** Warrantees and Conditions

  * Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

**[6] Broadband Forum License:**

  * All files contained within this sub-directory are provided under the terms of the Broadband Forum Software license (see Appendix C, Section 3, of https://www.broadband-forum.org/ipr-policy).
  
  
# Code of Conduct

The Yang Models Repository follows [The CNCF Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md).


