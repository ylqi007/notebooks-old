
# [Introduction to Git - Core Concepts](https://www.youtube.com/watch?v=uR6G2v_WsRA&ab_channel=DavidMahler)
Commands used in this video:
* git init - initialize a new repo in a directory
* git config --global user.name "name"
* git config --global user.email "email"
* git config --list
* (--local option as well) for a specific repo
* git status - see the state of files in working tree, staging area vs latest commit in git history
* git add - move file(s) to the staging area
* git log - view the git history / git commit graph
* git diff - diff of working tree and staging area
* git diff --cached - diff of staging area and latest commit
* git rm - remove a file from the working tree and the staging area
* git checkout -- filename - retrieve a file from the staging area into the working tree
* git reset HEAD filename - retrieve a file from the latest commit into the staging area
* git checkout (commit hash) filename - retrieve a file from a previous commit

# [Introduction to Git - Branching and Merging](https://www.youtube.com/watch?v=FyAAIHHClqI&ab_channel=DavidMahler)
Commands Used:
* git log =  git history
* git log --all --decorate --oneline --graph = commit history graph
* git branch (branch-name) = create a branch
* git checkout (branch-name) = checkout a branch/move head pointer
* git commit -a -m "commit message" = commit all modified and tracked files in on command (bypass separate 'git add' command)
* git diff master..SDN = diff between 2 branches
* git merge (branch-name) = merge branches (fast-forward and 3-way merges)
* git branch --merged = see branches merged into the current branch
* git branch -d (branch-name) = delete a branch, only if already merged
* git branch -D (branch-name) = delete a branch, including if not already merged (exercise caution here)
* git merge --abort = abort a merge during a merge conflict situation
* git checkout (commit-hash) = checkout a commit directly, not through a branch, results in a detached HEAD state
* git stash = create a stash point
* git stash list = list stash points
* git stash list -p = list stash points and show diffs per stash
* git stash apply = apply most recent stash
* git stash pop = apply most recent stash, and remove it from saved stashes
* git stash apply (stash reference) = apply a specific stash point
* git stash save "(description)" = create a stash point, be more descriptive


# [Introduction to Git - Remotes](https://www.youtube.com/watch?v=Gg4bLk8cGNo&ab_channel=DavidMahler)

Commands used:
* Retrieve/Clone a repo = git clone (URL)
* List remotes = git remote (-v for detail)
* Commit graph = git log --all --decorate --oneline --graph
* Checkout a branch = git checkout
* Create and checkout a branch = git checkout -b (branch name)
* Retrieve/download from a remote = git fetch (remote name)
* merge branch or tracking-branch = git merge (branch or tracking branch name)
* Show status = git status
* Upload to a remote = git push (remote name) (branch name)
* stage an edit = git add (filename)
* make a commit = git commit -m "description"
* stage and commit = git commit -a -m "description"
* List local branches = git branch
* List remote branches = git branch -r


[Pro Git by Scott Chacon](https://git-scm.com/book/en/v2)
[Visual Git Reference by Mark Lodato](https://marklodato.github.io/visual-git-guide/index-en.html)