#!/usr/bin/env python3

print(">>> pip_install started <<<")

import subprocess
import sys

libs_list = set() 

def install_lib(lib_name: str):
    print(f"📦 Installing {lib_name} ...\n")
    global libs_list
    with open("requirements.txt", "a+") as file:
        # read lines of requirements file
        all_libs = file.readlines()
        libs_list = set(line.strip() for line in all_libs)
        # Add library if it doesnt exists
        if lib_name not in libs_list:
            libs_list.add(lib_name)
            file.write(f"{lib_name}\n")


    try:
        global result
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", lib_name, "--break-system-packages"],
            check=True,
            text=True,
            capture_output=True, 
        )
        
       
        if "requirement already satisfied" in result.stdout.lower():
            print("\nInstallation Output:")
            print(result.stdout)
            print(f"✅ {lib_name} already installed")
        elif "successfully installed" in result.stdout.lower():
            print(f"✅ {lib_name} successfully installed")
           
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {lib_name}")
        print(e.output)


def main():
    if len(sys.argv) < 2:
        print("Provide at least one lib")
        return

    for lib in sys.argv[1:]:
        install_lib(lib)


if __name__ == "__main__":
    main()
