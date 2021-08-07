import tempfile
from git import Repo

def analyze_repo(name, git_url):

    ## TODO: pull to common dir, see if it already exists and fetch updates.
    with tempfile.TemporaryDirectory() as repo_checkout:

        repo = Repo.clone_from(git_url, repo_checkout)

        print(f'## {name}\n')
        print_remotes(repo)
        print()

def print_remotes(repo):
        
    for ref in repo.remotes[0].refs:

        if 'HEAD' in ref.name:
            continue
        
        hash = ref.dereference_recursive(ref.repo, ref.path)

        print(f'    {ref.name:40} {hash}')


