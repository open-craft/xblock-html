# HTML XBlock

[![build](https://circleci.com/gh/open-craft/xblock-html/tree/master.svg?style=shield)](https://circleci.com/gh/open-craft/xblock-html/tree/master) [![codecov](https://codecov.io/gh/open-craft/xblock-html/branch/master/graph/badge.svg)](https://codecov.io/gh/open-craft/xblock-html)


A new HTML XBlock that is designed with security and embedding in mind. 

## Introduction
This XBlock provides a newer alternative to the existing HTML XModule in edX platform as it presents a number of 
problems when trying to embed it in another site (in particular, it often hosts content that depends on JS globals like 
jQuery being present, and it allows users to include arbitrary JavaScript).

## Installation
You may install XBlock-html using its setup.py, or if you prefer to use pip, run:

```shell
pip install https://github.com/open-craft/xblock-html
```
You may specify the `-e` flag if you intend to develop on the repo.

Note that as of version 1.0.0, Python 2.7 is no longer supported. The current minimum Python version is 3.5.

To enable this block, add `"html5"`, `"excluded_html5"` add `"markdown"` to the course's advanced module list. 
The options `Text`, `Exclusion` and `Markdown` will appear in the advanced components.

The `Markdown` block uses [markdown2](https://pypi.org/project/markdown2/) to translate the content into HTML, 
by default the following extras are included:

* "code-friendly"
* "fenced-code-blocks"
* "footnotes"
* "tables"
* "use-file-vars"

It is possible to configure more [extras](https://github.com/trentm/python-markdown2/wiki/Extras), by adding to the extras list under `"markdown"` key in `XBLOCK_SETTINGS`
at `/edx/etc/{studio|lms}.yml`

Example:
```
"XBLOCK_SETTINGS": {
    "markdown": {
        "extras": [
            "code-friendly",
            "fenced-code-blocks",
            "footnotes",
            "header-ids",
            "metadata",
            "pyshell",
            "smarty-pants",
            "strike",
            "target-blank-links",
            "use-file-vars",
            "wiki-tables",
            "tag-friendly",
        ]
    }
}
```

## Development
If you're willing to develop on this repo, you need to be familiar with different technologies and the repos' 
dependencies. However, to make things easier to setup and to manage, there're bunch of make commands that you can use
 to do things faster.
 
### Setting the requirements up
Hitting the following command will install in your python environment all the requirements you need for this project:

```shell
$ make requirements
```

### Running tests
Tests are essential for this project to keep all its features working as expected. To check your changes you can use:

```shell
$ make test
```
Or if you want to check the code quality only, hit:
```shell
$ make quality
```
