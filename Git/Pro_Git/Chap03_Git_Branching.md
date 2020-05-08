# 3. Git 分支
几乎所有的版本控制系统都以某种形式支持分支。 使用分支意味着你可以把你的工作从开发主线上分离开来，以免影响开发主线。
Git 处理分支的方式可谓是难以置信的轻量，创建新分支这一操作几乎能在瞬间完成，并且在不同分支之间的切换操作也是一样便捷。 与许多其它版本控制系统不同，Git 鼓励在工作流程中频繁地使用分支与合并，哪怕一天之内进行许多次。 理解和精通这一特性，你便会意识到 Git 是如此的强大而又独特，并且从此真正改变你的开发方式。

## 3.1 分支简介
 Git 保存的不是文件的变化或者差异，而是一系列不同时刻的**快照**。

 在进行提交操作时，Git 会保存一个**提交对象（commit object）**。该提交对象会包含一个指向暂存内容快照的指针。 但不仅仅是这样，该**提交对象**还包含了作者的姓名和邮箱、提交时输入的信息以及指向它的父对象的指针。首次提交产生的提交对象没有父对象，普通提交操作产生的提交对象有一个父对象， 而由多个分支合并产生的提交对象有多个父对象。

 ![commits-and-parents](./../images/commits-and-parents.png)
 Git 的分支，其实本质上仅仅是指向提交对象的可变指针。Git 的默认分支名字是 `master`。 在多次提交操作之后，你其实已经有一个指向最后那个提交对象的 `master` 分支。 `master` 分支会在每次提交时自动向前移动。


 ### 3.1.1. 分支创建
 Git 如何创建分支？ ==> 使用`git branch`创建一个可以移动的指针。
 ```bash
 $ git branch testing
 $ git branch -b testing  # 创建+切换
 ```
 Git 如何知道当前在哪一个分支上呢？它有一个名为`HEAD`的特殊指针。`git branch`命令仅仅**创建**一个分支，并不会自动切换到新的分支中。
 ![commits-and-parents](./../images/head-to-master.png)

 你可以简单地使用 `git log` 命令查看各个分支当前所指的对象。 提供这一功能的参数是 ``--decorate`。
 ```bash
$ git log --oneline --decorate
 ```


### 3.1.2. 分支切换
要使用`git checkout`命令。
```bash
$ git checkout <branch-name>
```

**Note:** 分支切换会改变你工作目录中的文件。
在切换分支时，一定要注意你工作目录里的文件会被改变。如果是切换到一个较旧的分支，你的工作目录会恢复到该分支最后一次提交时的样子。如果 Git 不能干净利落地完成这个任务，它将禁止切换分支。

你可以简单地使用 `git log` 命令查看分叉历史。 运行 `git log --oneline --decorate --graph --all` ，它会输出你的提交历史、各个分支的指向以及项目的分支分叉情况。


## 3.2. 分支的新建与合并
### 3.2.1. 新建分支
想要新建一个分支并同时切换到那个分支上，你可以运行一个带有 `-b` 参数的 `git checkout` 命令：
```bash
$ git checkout -b iss53
Switched to a new branch "iss53"

$ git branch -d hotfix
Deleted branch hotfix (3a0874c).
```

当完成运行测试，确保修改是正确的，然后将 `hotfix` 分支合并回你的 `master` 分支来部署到线上。 你可以使用 `git merge` 命令来达到上述目的：
![basic-branching-4](./../images/basic-branching-4.png)
合并后的效果即是将`master`移动到`hotfix`上
![basic-branching-5](./../images/basic-branching-5.png)


### 3.2.2 分支的合并
简单的合并可以分为两步，从当前修改的分支checkout到 `master` 分支，然后执行 `git merge <branch-name>` 进行合并。
```bash
$ git checkout master
Switched to branch 'master'
$ git merge iss53
Merge made by the 'recursive' strategy.
index.html |    1 +
1 file changed, 1 insertion(+)
```

如果当前分支和 `master` 分支之间存在分叉，又该如何合并呢？ Git 会找到两个分支的共同祖先，执行简单的三方合并。
合并前如下：
![before merging](./../images/basic-merging-1.png)
合并后的效果如下：
![after merging](./../images/basic-merging-2.png)
合并完成后，即和删除没有用的分支了： `git branch -d iss53`


### 3.2.3 遇到冲突时的分支合并
有时候合并操作不会如此顺利。**如果你在两个不同的分支中，对同一个文件的同一个部分进行了不同的修改，Git 就没法干净的合并它们。**

虽然 Git 做了合并，但是没有自动地创建一个新的合并提交。 Git 会暂停下来，等待你去解决合并产生的冲突。 你可以在合并冲突后的任意时刻使用 `git status` 命令来查看那些因包含合并冲突而处于未合并（unmerged）状态的文件：
![unmerged](./../images/unmerged.png)
出现冲突的文件会如下图所示，`=======` 的上下两个半部分分别属于不同的分支，用户需要自己决定保留哪一个，删掉哪一个。
![conflict](./../images/conflict.png)


## 3.3. 分支管理
`git branch` 命令不只是可以创建与删除分支。 如果不加任何参数运行它，会得到当前所有分支的一个列表：
```bash
$ git branch
  iss53
