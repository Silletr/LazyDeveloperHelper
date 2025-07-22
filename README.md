# Lazy Developer Helper [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Lua](https://img.shields.io/badge/Lua-5.4.8-purple.svg?logo=lua&logoColor=white)](https://www.lua.org/)
[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://www.python.org)
[![Stars](https://img.shields.io/github/stars/Silletr/LazyDevHelper?style=round-square&color=yellow)](https://github.com/Silletr/LazyDevHelper/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=round-square)](https://github.com/Silletr/LazyDevHelper/pulls)

## Contents
<!-- toc -->
- [Video example](#video-example)
- [Introduction](#introduction)
- [Features](#features)
- [Future Features](#future-features)
- [Roadmap](#roadmap)
- [Install using Packer](#install-using-packer)
- [Avaible in](#available-in)
- [Usage](#usage)
- [Status](#status)
<!-- tocstop -->

## Video example
![Video example of commands](images/example.gif)
## Introduction

Have you ever found yourself adding multiple dependencies to your code before installing them? Do you hate switching between your editor and terminal? 🤔

LazyDevHelper solves this problem! It's a Neovim plugin that lets you manage Python dependencies directly from your editor, eliminating the need to switch to the terminal.
And plugin have Discord channel [from now](https://discord.gg/QnthFV3Zgp)

## Features

✨ Install Python packages directly from Neovim.
✨ Manage dependencies without leaving your editor.
✨ Compatible with modern Neovim configurations.

## Future Features
- [x] Will be added supporting Rust-, Lua- library manager.
- [ ] Code will be optimized better.


## Roadmap
Check my [TODO.md](./TODO.md) for upcoming features! Want to help? - contributions are welcome.


## Available in
- [vim.org](https://www.vim.org/scripts/script.php?script_id=6156)
- [dotfyle.com](https://dotfyle.com/plugins/Silletr/LazyDevHelper)
- [Awesome-NeoVim](https://github.com/rockerBOO/awesome-neovim?tab=readme-ov-file#utility)
- Soon will be in neovimcraft.

### Installation Methods
## Install using Packer
```lua
  use {
    'Silletr/LazyDevHelper',
    config = function()
      require("LazyDeveloperHelper")
    end
  }
```
## Usage
Command example:
![Command Example](https://raw.githubusercontent.com/Silletr/LazyDevHelper/main/images/command_example.png)

Example output:
![Installation Output](https://raw.githubusercontent.com/Silletr/LazyDevHelper/main/images/output_example.png)

## Status
Want to see status of plugin at any day? [Thats file for u](STATUS.md)
