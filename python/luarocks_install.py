#!/usr/bin/env python3

import subprocess
import sys

print("<< LuaRocks installer started >>\n")

# luarocks upload {lib_name}
def install_lib(lib_name):
    result = subprocess.run("luarocks", "install", lib_name,
            check=True,
            text=True,
            capture_output=True, 
            )
