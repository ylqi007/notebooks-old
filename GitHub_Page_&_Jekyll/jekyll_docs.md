[toc]

## TODO

- [x] 什么是 jekyll，可以干什么，怎么用
- [x] 什么是 `gem`
- [x] 什么是 `jekyll`
- [x] 什么是 `bundle`
- [x] install dependencies



## Jekyll on Ubuntu -- Install dependencies

1. Install Ruby and other dependencies: 

   ```bash
   sudo apt-get install ruby-full build-essential zlib1g-dev
   ```

2. Avoid installing RubyGems packages (called gems) as the root user. Instead, set up a gem installation directory for your user account. 为了避免以 root user 的身份安装 Ruby 软件包(也就是一些 gem 包)，可以提前设定 gem 包的安装目录。

   ```bash
   echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
   echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
   echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. Finally, install `Jekyll` and `Bundler`.

   ```bash
   gem install jekyll bundler
   ```

---

## Command Line Usage

The Jekyll gem makes a `jekyll` executable available to you in your terminal.

The `jekyll` program has several commands but the structure is always:

```bash
jekyll command [argument] [option] [argument_to_option]

Examples:
    jekyll new site/ --blank
    jekyll serve --config _alternative_config.yml
```

Here are some of the most common commands:

* `jekyll build`  when you need to generate the site for production. Performs a one off build your site to `./_site/`  by default.
* `jekyll serve` when developing locally for production. Builds your site any time a source file changes and serves it locally.
* `jekyll new <PATH>` Creates a new Jekyll site with default gem-based theme at specified path. The directories will be created as necessary.
* `jekyll new <PATH> --blank` Creates a new blank Jekyll site scaffold at specified path. 在指定的路径处创建一个新的空白Jekyll站点支架。
* `jekyll clean`  Removes all generated files: destination folder, metadata file, Sass and Jekyll caches. 
* `jekyll help`  Shows help, optionally for a given for a given subcommand, e.g. `jekyll help build`.
* `jekyll new-theme`  Creates a new Jekyll theme scaffold.
* `jekyll doctor`  Outputs any deprecation or configuration issues.

## 名词解释

* **RubyGems:** RubyGems 是一个方便而且强大的 Ruby 程序包管理器(package manager)，类似与 RedHat 的 RPM。它将一个 Ruby 应用程序打包到一个 gem 里，作为一个安装单元。无需安装，最新的 Ruby 版本，已经包含 RubyGems 了。
* **Gem:** Gem 是封装起来的 Ruby 应用程序或代码库。
* **注:** 在 terminal 中使用的 gem 命令，是指通过 RubyGems 管理 Gem 包。
* **Jekyll:** Jekyll 是一个静态网张生成器。
* **Bundler:** `Bundler` 是管理 Gem 相依性的工具，执行 `bundle install` 的时候，会根据 Gemfile 文件中的设定，检查指定的 Gem 与相关的套件是否已经安装。如果已经安装，则会显示 `Using`；如果是新下载安装的 Gem，则会显示 `Installing`。如果想知道已安装的 Gem 安装在哪里，可以使用 `bundle info gemname` 查看。



## References

1. [整理Ruby相关的各种概念（rvm, gem, bundle, rake, rails等](https://blog.csdn.net/sinat_25419171/article/details/51111639?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)
2. [初探Jekyll（一）：Jekyll是什么？Jekyll常用的专业名词](https://blog.csdn.net/yq_forever/article/details/103449864)
3. [簡介 Bundler](https://openhome.cc/Gossip/Rails/Bundler.html)
4. [Offical Liquid Document](https://shopify.github.io/liquid/)
5. [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
6. [How do I upgrade to Ruby 2.2 on my Ubuntu system?](https://askubuntu.com/questions/839775/how-do-i-upgrade-to-ruby-2-2-on-my-ubuntu-system)