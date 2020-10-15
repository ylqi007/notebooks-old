[TOC]

## TODO

- [ ] 什么是 plugins，该如何使用？
- [ ] `jekyll-sitemap` ?
- [ ] `jekyll-feed` ?
- [ ] `jekyll-seo-tag` ?
- [ ] 如何更换 theme？
- [ ] 如何使用 Environment？如何使用？
- [ ] `site.url` vs `site.baseurl`?

# Transform your plain text into static websites and blogs 将静态文本转换成静态网站和博客

* Simple: 不需要数据库，评论模块，或者复杂的更新，仅仅需要关注内容就好。
* Static: 可以引入 Markdown, Liquid, HTML & CSS，静态网页一旦准备好就可以部署。
* Blog-aware: 

---
## Ruby101
* **Gems:** Gems are code you can include in Ruby projects. Gems package specific functionality. Jekyll is a gem. Gems can perform actions like: 
  1. Converting a Ruby object to JSON
  2. Pagination
  3. Interacting with APIs such GitHub
* **Gemfile:** A `Gemfile` is a list of gems used by your site. Every Jekyll site has a Gemfile in the main folder.
* **Bundler:** Bundler is a gem that installs all gems in your `Gemfile`.


---
## Step by Step Tutorial
### 1. Setup
从头开始创建一个不依赖 gem-based theme 的 Jekyll site。

#### Installation
Jekyll 是 Ruby 程序，因此可以先从安装 Ruby 开始。
当 Ruby 安装完成之后，可以通过下面命令安装 Jekyll:

```
gem install jekyll bundler
```
创建一个新 `Gemfile` 列出 project’s dependencies.
```
bundle init
```
编辑 `Gemfile`，添加 jekyll 依赖。
```ruby
gem "jekyll"
```
然后 run `bundle` 安装 jekyll。
往后就可以在 jekyll 命令前添加 `bundle exec`，保证 jekyll 的 version。[???]

##### Gemfile

1. 首先，要告诉 Gemfile 到哪里去找需要的 gems，因此也就是需要定义 gem 的源。比如 `source "https://rubygems.org"` ,不推荐一个项目有多个源。

2. 设置 Gems: 

   ```ruby
   gem "gem_name", ">= 0.0"
   ```

   设置需要的 Gem 和需要的版本。

3. 从 git 安装 gem: 可以设置 gem 的安装源为一个 git repo，比如 GitHub，只需要在设置 Gems 时，将 source 属性替换为 git。可以设置这个 repo 的链接为 HTTP(S), SSH, GIT 等协议，但最好使用 HTTP(S) 和 SSH，因为其他的会使你可能成为  man-in-the-middle 攻击的受害者。如果你把 gem 放入到 repo 里面，你必须要在 repo  根目录文件夹下面有一个.gemspec  文件。这里面需要包含一个合法 gem 的声明。如果你没有提供这个文件，Bundler  会尝试创建一个，但是他不会被依赖。如果你尝试去 include 一个没有提供.gemspec 文件的 git repo 里面的  gem，你必须指定一个版本号。你可以为 gem 设置 branch，tag，ref，默认是使用 master branch。你也可以强制 Bundler 扩展 submodule，通过以下方式来设置：

   ```ruby
   gem "my_gem", git: "ssh@githib.com/tosbourn/my_gem", branch: test_branch, submodules: true
   ```

4. 设置 Git 作为 source:  可以设置一个 URL 来作为一个更广义的源，你可以通过调用 `#git_source` 方法并将 name 作为参数传进去，以及一个接收一个参数的 block，并返回一个 string 作为 repo 的 URL。如下所示：

   ```ruby
   git_source(:custom_git){ |repo| "https://my_secret_git_repos.com/#{repo}.git" }
   gem "my_gem", custom_git: "tosbourn/test_repo"
   ```


#### Create a site
创建第一个 HTML 文件 `index.html`，包含内容如下:
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Home</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>
```

##### Build

Jekyll is a static site generator so we need Jekyll to build the site before we can view it. There are two commands you can run in the root of your site to build it:
Jekyll 是静态网站生成器，在要看 site 之前，我们需要 Jekyll 创建 site。有两种命令可以用于生成 site，在项目目录下运行：

* `jekyll build` - 创建网站，输出一个静态网站到 `_site/` 目录下。
* `jekyll serve` - 与上述命令一样，不过这条命令还可以在你修改 project 之后随时 rebuild，然后在运行一个本地网站: `http://localhost:4000`
  


