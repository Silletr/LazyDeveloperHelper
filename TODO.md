1. Add auto-detecting of file-type (.lua, .py, etc.)
    1.1 - Check it from vim.bo.filetype
    1.2 - Save to "file_type" variable
    1.3 - If filetype is python = call plugin/pip_install.py, or if lua - call luarocks upload {package_name}
