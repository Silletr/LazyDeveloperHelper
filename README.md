# Lazy Developer Helper [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Lua](https://img.shields.io/badge/Lua-5.4.8-purple.svg?logo=lua&logoColor=white)](https://www.lua.org/)
[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://www.python.org)
[![Stars](https://img.shields.io/github/stars/Silletr/LazyDevHelper?style=round-square&color=yellow)](https://github.com/Silletr/LazyDevHelper/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=round-square)](https://github.com/Silletr/LazyDevHelper/pulls)
[![DeepSource](https://app.deepsource.com/gh/Silletr/LazyDeveloperHelper.svg/?label=active+issues&show_trend=true&token=6IT7yrn6pB2MxD9vprh3y6eJ)](https://app.deepsource.com/gh/Silletr/LazyDeveloperHelper/)
---

## Contents
<!-- toc -->
- [Video example](#video-example)
- [Status](#status)
- [Introduction](#introduction)
- [Plugin History](#plugin-history)
- [Features](#features)
- [Future Features](#future-features)
- [Roadmap](#roadmap)
- [Install using Packer](#install-using-packer)
- [Install using Lazy](#install-using-Lazy)
- [Avaible in](#available-in)
- [Usage](#usage)
- [Telemetry](#telemetry)
<!-- tocstop -->

## Video example
![Video example of commands](https://github.com/Silletr/LazyDeveloperHelper/blob/b5d3f0fcdce9c30f2217a7e83246f1debcc23b81/images/examples/example.gif)

## Status
Want to see status of plugin at any day? [Thats file for u](STATUS.md)


## Introduction
Have you ever found yourself adding multiple dependencies to your code before installing them? Do you hate switching between your editor and terminal for installing libs? 🤔

LazyDevHelper solves this problem! It's a Neovim plugin that lets you manage Python dependencies directly from your editor, eliminating the need to switch to the terminal.
And plugin have Discord channel [from now](https://discord.gg/QnthFV3Zgp)


## Plugin History
# 📃 Hitory of plugin creation
It was a deep night, *2:40 AM*, un-sleep me, phone, Notes, and brain (maybe it exist for me), and i one moment through "What if I will write the plugin for Neovim that installing libs right from editor, and will add this libs to requirements file" (generally, i through add only the Python-pip3 packages, but.. you see what happend)
And, because of that idea - i fully (at all, fck it) knocked down my sleep-mode during 4 months, and only now i have +- good sleep mode, so i can say only two things -
1. Do not deep into your project too deep - **you will fuck your organism, and will life in Light sleep phase, instead of REM + Deep sleep**

2. `If u wanna think up some project from nothing` - **just try to do not anything 1-2 days in coding, and brain from lazzy state will think up project itself**


## Features
✨ Install Python packages directly from Neovim.  
✨ Manage dependencies without leaving your editor.  
✨ Compatible with modern Neovim configurations.  

## Future Features
(As of 20.10.25 8:14 PM its list clear, i`ll do just small fixes, maybe)

(1:01, 21.10.2024) - will be added installing libs right from requirements.txt for python, or from Cargo.toml ([Dependencies] block on corresponding file)


## Roadmap
Check my [TODO.md](./TODO.md) for upcoming features! Want to help? - contributions are welcome.


## Available in
- [vim.org](https://www.vim.org/scripts/script.php?script_id=6156)
- [dotfyle.com](https://dotfyle.com/plugins/Silletr/LazyDevHelper)
- [Awesome-NeoVim](https://github.com/rockerBOO/awesome-neovim?tab=readme-ov-file#utility)
- [Neovim Craft](https://neovimcraft.com/plugin/Silletr/LazyDevHelper/)


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
![Command Example](https://github.com/Silletr/LazyDeveloperHelper/blob/d129a416c1f6a1273fdc077dff73bbd948757d6c/images/examples/command_example.png)

Example output:
![Installation Output](https://github.com/Silletr/LazyDeveloperHelper/blob/d129a416c1f6a1273fdc077dff73bbd948757d6c/images/examples/output_example.png)


## Telemetry 
**📊 Anonymous Usage Stats (Optional)**

LazyDeveloperHelper can send anonymous usage stats - plugin version, OS type, Neovim version.
No personal data, usernames, or IPs are collected.

To disable telemetry:
```bash
:LazyDevHelpDisableTelemetry
```
