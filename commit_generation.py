#!/usr/bin/env python3

import subprocess
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
#   M  commit_generation.py
#   A  python/cargo_install.py
#
# ❓ Files/dirs changed (comma separated):
#     python/cargo_install.py, .deepsource.toml
#
# 📜 Short description:
#     Optimized script speed, added some files to ignores


# --- AUTO-GENERATION OF COMMITS
class CommitGen:
    def __init__(self) -> None:
        self.msg = ""
        self.git_path = shutil.which("git")
        if not self.git_path:
            print("❌ Git not found in PATH!")
            exit(1)

        self.categories = {
            1: "DELETED FILE/DIR",
            2: "CHANGED FILE/DIR",
            3: "BUGFIX IN FILE/DIR",
            4: "HOTFIX",
            5: "NEW FILE/DIR",
        }

    def get_category(self) -> str:
        """Get commit category from user input."""
        print("\n🗂️ Commit category:")
        for num, name in self.categories.items():
            print(f"{num}. {name}")

        while True:
            try:
                choice = int(input("> "))
                if choice in self.categories:
                    return self.categories[choice]
                print("❌ Invalid choice, try again.")
            except ValueError:
                print("❌ Enter a number, not text.")

    def show_git_changes(self) -> None:
        """Show changed files like git diff --name-status."""
        try:
            result = subprocess.run(
                [self.git_path, "diff", "--name-status"],
                text=True,
                capture_output=True,
                check=True,
            )
            lines = result.stdout.strip().split("\n")
            if not lines or lines == [""]:
                print("✅ No unstaged changes")
            else:
                print("⚡ Changed files:")
                for line in lines:
                    print("  " + line)
        except subprocess.CalledProcessError as e:
            print(f"❌ Git error: {e.stderr.decode() if e.stderr else 'Unknown error'}")

    def get_changed_files(self) -> list[str]:
        """Get list of changed files/dirs from user input."""
        while True:
            files_input = input("\n❓ Files/dirs changed (comma separated):\n").strip()
            if not files_input:
                print("❌ No files/dirs provided, try again.")
                continue
            files = [f.strip() for f in files_input.split(",") if f.strip()]
            if files:
                return files
            print("❌ Invalid input, provide at least one file/dir.")

    def get_description(self) -> str:
        """Get short description from user input."""
        while True:
            desc = input("\n📜 Description:\n").strip()
            if desc:
                return desc
            print("❌ Description cannot be empty, try again.")

    def run(self) -> None:
        """Generate and execute commit."""
        category = self.get_category()
        self.show_git_changes()
        changed_files = ", ".join(self.get_changed_files())
        description = self.get_description()
        self.msg = f"[{category}: {changed_files}] {description}"
        print(f"\n✅ Commit message:\n{self.msg}")

        try:
            subprocess.run([self.git_path, "add", "."], check=True)
            subprocess.run([self.git_path, "commit", "-m", self.msg], check=True)
        except subprocess.CalledProcessError as e:
            print(
                f"❌ Commit failed: {e.stderr.decode() if e.stderr else 'Unknown error'}"
            )

        push_question = (
            input("\nYou want to push it on current branch? (Yes/No): ").lower().strip()
        )
        if push_question in ("y", "yes"):
            try:
                subprocess.run([self.git_path, "push"], check=True)
                print("✅ Push successful!")
            except subprocess.CalledProcessError as e:
                print(
                    f"❌ Push failed: {e.stderr.decode() if e.stderr else 'Unknown error'}"
                )


if __name__ == "__main__":
    CommitGen().run()
