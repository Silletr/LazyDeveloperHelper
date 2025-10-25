#!/usr/bin/env python3

import subprocess
import sys
from typing import List
import shutil

# --- EXAMPLE OF OUTPUT:
# 🗂️ Commit category:
# 1. DELETED FILE/DIR
# 2. CHANGED FILE/DIR
# 3. BUGFIX IN FILE/DIR
# 4. HOTFIX
# 5. NEW FILE/DIR
# > 2
#
# ⚡ Changed files:
# M commit_generation.py
# A python/cargo_install.py
#
# ❓ Files/dirs changed (comma separated):
# python/cargo_install.py, .deepsource.toml
#
# 📜 Short description:
# Optimized script speed, added some files to ignores


# --- AUTO-GENERATION OF COMMITS
class CommitGen:
    def __init__(self) -> None:
        self.msg = ""
        self.git_path = str(shutil.which("git"))
        if not self.git_path:
            print("❌ Git not found in PATH!")
            sys.exit(1)
        self.categories = {
            1: "DELETED FILE/DIR",
            2: "CHANGED FILE/DIR",
            3: "BUGFIX IN FILE/DIR",
            4: "HOTFIX",
            5: "NEW FILE/DIR",
        }

    def get_category(self) -> list[str]:
        """Get multiple commit categories from user input."""
        print(
            "\n🗂️ Commit categories (enter numbers separated by commas or spaces, e.g., 2,5): "
        )
        for num, name in self.categories.items():
            print(f"{num}. {name}")
        while True:
            try:
                choices_input = input("> ").strip().replace(",", " ")
                if not choices_input:
                    print("❌ At least one category must be selected.")
                    continue
                choices = [int(x) for x in choices_input.split() if x]
                if all(choice in self.categories for choice in choices):
                    return [self.categories[choice] for choice in choices]
                print("❌ Invalid choice(s), select valid numbers.")
            except ValueError:
                print("❌ Enter numbers, not text.")

    def show_git_changes(self) -> None:
        """Show changed files."""
        try:
            result = subprocess.run(
                [str(self.git_path), "status", "--short"],
                text=True,
                capture_output=True,
            )
            lines = result.stdout.strip().split("\n")
            if not lines or lines == [""]:
                print("✅ No unstaged changes")
            else:
                print("⚡ Changed files:")
                for line in lines:
                    print("  " + line)
        except subprocess.CalledProcessError as e:
            print(f"❌ Git error:\n{e.stdout}\n{e.stderr}")
        except FileNotFoundError:
            print("❌ Git command not found!")
        except PermissionError:
            print("❌ Permission denied for git operations!")

    @staticmethod
    def get_changed_files() -> List[str]:
        """Get list of changed files/dirs from user input."""
        while True:
            files_input = input(
                """\n❓ Files/dirs changed
                                (comma separated):\n"""
            ).strip()
            if not files_input:
                print("❌ No files/dirs provided, try again.")
                continue
            files = [f.strip() for f in files_input.split(",") if f.strip()]
            if files:
                return files
            print("❌ Invalid input, provide at least one file/dir.")

    @staticmethod
    def get_description() -> str:
        """Get short description from user input."""
        while True:
            desc = input("\n📜 Description:\n").strip()
            if desc:
                return desc
            print("❌ Description cannot be empty, try again.")

    def run(self) -> None:
        """Generate and execute commit."""
        categories = self.get_category()
        self.show_git_changes()
        changed_files = ", ".join(self.get_changed_files())
        description = self.get_description()
        category_str = ", ".join(categories)
        self.msg = f"[{category_str}: {changed_files}] {description}"
        print(f"\n✅ Commit message:\n{self.msg}")
        try:
            subprocess.run([self.git_path, "add", "."], check=True)
            subprocess.run([self.git_path, "commit", "-m", self.msg], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Git error:\n{e.stdout}\n{e.stderr}")
            return
        push_question = (
            input(
                """\nYou want to push it on
                  current branch? (Yes/No): """
            )
            .lower()
            .strip()
        )
        if push_question in ("y", "yes"):
            try:
                subprocess.run([self.git_path, "push"], check=True)
                print("✅ Push successful!")
            except subprocess.CalledProcessError as e:
                print(f"❌ Push failed: {e.stderr}")


if __name__ == "__main__":
    CommitGen().run()
