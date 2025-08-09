#!/usr/bin/env python3

import sys
import os
from subprocess import run
from subprocess import CalledProcessError

def find_cargo_toml(start_dir='.'):
    """Search for Cargo.toml starting from specified directory"""
    # Check current directory first
    cargo_path = os.path.join(start_dir, 'Cargo.toml')
    if os.path.exists(cargo_path):
        return cargo_path
    
    # If not found, search parent directories
    current_dir = os.path.abspath(start_dir)
    while True:
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # Reached root
            break
        
        cargo_path = os.path.join(parent_dir, 'Cargo.toml')
        if os.path.exists(cargo_path):
            return cargo_path
            
        current_dir = parent_dir
    
    return None

def cargo_install(lib_name):
    # Find Cargo.toml
    cargo_path = find_cargo_toml()
    if not cargo_path:
        print("❌ Cargo.toml not found in current or parent directories.")
        return

    # Get absolute paths for better error reporting
    abs_cargo_path = os.path.abspath(cargo_path)
    current_dir = os.getcwd()
    
    print(f"📁 Found Cargo.toml at: {abs_cargo_path}")
    print(f"📍 Current directory: {current_dir}")

    # Change to Cargo.toml's directory temporarily
    original_dir = os.getcwd()
    try:
        os.chdir(os.path.dirname(abs_cargo_path))
        
        # Install the dependency
        print(f"🔧 Running cargo add {lib_name} ...")
        try:
            result = run(
                ["cargo", "add", lib_name],
                check=True,
                capture_output=True,
                text=True,
            )
            print("📦 Cargo output:\n", result.stdout)

        except CalledProcessError as e:
            print(f"❌ Failed to install {lib_name}")
            print("🔻 stdout:\n", e.stdout)
            print("🔻 stderr:\n", e.stderr)
            print("🔚 Return code:", e.returncode)

    finally:
        os.chdir(original_dir)  # Restore original directory

def main():
    if len(sys.argv) < 2:
        print("Provide at least one Rust package name")
        return

    for lib in sys.argv[1:]:
        cargo_install(lib)

if __name__ == "__main__":
    main()
