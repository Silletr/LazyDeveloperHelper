# Lazy Developer Helper [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Lua](https://img.shields.io/badge/Lua-5.4.8-purple.svg?logo=lua&logoColor=white)](https://www.lua.org/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org)
[![Stars](https://img.shields.io/github/stars/Silletr/LazyDevHelper?style=flat-square&color=yellow)](https://github.com/Silletr/LazyDevHelper/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Silletr/LazyDevHelper/pulls)

## Contents
<!-- toc -->
- [Introduction](#introduction)
- [Features](#features)
- [Install using Packer](#install-using-packer)
- [Usage](#usage)
- [Status](#status)
<!-- tocstop -->

## Introduction

Have you ever found yourself adding multiple dependencies to your code before installing them? Do you hate switching between your editor and terminal? 🤔

LazyDevHelper solves this problem! It's a Neovim plugin that lets you manage Python dependencies directly from your editor, eliminating the need to switch to the terminal.

## Features

✨ Install Python packages directly from Neovim
✨ Manage dependencies without leaving your editor
✨ Compatible with modern Neovim configurations

### Installation Methods
## Install using Packer
```lua
use {
    'Silletr/LazyDevHelper',
    config = function()
        require('lazy-dev-helper').setup({
            -- Configuration options here
        })
    end
}
```
## Usage
Command example:

![Command Example](https://raw.githubusercontent.com/Silletr/LazyDevHelper/main/images/command_example.png)

Example output:

![Installation Output](https://raw.githubusercontent.com/Silletr/LazyDevHelper/main/images/output_example.png)

## Status

Status as of July 1st, 2025:
🎉 Plugin released successfully!
If you spot bugs or have ideas for improvements, feel free to open an issue or PR.