### 2. Liquid
> Liquid is where jekyll starts to get more interesting. Liquid is a templating language which has three main parts: `objects`, `tags` and `filters`. 
> Liquid 是一个模板语言，包含三个主要的部分 `objects`, `tags` and `filters`.
* **Objects:** Objects tell Liquid where to output content. They are denoted by double curly braces: `{{` and `}}`. Objects 告诉 Liquid 模板在哪里输出内容。
  * `{{ page.title }}` outputs a variable called `page.title` on the page. 比如 `{{ page.title }}` 在页面输出一个叫做 `page.title` 的变量。
* **Tags:** Tags create the logic and control flow for templates. The are denoted by curly brances and percent signs: `{%` and `%}`. Tags 创建模板的逻辑和控制流程。
* **Filters:** Filters change the output of a Liquid object. They are used within an output and are separated by a `|`. Filter 用于改变 Liquid Object 的输出内容。

#### Use Liquid

 To get changes processed by Jekyll we need to add `front matter` to the top of the page. 如果要想用 Liquid 模板，要在页面前添加 `front matter`.


### 3. Front Matter
> Front matter is a snippet of `YAML` which sits between two triple-dashed lines at the top of a file. Front matter is used to set variables for the page.
> Front matter 是 `YAML` 的一个片段，内容在两行 `---` 之间，放在文件的头部。Front matter 用于设置页面的变量。
> Front matter variables are available in Liquid under the page variable. 
> 在 Front matter 中定义的变量在 Liquid 中，是在变量 `page` 之下。
* Note that in order for Jekyll to process any liquid tags on your page, you must include front matter on it.
* Front matter variables are available in Liquid under the `page` variable.
* 要想 liquid tags 起作用，在 page 上必须添加 (front matter). The most minimal snippet of front matter you can include is:
```
---
---
```
在页面的头部添加两行 `---` 就可以起到 front master 的作用。

### 4. Layouts
> Jekyll supports Markdown as well as HTML for pages.
> 如果每创建一个页面都需要进行排版的话，则会非常繁琐复杂，比如为了给每个页面添加一个 stylesheet(css)，则不得不到每个页面的 `<head>` 里进行修改，即使一个简单的修改都需要很长的时间。

#### Creating a layout
* Using a layout is a much better choice. Layouts are templates that wrap around your content. They live in a directory called `_layouts/`.
使用布局(layouts) 则会非常简单方便。Layouts 是一个包含 content 的模板。它们放置在 `_layouts/` 之下。
* Create the first layout at `_layouts/default.html`.
创建的 `_layouts/default.html` 与 `/index.html` 几乎是一致的，都有两点不同:
   * 在 `_layouts/default.html` 没有 front matter，也就是没有 `/index.html` 页面头部的两行 `---`;
   * 在 `_layouts/default.html` 中没有 `<body>` 中的内容，而是由 liquid.object `{{ content }}` 代替。`content` is a special variable which has the value of the rendered content of the page it’s called on.
  To have `index.html` use this layout, you can set a `layout` variable in front matter. The layout wraps around the content of the page

#### Using layout in about page 
* 在 run `jekyll serve` 之后，会在 `_sites` 下生成 `_sites/about.html`，然后在 Brower 中打开 `http://localhost:4000/about.html`。 


### 5. Includes
**Navigation** should be on every page so adding it to your layout is the correct place to do this. 
为了在每个页面之间实现切换，可以在每个页面中加入导航(navigation)，可以在 `default.html` layout 中加入。为了学习使用 `includes`，这次使用 `includes` 实现 navigation。

#### Include tag
The `include` tag allows you to include content from another file stored in an `_includes` folder. Includes are useful for having a single source for source code that repeats around the site or for improving the readability.
`include` tag 允许我们从 `_includes/` 中添加内容。对于要重复使用的内容非常有用。

#### Include usage

Create a file for the navigation at `_includes/navigation.html`.
Try using the include tag to add the navigation to `_layouts/default.html`

通过创建 `_layouts/navigation.html`，`navigation.html` 中包含到各个网页的链接。

#### Current page highlighting
Let’s take this a step further and highlight the current page in the navigation.
`_includes/navigation.html` needs to know the URL of the page it’s inserted into so it can add styling. Jekyll has useful `variables` available, one of which is `page.url`. 


### 6. Data Files
Jekyll supports loading data from YAML, JSON, and CSV files located in a `_data` directory. Data files are a great way to separate content from source code to make the site easier to maintain.
In this step you’ll store the contents of the navigation in a data file and then iterate over it in the navigation include. 在这步中，我们将 navigation 中的内容保存到 data file 中，然后遍历添加到 navigation 中。如果 `navigation` 中需要添加多个 hyperlink，可以在 `_data/navigation.yml` 中添加保存，然后在 `_layouts/navigation.html` 中调用即可。

