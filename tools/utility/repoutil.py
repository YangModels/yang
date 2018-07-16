import tempfile
import shutil
import os

import sys
from git import Repo
from git.exc import GitCommandError

'''Notes:

repo.index.add(repo.untracked_files)

  Add all new files to the index

repo.index.add([i.a_path for i in repo.index.diff(None)])

  Add all modified files to the index. Also works for new directories.

repo.index.commit('commit for delete file')

  Commit any changes

repo.git.push()

  Push changes to origin.

repo.git.rm([f1, f2, ...])

  Remove files safely and add removal to index (note that files are
  left in lace, and then look like untracked files).

'''


class RepoUtil(object):
    """Simple class for rolling up some git operations as part of file
    manipulation. The user should create the object with the URL to
    the repository and an appropriate set of credentials. At this
    """

    def __init__(self, repourl):
        self.repourl = repourl
        self.localdir = None
        self.repo = None

    def get_repo_dir(self):
        """Return the repository directory name from the URL"""
        return os.path.basename(self.repourl)

    def get_repo_owner(self):
        """Return the root directory name of the repo.  In GitHub
        parlance, this would be the owner of the repository.
        """
        owner = os.path.basename(os.path.dirname(self.repourl))
        if ':' in owner:
            return owner[owner.index(':') + 1:]

        return owner

    def clone(self, config_user_name=None, config_user_email=None):
        """Clone the specified repository to a local temp directory. This
        method may generate a git.exec.GitCommandError if the
        repository does not exist
        """
        self.localdir = tempfile.mkdtemp()
        self.repo = Repo.clone_from(self.repourl, self.localdir)
        if config_user_name:
            config = self.repo.config_writer()
            config.set_value('user', 'email', config_user_email)
            config.set_value('user', 'name', config_user_name)

    def updateSubmodule(self, recursive=True, init=True):
        """Clone submodules of a git repository"""
        for submodule in self.repo.submodules:
            submodule.update(recursive, init)

    def add_all_untracked(self):
        """Commit all untracked and modified files. This method shouldn't
        generate any exceptions as we don't allow unexpected
        operations to be invoked.
        """
        self.repo.index.add(self.repo.untracked_files)
        modified = []
        deleted = []
        for i in self.repo.index.diff(None):
            if os.path.exists(self.localdir+'/'+i.a_path):
                modified.append(i.a_path)
            else:
                deleted.append(i.a_path)
        if len(modified) > 0:
            self.repo.index.add(modified)
        if len(deleted) > 0:
            self.repo.index.remove(deleted)

    def commit_all(self, message='RepoUtil Commit'):
        """Equivalent of git commit -a -m MESSAGE."""
        self.repo.git.commit(a=True, m=message)

    def push(self):
        """Push repo to origin. Credential errors may happen here."""
        self.repo.git.push("origin")

    def remove(self):
        """Remove the temporary storage."""
        shutil.rmtree(self.localdir)
        self.localdir = None
        self.repo = None


if __name__ == '__main__':

    #
    # local imports
    #
    from argparse import ArgumentParser

    #
    # test arguments
    #
    parser = ArgumentParser(description='RepoUtil test params:')
    parser.add_argument('userpass', nargs=1, type=str,
                        help='Provide username:password for github https access'
                        )
    args = parser.parse_args()
    if not args.userpass:
        print("username:password required")
        sys.exit(1)

    #
    # This repo exists
    #
    TEST_REPO = 'https://%s@github.com/einarnn/test.git'

    #
    # This repo does not exist
    #
    BOGUS_REPO = 'https://%s@github.com/einarnn/testtest.git'

    #
    # Create, clone and remove repo that exists.
    #
    print('\nTest 1\n------')
    try:
        r = RepoUtil(TEST_REPO % args.userpass[0])
        r.clone()
        print('Temp directory: '+r.localdir)
        r.remove()
    except GitCommandError as e:
        print('Git Exception: ' + e.status)

    #
    # Create, clone and modify a repo with good credentials. Will Then
    # try to modify, commit and push. If the file 'ok.txt' is present,
    # we will try to delete it. If it's not, we will create it!
    #
    print('\nTest 2\n------')
    try:
        r = RepoUtil(TEST_REPO % args.userpass[0])
        r.clone()
        print('Temp directory: '+r.localdir)
        ok_path = r.localdir + '/ok.txt'
        if os.path.exists(ok_path):
            print('Removing test file!')
            r.repo.git.rm(ok_path)
            # os.remove(ok_path)
        else:
            print('Creating test file!')
            with open(ok_path, 'w') as f:
                f.write('hello!\n')
                f.close()
        try:
            r.add_all_untracked()
            r.commit_all(message='push should succeed')
            r.push()
        except GitCommandError as e:
            print('Git Exception: ' + e.stderr)
        r.remove()
    except GitCommandError as e:
        print('Git Exception: ' + e.stderr)

    #
    # Create, clone and modify a repo with bogus credentials. Will Then try
    # to modify, commit and push, but still with bogus credentials.
    #
    print('\nTest 3\n------')
    try:
        r = RepoUtil(TEST_REPO % (args.userpass[0]+'bogus'))
        r.clone()
        print('Temp directory: '+r.localdir)
        with open(r.localdir+'/bogus.txt', 'w') as f:
            f.write('hello!\n')
            f.close()
        try:
            r.add_all_untracked()
            r.commit_all(message='push should fail')
            r.push()
        except GitCommandError as e:
            print('Git Exception as expected: ' + e.stderr)
        r.remove()
    except GitCommandError as e:
        print('Git Exception: ' + e.stderr)

    #
    # Try to create, clone and remove repo that does not exist. If
    # this is the caser, no dangling directory is left, so no need to
    # try and remove it.
    #
    print('\nTest 4\n------')
    try:
        r = RepoUtil(BOGUS_REPO % args.userpass[0])
        r.clone()
        print('Temp directory: ' + r.localdir)
        r.remove()
    except GitCommandError as e:
        print('Git Exception as expected: ' + e.stderr)
