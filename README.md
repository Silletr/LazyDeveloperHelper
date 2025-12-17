<h1 align="center">💫 Lazy Developer Helper</h1>

<p align="center">
  Automation tools for lazy developers.<br/>
  <i>Less routine, more coding!</i>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Silletr/LazyDeveloperHelper" />
  <img src="https://img.shields.io/github/license/Silletr/LazyDeveloperHelper" />
  <img src="https://img.shields.io/github/last-commit/Silletr/LazyDeveloperHelper" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Lua-2C2D72?style=flat&logo=lua&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
</p>

---
## Contents
<!-- toc -->
- [Video example](#video-example)
- [Status](#status)
- [Introduction](#introduction)
- [Features](#features)
- [Future Features](#future-features)
- [Roadmap](#roadmap)
- [Install using Packer](#install-using-packer)
- [Install using Lazy](#install-using-Lazy)
- [Avaible in](#available-in)
- [Usage](#usage)
- [Plugin History](#plugin-history)
<!-- tocstop -->

## Video example
![Video example of commands](https://github.com/Silletr/LazyDeveloperHelper/blob/e12147f98c4cd1bd884c3bdc22cbbf7fec6ec25d/images/examples/example.gif)
## Status
Want to see status of plugin at any day? [Thats file for u](STATUS.md)


## Introduction
Have you ever found yourself adding multiple dependencies to your code before installing them? Do you hate switching between your editor and terminal for installing libs? 🤔

LazyDevHelper solves this problem! It's a Neovim plugin that lets you manage Python dependencies directly from your editor, eliminating the need to switch to the terminal.
And plugin have Discord channel [from now](https://discord.gg/QnthFV3Zgp)


## Features
1. - ✨ Install Python, Lua, Javascript, Ruby, Rust packages directly from Neovim,
2. - ✨ Manage dependencies without leaving your editor,
3. - ✨ Compatible with modern Neovim configurations

## Future Features
(As of 20.10.25 8:14 PM its list clear, i`ll do just small fixes, maybe)

- [x] (1:01, 21.10.2024) - will be added installing libs right from requirements.txt for python, or from Cargo.toml ([Dependencies] block on corresponding file) <- Completed in 21.10.2025 15:00

## Roadmap
Check my [TODO.md](./TODO.md) for upcoming features! Want to help? - contributions are welcome.
## Available in
- [vim.org](https://www.vim.org/scripts/script.php?script_id=6156)
- [dotfyle.com](https://dotfyle.com/plugins/Silletr/LazyDevHelper)
- [Awesome-NeoVim](https://github.com/rockerBOO/awesome-neovim?tab=readme-ov-file#dependency-management)
- [Neovim Craft](https://neovimcraft.com/plugin/Silletr/LazyDeveloperHelper)
- Store.nvim (from recently)


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
Then: `:PackerSync`

## Install using Lazy
```lua
return {
    "Silletr/LazyDeveloperHelper",
    config = function ()
        require("LazyDeveloperHelper").setup()
    end
  }
```
Then: `:Lazy sync`



## Usage
Command example:
![Command example](https://github.com/Silletr/LazyDeveloperHelper/blob/ee3d4c47e690170a6ca3c28e523bdb035909ea6a/images/examples/command_example.png)
---
Example output:
![Installation Output](https://github.com/Silletr/LazyDeveloperHelper/blob/d129a416c1f6a1273fdc077dff73bbd948757d6c/images/examples/output_example.png)


![Alt](https://repobeats.axiom.co/api/embed/91c0a59ebb003b31f4184cc769db134500a0fde8.svg "Repobeats analytics image")

## Plugin History
![If you want to know more - read the plugin history!](./PLUGIN_HISTORY.md)