#### Data file usage
`YAML` is a format that’s common in the Ruby ecosystem. You’ll use it to store an array of navigation items each with a name and link.
Create a data file for the navigation at `_data/navigation.yml`.
Jekyll makes this data file available to you at `site.data.navigation`. Instead of outputting each link in `_includes/navigation.html`, now you can iterate over the data file instead.


### 7. Assets
Using CSS, JS, images and other assets is straightforward with Jekyll. Place them in your site folder and they’ll copy across to the built site.

#### Sass
Inlining the styles used in `_includes/navigation.html` is not a best practice, let’s style the current page with a class instead. 用 inline style 的方式给 navigation 中的元素添加 style，这不是最好的方式。可以通过定义 class 的方式取代。
You could use a standard CSS file for styling, we’re going to take it a step further by using Sass. Sass is a fantastic extension to CSS baked right into Jekyll. 关于 style 的定义，可以直接使用 CSS，也可以直接使用 Sass，Sass 是 CSS 的 extension，对于 Jekyll 可以直接使用。
First create a Sass file at `assets/css/styles.scss`，然后通过 `@import "main";` 调用 sass 目录 (`_sass/`) 下的 `main.scss`.

#### Note!

在 HTML 中调用头部调用的是 `<link rel="stylesheet" href="/assets/css/styles.css">`，注意是 `styles.css` 而不是 `styles.scss`。此处的 `styles.css` 是 Jekyll 从 `assets/css/styles.scss` 文件中生成的。


### 8. Blogging
In true Jekyll style, blogging is powered by text files only.

#### Posts
Blog posts live in a folder called `_posts`. The filename for posts have a special format: the publish date, then a title, followed by an extension. Blog posts 文件在 `_posts` 下，并且有一个特殊的命名格式，发布日期，标题和一个 extension。

#### Layout
The post layout doesn’t exist so you’ll need to create it at `_layouts/post.html` which is an example of layout inheritance.

#### List posts
There’s currently no way to navigate to the blog post. Typically a blog has a page which lists all the posts, let’s do that next.
Jekyll makes posts available at `site.posts`. 目前没有直接的方法访问 blog post，可以通过 jekyll 自动生成的链接来访问。

- `post.url` is automatically set by Jekyll to the output path of the post
- `post.title` is pulled from the post filename and can be overridden by setting `title` in front matter
- `post.excerpt` is the first paragraph of content by default


### 9. Collections
使用**合集**，需要一下三步：

1. 告诉Jekyll读取你的合集
2. 添加你的内容
3. 有选择地将你的合集文档渲染为独立的文件

* Let’s look at fleshing out authors so each author has their own page with a blurb and the posts they’ve published.
  充实每个 author 的页面，使每个 author 都有一个单独的页面，包含 author 的基本信息和发布文章的列表。* 

* Collections are similar to posts except the content doesn’t have to be grouped by date.
  Collections 与 posts 相似，但是不用按照 date 分组。

#### Configuration
To set up a collection you need to tell Jekyll about it. Jekyll configuration happens in a file called `_config.yml` (by default).

#### Add authors
Documents (the items in a collection) live in a folder in the root of the site named `_*collection_name*`. In this case, `_authors`.

#### Staff page
Let’s add a page which lists all the authors on the site. Jekyll makes the collection available at `site.authors`.
Create `staff.html` and iterate over `site.authors` to output all the staff.

#### Output a page
By default, collections do not output a page for documents. In this case we want each author to have their own page so let’s tweak the collection configuration.
Open `_config.yml` and add `output: true` to the author collection configuration.

要设置 `output: true` 并重新 restart serve 才可以是这个 configuration 生效。

#### Front matter defaults

如果我们想要所有的 posts 都自动地带有 post layout，authors 都自动带有 author layout，其他的所有的都使用 default layout。要如何实现呢？

**You can achieve this by using `front matter defaults` in `_config.yml`. ** You can set a scope of what the default applies to, then the default front matter you'd like.

Using *front matter defaults* in `_config.yml`. You set a scope of what the default applies to, then the default front matter you'd like.

#### List autho's posts

列出每个 author 发表的所有文章。为实现这个，要将作者的 `short_name` 与发布作者 `author` 匹配。所以我们需要使用 filter 过滤与 `author` 匹配的 `post`。

```gem
{% assign filtered_posts = site.posts | where: 'author', page.short_name %}
```

在 `_layout/post.html` 中为每个 author 添加 link，指向相应作者的页面。


### 10. Gemfile