* master
  testing
```
`*`字符代表当前`HEAD`指向的分支。

如果需要查看每一个分支的最后一次提交，可以运行 `git branch -v` 命令。

`--merged` 与 `--no-merged` 这两个有用的选项可以过滤这个列表中已经合并或尚未合并到当前分支的分支。


### 3.4. 分支开发工作流
常见的利用分支进行开发的工作流程。


### 3.4.1 长期分支
在整个项目开发周期的不同阶段，你可以同时拥有多个开放的分支；你可以定期地把某些主题分支合并入其他分支中。
许多使用 Git 的开发者都喜欢使用这种方式来工作，比如只在 master 分支上保留完全稳定的代码——有可能仅仅是已经发布或即将发布的代码。 他们还有一些名为 develop 或者 next 的平行分支，被用来做后续开发或者测试稳定性——这些分支不必保持绝对稳定，但是一旦达到稳定状态，它们就可以被合并入 master 分支了。
![lr-branches](./../images/lr-branches-2.png)


### 3.4.2. 主题分支
主题分支对任何规模的项目都适用。 主题分支是一种短期分支，它被用来实现单一特性或其相关工作。

![topic-branches](./../images/topic-branches-1.png)


## 3.5. 远程分支
远程引用是对远程仓库的引用（指针），包括分支、标签等等。 你可以通过 `git ls-remote <remote>` 来显式地获得远程引用的完整列表， 或者通过 `git remote show <remote>` 获得远程分支的更多信息。 然而，一个更常见的做法是**利用远程跟踪分支**。
![remote-branch](./../images/remote-branches-1.png)

如果你在本地的 master 分支做了一些工作，在同一段时间内有其他人推送提交到 `git.ourcompany.com` 并且更新了它的 `master` 分支，这就是说你们的提交历史已走向不同的方向。 即便这样，只要你保持不与 `origin` 服务器连接（并拉取数据），你的 `origin/master` 指针就不会移动。


### 3.5.1. 推送
当你想要公开分享一个分支时，需要将其推送到有写入权限的远程仓库上。 本地的分支并不会自动与远程仓库同步——你必须显式地推送想要分享的分支。 这样，你就可以把不愿意分享的内容放到私人分支上，而将需要和别人协作的内容推送到公开分支。


**Note:** 如何避免每次输入密码

如果你正在使用 `HTTPS URL` 来推送，Git 服务器会询问用户名与密码。 默认情况下它会在终端中提示服务器是否允许你进行推送。

如果不想在每一次推送时都输入用户名与密码，你可以设置一个 “credential cache”。 最简单的方式就是将其保存在内存中几分钟，可以简单地运行 `git config --global credential.helper cache` 来设置它。


### 3.5.2. 跟踪分支


### 3.5.3. 拉取
当 `git fetch` 命令从服务器上抓取本地没有的数据时，它并不会修改工作目录中的内容。它只会获取数据然后让你自己去合并。

`git pull` 命令在大多数情况下的含义是 `git fetch` 紧接着一个 `git merge` 命令。

由于 git pull 的魔法经常令人困惑所以通常单独显式地使用 fetch 与 merge 命令会更好一些。


### 3.5.4. 删除远程分支
假设你已经通过远程分支做完所有的工作了——也就是说**你和你的协作者已经完成了一个特性**， 并且将其合并到了远程仓库的 `master` 分支（或任何其他稳定代码分支）。 可以运行带有 `--delete` 选项的 `git push` 命令来删除一个远程分支。 如果想要从服务器上删除 serverfix 分支，运行下面的命令：
```bash
$ git push origin --delete serverfix
To https://github.com/schacon/simplegit
 - [deleted]         serverfix
