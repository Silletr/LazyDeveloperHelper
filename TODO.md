1. Add auto-detecting of file-type (.lua, .py, etc.)
    - [x] Check it from vim.bo.filetype
    - [x] Save to "file_type" variable
    - [x] If filetype is python = call plugin/pip_install.py, or if lua - call `luarocks install {package_name}`
2. [x] Replace `prints` to vim.notify for better UI and just visual enjoyment
---
3. Add supporting:
    - [x] Lua (`luarocks install ...`)
    - [x] **Rust** (`cargo add ...`)
    - [x] *Node.js* (`npm install ...`)
---
4. - [x] **Optimize code**
---
New point (20.10.2025, 10:47):
    1. - [ ] **Create a option for installing requirements from files (Applyable for Cargo, Python)** by adding `-r`in `SuggestImports` command (Will be renamed to InstallLibs), end result - `SuggestImports -r` (or `InstallLibs -r`)
    2. - [ ] ** **
