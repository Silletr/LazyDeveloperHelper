# Lazy Developer Helper [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Lua](https://img.shields.io/badge/Lua-5.4.8-purple.svg?logo=lua&logoColor=white)](https://www.lua.org/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org)
[![Stars](https://img.shields.io/github/stars/Silletr/LazyDevHelper?style=flat-square&color=yellow)](https://github.com/Silletr/LazyDevHelper/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Silletr/LazyDevHelper/pulls)

## Table of Contents
<!-- toc -->
  - [Introduction](#introduction)
  - [Errors](#errors)
  - [Installation Requirements](#installation-requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Status](#status)
  - [License](#license)
<!-- tocstop -->

## Introduction

Have you ever found yourself adding multiple dependencies to your code before installing them? Do you hate switching between your editor and terminal? 🤔

LazyDevHelper solves this problem! It's a Neovim plugin that lets you manage Python dependencies directly from your editor, eliminating the need to switch to the terminal.

## Features

✨ Install Python packages directly from Neovim
✨ Manage dependencies without leaving your editor
✨ Compatible with modern Neovim configurations

### Using Packer

Add this to your Packer configuration:

```lua
use {
- With Packer:
  ```lua
  use {
    'Silletr/LazyDevHelper',
    config = function()
        require('LazyDevHelper.plugin.commands').commands()
    end
}
```

## Usage

Install packages using the command palette:
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
# License
MIT License

Copyright (c) 2025 Silletr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
