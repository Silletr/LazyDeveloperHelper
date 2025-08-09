1. Add auto-detecting of file-type (.lua, .py, etc.)
    - [x] Check it from vim.bo.filetype
    - [x] Save to "file_type" variable
    - [x] If filetype is python = call plugin/pip_install.py, or if lua - call luarocks upload {package_name}
2. Replace `prints` to vim.notify for better UI and just visual enjoyment 
3. Add supporting:
    - [x] Lua (`luarocks install ...`)
    - [x] Rust (`cargo add ...`)
    - [x] Node.js (`npm install ...`)
    - [ ] C/C++ (`conan`, `vckpg`, `cmake`, fallback: `make`)
