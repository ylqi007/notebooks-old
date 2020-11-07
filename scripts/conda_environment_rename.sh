# https://gist.github.com/Mukei/db1ef8fdefe20fdb6aa8ed39610887b3
# One workaround is to create clone environment, and then remove original one:
# (remember about deactivating current environment with deactivate on Windows and source deactivate on macOS/Linux)

conda create --name new_name --clone old_name --offline #use --offline flag to disable the redownload of all your packages
conda remove --name old_name --all # or its alias: `conda env remove --name old_name`

# There are several drawbacks of this method:
# time consumed on copying environment's files,
# temporary double disk usage.