```
基本上这个命令做的只是从服务器上移除这个指针。 Git 服务器通常会保留数据一段时间直到垃圾回收运行，所以如果不小心删除掉了，通常是很容易恢复的。


---
## 3.6. 变基
在 Git 中整合来自不同分支的修改主要有两种方法： `merge` 和 `rebase` 。

### 3.6.1. 变基的基本操作
当开发任务分叉到两个不同的分支，有各自提交了更新时，如下图所示：

![basic rebase 1](./../images/basic-rebase-1.png)

根据简单的 `merge` 命令。它会把两个分支的最新快照（C3 和 C4）以及二者最近的共同祖先（C2）进行三方合并，合并的结果是生成一个新的快照（并提交）。

![basic rebase 2](./../images/basic-rebase-2.png)

其实，还有一种方法：你可以提取在 C4 中引入的补丁和修改，然后在 C3 的基础上应用一次。 在 Git 中，这种操作就叫做 变基（`rebase`）。 你可以使用 rebase 命令将提交到某一分支上的所有修改都移至另一分支上，就好像“重新播放”一样。  ==> 提取 C4 的变化，添加到 C3 上。
即从 `experiment` 分支上 `checkout`，停在 `master` 分支，然后 `rebase`，代码如下所示：
```bash
$ git checkout experiment
$ git rebase master
First, rewinding head to replay your work on top of it...
Applying: added staged command
```

![basic rebase 3](./../images/basic-rebase-3.png)

此时，C4' 指向的快照就和 the merge example 中 C5 指向的快照一模一样了。 这两种整合方法的最终结果没有任何区别，但是变基使得提交历史更加整洁。 你在查看一个经过变基的分支的历史记录时会发现，尽管实际的开发工作是并行的， 但它们看上去就像是串行的一样，提交历史是一条直线没有分叉。  ==> 即 `merge` 和 `rebase` 的结果是一致的，但是 `rebase` 的最终结果更简洁。

请注意，无论是通过变基，还是通过三方合并，整合的最终结果所指向的快照始终是一样的，只不过提交历史不同罢了。 变基是将一系列提交按照原有次序依次应用到另一分支上，而合并是把最终结果合在一起。


### 3.6.2. 更有趣的变基例子
![interesting rebase 1](./../images/interesting-rebase-1.png)

目标：希望将 `client` 分支中的修改合并到 `master` 分支并发布，但是暂时不想合并 `server` 中的修改，因为它们还要经过更全面的测试。这时候可以使用 `git rebase` 命令的 `--onto` 选项，选中在 `client` 分支里，但不在 `server` 分支里的修改，将它们在 `master` 分支上重放：

```bash
$ git rebase --onto master server client
```

以上命令的意思是：“取出 client 分支，找出它从 server 分支分歧之后的补丁， 然后把这些补丁在 master 分支上重放一遍，让 client 看起来像直接基于 master 修改一样”。这理解起来有一点复杂，不过效果非常酷。

![interesting rebase 2](./../images/interesting-rebase-2.png)

然后可以进行快速合并 `master` 分支：
```bash
$ git checkout master
$ git merge client
```

![interesting rebase 3](./../images/interesting-rebase-3.png)

然后再用 `git rebase <bash-branch> <topic-branch>` 将 `server` 分支变基到 `master` 分支：

```bash
$ git rebase master server
```
![interesting rebase 4](./../images/interesting-rebase-4.png)

然后再进行快速合并到分支 `master`，最后删除 `client` 和 `server` 分支：

```bash
$ git checkout master
$ git merge server

$ git branch -d client
$ git branch -d server
```
![interesting rebase 5](./../images/interesting-rebase-5.png)


### 3.6.3. 变基的风险
奇妙的变基也并非完美无缺，要用它得遵守一条准则：

**如果提交存在于你的仓库之外，而别人可能基于这些提交进行开发，那么不要执行变基。（Do not rebase commits that exist outside your repository and that people may have based work on.）**

*例子让我很晕*


### 3.6.4. 用变基解决变基
？？？


### 3.6.5. 变基 v.s. 合并
`merge`： **记录实际发生过什么**

`rebase`：**项目过程中发生的事**

总的原则是，**只对**尚未推送或分享给别人的**本地修改**执行变基操作清理历史，从不对已推送至别处的提交执行变基操作，这样，才能享受两种方式带来的便利。



--20200508
