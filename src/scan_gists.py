
from github import Github
from util import analyze_repo
import os
from datetime import datetime

g = Github(os.environ.get('GITHUB_PAT'))

user = g.get_user()

print(f'Report on {datetime.utcnow().isoformat()}\n')

print(f"Enumerating gists for github/{user.login}", end='\n\n')

for gist in g.get_user().get_gists():
    
    is_public = '' if gist.public else ' (Secret)'
    analyze_repo(f'{gist.html_url}{is_public}', gist.git_pull_url)