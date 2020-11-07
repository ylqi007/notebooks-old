* List all environments
```bash
conda info --envs
```

* [Rename environment name](../scripts/conda_environment_rename.sh)
* [How can I rename a conda environment?](https://stackoverflow.com/questions/42231764/how-can-i-rename-a-conda-environment)

* [How do I prevent Conda from activating the base environment by default?](https://stackoverflow.com/questions/54429210/how-do-i-prevent-conda-from-activating-the-base-environment-by-default)

  ```bash
  conda config --set auto_activate_base false	
  ```

* [How do I install Python OpenCV through Conda?](https://stackoverflow.com/questions/23119413/how-do-i-install-python-opencv-through-conda)

  ```bash
  conda install -c menpo opencv
  ```

* [Trouble installing 'easydict' package from conda prompt](https://stackoverflow.com/questions/47449723/trouble-installing-easydict-package-from-conda-prompt)

  ```bash
  conda install easydict -c conda-forge 
  ```

* [ImportError: No module named PIL](https://stackoverflow.com/questions/8863917/importerror-no-module-named-pil)

  ```bash
  conda install Pillow
  ```

  