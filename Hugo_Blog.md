[TOC]



## 1. Quick Start

### 1.1 Install Hugo

[Hugo Install on Ubuntu](https://gohugo.io/getting-started/installing/#debian-and-ubuntu)



### 1.2 Create a New Site

```bash
hugo new site quickstart
```

* The above will create a new Hugo site in a folder named `quickstart`



### 1.3 Add a Theme

First, download the theme from GitHub and add it to your site's `themes` directory

```bash
cd quickstart
git init
git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
```

Then, add the theme to the site configuration:

```bash
echo 'theme = "ananke"' >> config.toml
```



### 1.4 Add Some Content

You can manually create content files (for example, `content/<CATEGORY>/<FILE>.<FORMAT>`) and provide metadata in them.

You can also use the `new` command to do a few things, like adding title and date. 

```bash
hugo new posts/my-first-post.md
hugo new articals/my-first-artical.md
hugo new tutorials/my-first-turorial.md
```

The newly created file will start with something like the following, and you can edit content file if you want.

```markdown
---
title: "My First Post"
date: 2019-03-26T08:47:11+01:00
draft: true
---
```

* `draft: true` means that this file does not get deployed. Once you finish a post, update the header of the post to `draft: false'



### 1.5 Start the Hugo Server

Start the Hugo server with drafts enabled:

```bash
hugo server -D
```



### 1.6 Customize the Theme

#### Site Configuration

If you already have a domain ready, set the `baseURL`. Not that this value is not needed when running the local development server.



### 1.7 Build Static Pages

```bash
hugo -D
```

This will output be in `./public/` directory by default. `-d/--destination` flag to change the default output directory, or set `publishdir` in the config file. 



## 2. Basic Usage

### 2.1 The `hugo` Command

The most common usage is probably to run `hugo` with the current directory being the input directory. (也就是直接运行 `hugo`)

Running `hugo` generates your website to the `public/` directory by default, although you can customize the output directory.

The command `hugo` renders your site into `public/` dire and is ready to be deployed to your web server. (`/public` 中的内容就可以部署到网站服务器上)



### 2.2 Draft, Future, and Expired Content



### 2.3 Deploy Your Website

After running `hugo server` for local web development, you need to do a final `hugo` run without the `server` part of the command to rebuild your site. (`hugo server` 用于本地测试；`hugo` 用于创建将要部署到 web server 的文件内容). 

* Running `hugo` does not remove generated files before building. This means that you should delete your `public/` directory before running the `hugo` command.

You may then deploy your site by copying the `public/` directory to your production web server.

Since Hugo generates a static website, your site can be hosted anywhere using any web server.



## 3. Content Organization

Hugo assumes that the same structure that works to organize your source content is used to organize the rendered site. [Hugo假定使用用于组织源内容的相同结构来组织呈现的网站。]

[Page Resources](https://gohugo.io/content-management/page-resources/)

[Image Processing](https://gohugo.io/content-management/image-processing/)

### 3.1 Organization of Content Source

In Hugo, your content should be organized in a manner that reflects the rendered website.

While Hugo supports content nested at any level, the top levels (i.e. `content/<DIRECTORIES>`) are special in Hugo and are considered the content to determine layouts etc.

[sections](https://gohugo.io/content-management/sections/)

Without any additional configuration, the following will just work:

```bash
.
└── content
    └── about
    |   └── index.md  // <- https://example.com/about/
    ├── posts
    |   ├── firstpost.md   // <- https://example.com/posts/firstpost/
    |   ├── happy
    |   |   └── ness.md  // <- https://example.com/posts/happy/ness/
    |   └── secondpost.md  // <- https://example.com/posts/secondpost/
    └── quote
        ├── first.md       // <- https://example.com/quote/first/
        └── second.md      // <- https://example.com/quote/second/
```

### 3.2 [Path Breakdown in Hugo](https://gohugo.io/content-management/organization/#path-breakdown-in-hugo)

#### Index Pages: `_index.md`

`_index.md` has a special role in Hugo. It allows you to add front matter and content to your [list templates](https://gohugo.io/templates/lists/).

### 3.3 Paths Explained

[Section](https://gohugo.io/content-management/organization/#section): A default content type is determined by a piece of content’s section. `section` is determined by the location within the project’s `content` directory. `section` *cannot* be specified or overridden in front matter.

[path](https://gohugo.io/content-management/organization/#path)

[url](https://gohugo.io/content-management/organization/#url)



## 4. Content Types

Hugo is build around content organized in sections. A **content type** is a way to organize your content. 

[Content View Templates](https://gohugo.io/templates/views)

[Hugo's Lookup Order](https://gohugo.io/templates/lookup-order/)



## 5. [Host on GitHub](https://gohugo.io/hosting-and-deployment/hosting-on-github/)

### 5.1 Types of GitHub Pages

There are 2 types of GitHub Pages:

* User/Organization Pages: `https://<Username|Organization>.github.io/`
* Project Pages: `https://<Username|Organization>.github.io/<Project>/`

### 5.2 [GitHub User or Organization Pages ](https://gohugo.io/hosting-and-deployment/hosting-on-github/#github-user-or-organization-pages)



### 5.3 [GitHub Project Pages](https://gohugo.io/hosting-and-deployment/hosting-on-github/#github-user-or-organization-pages)

> Make sure your `baseURL` key-value in configuration file reflects the full URL of your GitHub pages repository if you're using the default GitHub Pages URL(e.g. `<USERNAME>.github.io/<PROJECT>`) and not a custom domain.



## Reference

[Draft, Future, and Expired Content](https://gohugo.io/getting-started/usage/#draft-future-and-expired-content)

[Deploy Your Website](https://gohugo.io/getting-started/usage/#deploy-your-website)

[使用Hugo搭建个人博客](https://fengberlin.github.io/post/use-hugo-to-build-blog/)

[使用 Hugo 生成静态博客教程](https://sb.sb/blog/migrate-to-hugo/)

[使用hugo搭建个人博客站点](https://www.gohugo.org/post/coderzh-hugo/)

[Hugo创建个人博客指南](https://juejin.cn/post/6844903856887824398)

[Hugo-Octopress](https://themes.gohugo.io/hugo-octopress/)





