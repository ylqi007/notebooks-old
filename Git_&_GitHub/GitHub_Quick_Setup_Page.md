When you have a repository in your local machine and then you create a repository on GitHub, 
how should you connect the local and remote repository.

## Option: Create a repository locally and setup a remote
```bash
git init
git remote add origin git@github.com:<username>/<repository>.git
touch README.md
git commit -a -m "Created README"
git push -u origin master
```

* The following figure is the GitHub Quick Setup Page for new Github            
![Link local repo to remote repo](images/Github_Remote_Repo_Quick_Setup.png)


## References:
1. [When I created a repository on GitHub, it kept showing quick setup page. How should I remove that page and proceed?](https://stackoverflow.com/questions/53004615/when-i-created-a-repository-on-github-it-kept-showing-quick-setup-page-how-sho)