#### Gemfile

It's good practice to have a `Gemfile` for site. This ensures the version of Jekyll and other gems remains consistent across different environments. 最好有一个 `Gemfile` 文件记录所需要的 gems 的版本。

When using a `Gemfile`, you'll run commands like `jekyll serve` with `bundle exec` prefixed. So the full command is: `bundle exec jekyll serve`. 当使用 Gemfile 时，运行 `jekyll serve` 命令默认添加了前置 `bundle exec`，所以完整的命令就是 `bundle exec jekyll serve`。 

This restricts your Ruby environment to only use gems set in your `Gemfile`。

#### Plugins
Jekyll plugins allow you to create custom generated content specific to your site. Jekyll 插件可以定制生成不同的内容。比如，
* `jekyll-sitemap` - Creates a sitemap file to help search engines index content

* `jekyll-feed` - Creates an RSS feed for your posts

* `jekyll-seo-tag` - Adds meta tags to help with SEO

要使用 plugins，分别要在 `Gemfile` 和 `_config.yml` 中作出修改。

#### Environments
Sometimes you might want to output something in production but not in development. **Analytics** scripts are the most common example of this. 有时候需要在 production 的过程中进行调试，而不是直接 development。Analytics 脚本常常用于这种目的。
To do this you can use environments. You can set the environment by using the `JEKYLL_ENV` environment variable when running a command. 可以在运行一个命令的时候，添加上 `JEKYLL_ENV` 环境变量。比如

```bash
JEKYLL_ENV=production bundle exec jekyll build
```

By default `JEKYLL_ENV` is **development**. The `JEKYLL_ENV` is available to you in liquid using `jekyll.environment`(默认的时候，也就是在运行命令的时候不指定 `JEKYLL_ENV` 的时候，默认是 `development`。). So to only output the analytics script on production you would do the following (如果仅仅想要分析的脚本文件出现在 production 过程中，则可以添加以下代码片段):

```
{% if jekyll.environment == "production" %}
  <script src="my-analytics-script.js"></script>
{% endif %}
```

#### Deployment

The final step is to get the site onto a *production server*. The most basic way to do this is to run a production build:

```bash
JEKYLL_ENV=production bundle exec jekyll build
```

And copy the contents of `_site` to your server. 在 build 完成之后，把生成的 `_site/` 的内容放置到服务器上就可以了。

##### Development and Production

