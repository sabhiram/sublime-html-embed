# HTML Embed

A SublimeText plugin to convert back and forth from HTML to embed-able lines. Particularly useful when writing or modifying HTML templates within a directive etc.

![](https://raw.githubusercontent.com/sabhiram/public-images/master/sublime-html-embed/sublime-html-embed.gif)

## Usage:

To convert from HTML to Embedable lines (or vice versa):
1. Select some HTML (or embeded lines)
2. Press:

|    OS   | Key Combination           |
| ------- | ---------------           |
| Linux   | ctrl + alt + T            |
| Mac     | super(⌘) + alt + ctrl + T |
| Windows | ctrl + alt + T            |


## Installation

The easiest way to install `HTML Embed` is to install it from Package Control

### Package Control Install (Not added yet...)

If you have [Package Control](https://sublime.wbond.net/installation) installed, then simply naviagte to `Package Control: Install Package` and select the `HTML Embed` plugin and you are done!

### Manual Install 

From SublimeText `Packages` folder:
```sh
git clone git@github.com:sabhiram/sublime-html-embed.git sublime-html-embed
```

## Settings & Default Key Mapping

Currently there are no exposed settings used by this plugin

## Developers

Appreciate the help! Here is stuff you should probably know:

### Install for both Sublime Text 2 and 3:

Some folks prefer to clone the git repo right into their SublimeText `Packages` folder. While this is probably ok for most users, I prefer to create a symbolic link to the package so that I can point to the plugin from both flavors of SublimeText (for testing and the like...)

```sh
cd ~/dev
git clone git@github.com:sabhiram/sublime-html-embed.git sublime-html-embed
ln -s sublime-html-embed ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/sublime-html-embed
ln -s sublime-html-embed ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/sublime-html-embed
```

## Versions Released

#### 1.0.0 - Initial Release

1. Implements basic plugin functionality
2. Ready for package control deployment
