from github import Github

# or using an access token
g = Github("")
repo = g.get_repo("MohammedYassin1/ensf400lab2")

#Get all branches you have created for your public repo
branches = list(repo.get_branches())
for branch in branches:
    print(branch)

#Get all pull requests you have created
pulls = repo.get_pulls(state='all', sort='created', base='main')
for pull in pulls:
    print(f"PR #{pull.number}: {pull.title}")
    
#Get a list of commits you have created in your main branch.
commits = repo.get_commits(sha='main')
for commit in commits:
    print(commit)