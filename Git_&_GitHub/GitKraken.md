## Branching in Git

```bash
git branch

# To rename a Git Branch locally using the terminal
git branch -m <the desired new branch name>
# Rename a branch that has already been pushed to a remote
git push -u (or --set-upstream)	//?

# To delete a local Git branch
git branch -d <local branch name>
# To delete a remote Git branch
git push <name-of-remote-repository> --delete <branch-name>

# To switch to another branch
git checkout
```

* [how to create a branch in Git](https://www.gitkraken.com/learn/git/problems/create-git-branch)
* [how to delete a Git branch locally](https://www.gitkraken.com/learn/git/problems/delete-local-git-branch)
* [how to delete a remote branch in Git](https://www.gitkraken.com/learn/git/problems/delete-remote-git-branch)
* [switch to another branch in Git](https://www.gitkraken.com/learn/git/problems/switch-git-branch)



## Git Checkout

If you want to make changes to a branch that you don't already have checked out, you will first need to checkout the branch.

```bash
# How to checkout a branch
git checkout <name-of-branch>

# How to checkout a commit
git checkout <commit hash>

# How to checkout a tag
git checkout <tag name>

# How to checkout the tag as a branch
git checkout -b <branch name> <tag name>
```

* ##### [What is Git Checkout?			](https://www.gitkraken.com/learn/git/tutorials/what-is-git-checkout)

* ***how to [Git checkout a remote branch](https://www.gitkraken.com/learn/git/problems/git-checkout-remote-branch)*** 

* ***how to [switch between local branches](https://www.gitkraken.com/learn/git/problems/switch-git-branch).***

* ***[How do you Git checkout a commit?			](https://www.gitkraken.com/learn/git/problems/git-checkout-commit)***

* ##### [How do you checkout a Git tag?			](https://www.gitkraken.com/learn/git/problems/git-checkout-tag)

* ##### [How do you checkout a remote branch in Git?			](https://www.gitkraken.com/learn/git/problems/git-checkout-remote-branch)



## [Git Cherry Pick](https://www.gitkraken.com/learn/git/cherry-pick)

A Git commit is a snapshot of your repository at one point in time, with each commit cumulatively forming your repo history.

In Git, the cherry pick command takes changes from a target commit and places them on the HEAD of the currently checked out branch. From here, you can either continue working with these changes in your working directory or you can immediately commit the changes onto the new branch.

```bash
# To begin the process of cherry picking in the CLI, you will first need to obtain the SHA for the commit you wish to cherry pick.
git log --all --decorate --oneline --graph

# After copying the SHA from your log, you can then run
git cherry-pick <followed by the SHA to cherry-pick the target commit>

# If the command performed a cherry pick correctly, a new commit should be visible with a unique SHA. You can also verify that everything looks good by running `git log` again to view log graph
git log --all --decorate --oneline --graph

# Clean up history after cherry picking. Go back and checkout the original branch and do a hard reset on the parent commit.
```



* To [cherry pick in GitKraken](https://support.gitkraken.com/working-with-commits/cherrypick/),

* ##### [Can you cherry pick multiple commits in Git?			](https://www.gitkraken.com/learn/git/problems/cherry-pick-multiple-commits)

* ##### [Can you cherry pick from another repository in Git?			](https://www.gitkraken.com/learn/git/problems/cherry-pick-from-another-repository)

* ##### [Learn Git: How to Cherry Pick a Commit			](https://www.gitkraken.com/learn/git/tutorials/how-to-cherry-pick-git)

* ##### [Clean Up History After Cherry Picking			](https://www.gitkraken.com/learn/git/best-practices/clean-up-history-after-cherry-picking)

