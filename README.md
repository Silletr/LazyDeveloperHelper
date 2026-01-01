<h1 align="center">💫 Lazy Developer Helper</h1>

<p align="center">
  Automation tools for lazy developers.<br/>
  <i>Less routine, more coding!</i>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Silletr/LazyDeveloperHelper" alt="Stars" />
  <img src="https://img.shields.io/github/license/Silletr/LazyDeveloperHelper" alt="License" />
  <img src="https://img.shields.io/github/last-commit/Silletr/LazyDeveloperHelper" alt="Last Commit" />
</p>

<p align="center">
  <strong>Supported Languages:</strong><br/>
  <img src="https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white" alt="Lua" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white" alt="Rust" />
  <img src="https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white" alt="Ruby" />
  <img src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black" alt="C" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++" />
</p>

<p align="center">
  <strong>Supported Package Managers:</strong><br/>
  <img src="https://img.shields.io/badge/pip-3776AB?style=for-the-badge&logo=pypi&logoColor=white" alt="pip" />
  <img src="https://img.shields.io/badge/Cargo-DEA584?style=for-the-badge&logo=rust&logoColor=black" alt="Cargo" />
  <img src="https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white" alt="npm" />
  <img src="https://img.shields.io/badge/Gem-990000?style=for-the-badge&logo=rubygems&logoColor=white" alt="RubyGems" /> <!-- Ruby Gem -->
  <img src="https://img.shields.io/badge/Conan-66C2A5?style=for-the-badge&logo=conan&logoColor=white" alt="Conan" />
  <img src="https://img.shields.io/badge/NuGet-512BD4?style=for-the-badge&logo=nuget&logoColor=white" alt="NuGet" />
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
If you wanna to see roadmap for 2026 and current year (2025, if you forget) - this for you:
[Go to Roadmap.sh](https://roadmap.sh/r/lazydeveloperhelper-roadmap-for-2026-year)


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
