1). [src refspec master does not match any error when pushing to repository](https://confluence.atlassian.com/bitbucketserverkb/src-refspec-master-does-not-match-any-error-when-pushing-to-repository-788727186.html)

2). [How do I ensure Git doesn't ask me for my GitHub username and password?](https://superuser.com/questions/199507/how-do-i-ensure-git-doesnt-ask-me-for-my-github-username-and-password) <br>
因为使用了不同的协议。 <br>

![Git_Config_Remote_Origin](./images/Git_Config_Remote_Origin.png)
如 `git config remote.origin.url <...>` 前后的 `remote.origin.url` 所示。


3). [Untrack files already added to git repository based on .gitignore](http://www.codeblocq.com/2016/01/Untrack-files-already-added-to-git-repository-based-on-gitignore/)

如果不小心 track 了一些文件或目录，想要将其从**暂存区**移除，但是依然在本地保留，则可以考虑下面命令：
```bash
git rm -r --cached .
```
* `rm` is the remove command
* `-r` will allow recursive removal
* `--cached` will only remove files from index, but the files will still be there
* `.` indicates that all files will be untracked. You want to untrack a specific file with `git rm --cached <file>`.

4). [Untrack files]()
Use the following command to unstage files:
```bash 
git reset HEAD <file>...
```

5). [There is no tracking information for the current branch](https://stackoverflow.com/questions/32056324/there-is-no-tracking-information-for-the-current-branch)
[git branch --set-upstream 本地关联远程分支](https://blog.csdn.net/z1137730824/article/details/78254564)

6). Errors of `git pull fatal`: 
* `refusing to merge unrelated histories` and `fatal: Couldn't find remote ref master`

* [The “fatal: refusing to merge unrelated histories” Git error](https://www.educative.io/edpresso/the-fatal-refusing-to-merge-unrelated-histories-git-error)

7). error: Your local changes to the following files would be overwritten by merge:
* [How do I ignore an error on 'git pull' about my local changes would be overwritten by merge?](https://stackoverflow.com/questions/14318234/how-do-i-ignore-an-error-on-git-pull-about-my-local-changes-would-be-overwritt)
* [How do I resolve git saying “Commit your changes or stash them before you can merge”?](https://stackoverflow.com/questions/15745045/how-do-i-resolve-git-saying-commit-your-changes-or-stash-them-before-you-can-me)
    1. Option 1: **Commit the change using:** `git commit -m "commit info"`
    2. Option 2: **Stash it:** Stashing acts as a stack, where you can push changes, and you pop them in reverse order.
        * `git stash` --> merge --> `git stash pop`.
        * You can use `git stash -u` to stash uncommitted files too.
    3. Option 3: **Discard the local changes:**
        * Using `git reset --hard` or `git checkout -t -f remote/branch`
        * Discard local changes for a specific file: `git checkout filename`