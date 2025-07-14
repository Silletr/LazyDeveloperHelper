1. Add auto-detecting of file-type (.lua, .py, etc.)  
    - [x] Check it from vim.bo.filetype  
    - [x] Save to "file_type" variable  
    - [x] If filetype is python = call plugin/pip_install.py, or if lua - call luarocks upload {package_name}
2. Add supporting: 
    - [ ] Rust (`cargo add ...`)
    - [ ] Node.js (`npm install ...`)
    - [ ] C/C++ (`conan`, `vckpg`, `cmake`, fallback: `make`)