* **Development:**  在开发过程中，我们需要在本地打开网页查看，此时默认的 `site.url = http://localhost:4000` and `site.baseurl=/jekyll-demo`
* **Production:** 在开发完成后，需要部署的时候，此时要设置 `site.url=https://ylqi007.github.io` and `site.baseurl=/jekyll-demo`
* 可以参考 [ref 8](https://stackoverflow.com/questions/27386169/change-site-url-to-localhost-during-jekyll-local-development), 为 development 和 production 设置不同的 config file。

#### Wrap up



---

# Environments

In the `build` or `sever` arguments, you can specify a Jekyll environment and value. The build will then apply this value in any conditional statements in your content. 我们可以在 `build` or `serve` 的时候，设置 Jekyll environment 变量，然后在 `build/serve` 的时候，环境变量的参数值可以用于 statement 中。

We need to understand `site.url` and `site.baseurl` and in which situation we need them. Those variables don't serve the same purpose.

* `site.url` By default, this variable is only used in page head for the `canonical` header and the `RSS link`.
* `site.baseurl` This variable indicates the root folder of your Jekyll site. By default it is set to `""`(empty string). That means that your Jekyll site is at the root of `http://example.com`. If your Jekyll site lives in `http://example.com/blog`, you have to set `site.baseurl` to `/blog` (**note the slash**).

---

# Themes

## 1. Pickup a theme

## 2. Understanding gem-based themes

When you create a new Jekyll site (by running the `jekyll new <PATH>` command), Jekyll installs a site that uses a gem-based theme called **Minima**.

With gem-based themes, some of the site's directories (such as the `assets`, `_layout`, `_includes`, and `_sass` directories) are stored in the theme's gem, hidden from your immediate view. Yet all of the necessary directories will be read and processed during Jekyll's build process.

The `Gemfile` and `Gemfile.lock` files are used by Bundler to keep track of the required gems and gem versions you need to build your Jekyll site.

If you have the theme gem, you can (if you desire) run `bundle update` to update all gems in your project. Or you can run `bundle update <THEME>`, to just update the theme gem.  
如果你使用的是 gem-based theme，则如果 theme 更新的话，进通过 `bundle update <THEME>` 就可以更新本地的 theme。

## 3. Overriding theme defaults

Jekyll themes set default layouts, includes, and stylesheets. However, you can override any of the theme defaults with your own site content.

To replace layouts or includes in your theme, make a copy in your `_layouts` or `_includes` directory of the specific file you wish to modify, or create the file from scratch giving it the same name as the file you wish to override.

## 4. Converting gem-based themes to regular themes

Suppose you want to get rid of the gem-based theme and convert it to a regular theme, where all files are present in your Jekyll site directory, with nothing stored in the theme gem. 
如果不想用 gem-based theme，而是想把所有的文件放在 Jekyll site 目录下，没有什么内容保存在 theme gem 中。

To do this, copy the files from the theme gem's directory into your Jekyll site directory.

Then you must tell Jekyll about the plugins that were referenced by the theme. You can find these plugins in the theme's gemspec file as runtime dependencies. You should include these references in the `Gemfile` and `_config.yml`. And then, don't forget to `bundle update'.

If you're publishing on GitHub Pages, you should update only your `_config.yml` as GitHub Pages doesn't load plugins via Bundler. 
如果要将网页用 GitHub Pages 发布，则只可以更新 `_config.yml`, 因为 GitHub Pages 不会通过 Bundler 安装插件。

Finally, remove references to the theme gem in `Gemfile` and configuration. Now `bundle update` will no longer get updates for the theme gem.

## 5. Installing a gem-based theme

The `jekyll new <PATH>` command isn't the only way to create a new Jekyll site with a gem-based theme. you can also find gem-based themes online and incorporate them into your Jekyll project. For example, search for [jekyll theme on RubyGems](https://rubygems.org/search?utf8=%E2%9C%93&query=jekyll-theme) to find other gem-based themes.

### To install a gem-based theme:

1. Add the theme gem to your site's `Gemfile`: 

   ```ruby
   # ./Gemfile
   # This is an example, declare the theme gem you want to use here
   gem "jekyll-theme-minimal"
   ```

2. Install the theme:

   ```bash
   bundle install
   ```

3. Add the following to your site's `_config.yml` to activate the theme:

   ```ruby
   theme: jekyll-theme-minimal
   ```

4. Build your site:

   ```bash
   bundle exec jekyll serve
   ```

* You can have multiple themes listed in your site's `Gemfile`, but only one theme can be selected in your site's `_config.yml`. 
* If you're publising your Jekyll site on GitHub Pages, note that GitHub Pages supports only *some gem-based themes*. GitHub Pages also supports *using any theme hosted on GitHub* using the `remote_theme` configuration as if it were a gem-based theme.

## 6. Creating a gem-based theme




---
# Other Related Problems
## 1. 多个 GitHub Pages
### Questions
1. 每个 GitHub 帐号除了可以有一个 `username.github.io` 的 GitHub Pages 的项目之外，是否可以创建多个 GitHub Pages 项目。
2. GitHub Pages site 的域名设置。


## Reference
1. [Working with GitHub Pages](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages)
2. [Ruby - Gemfile 详解](https://ruby-china.org/topics/26655)
3. [What is a Gemfile](https://tosbourn.com/what-is-the-gemfile/)
4. [Ruby 实战 - Bundler](http://blog.danthought.com/programming/2015/05/02/ruby-in-action-bundler/)
5. [[Gemfile中新块"git_source(:github)"的含义](https://qa.1r1g.com/sf/ask/2901803341/#)](https://qa.1r1g.com/sf/ask/2901803341/)
6. [Liquid语言(jekyll所需)](https://gohom.win/2015/11/28/Liquid-jekyll/)
7. [《Jekyll使用教程笔记 五：合集、数据文件》](https://juejin.im/post/6844903630001160199)
8. [Change site.url to localhost during jekyll local development](https://stackoverflow.com/questions/27386169/change-site-url-to-localhost-during-jekyll-local-development)
9. [Jekyll简单总结](http://zhaoxuhui.top/blog/2017/03/21/Jekyll%E7%AE%80%E5%8D%95%E6%80%BB%E7%BB%93.html)
10. [Jekyll 中的配置和模板语法](https://gist.github.com/biezhi/f88be58ef4ae0f3741bb36ab8daa53c5)
11. [Jekyll/Liquid API 语法文档](https://kang000feng.github.io/blog/2015/01/10/jekyll-liquid-syntax-documentation/)
12. [Jekyll Cheat Sheet](https://learn.cloudcannon.com/jekyll-cheat-sheet/)
13. [Adding a theme to your GitHub Pages site using Jekyll](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/adding-a-theme-to-your-github-pages-site-using-jekyll#adding-a-theme)

