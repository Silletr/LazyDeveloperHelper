"""
EXMAPLE OF OUTPUT:
    🗂️ Commit category:
1. DELETED FILE/DIR
2. CHANGED FILE/DIR
3. BUGFIX IN FILE/DIR
4. HOTFIX
5. NEW FILE/DIR
> 2

❓ Files/dirs changed (comma separated):
    python/cargo_install.py, .deepsource.toml

📜 Short description:
    Optimized script speed, added some files to ignores
"""

import subprocess
import shutil


# --- class for auto-commit generation
class CommitGen:
    def __init__(self) -> None:
        self.msg = ""
        self.categories = {
            1: "DELETED FILE/DIR",
            2: "CHANGED FILE/DIR",
            3: "BUGFIX IN FILE/DIR",
            4: "HOTFIX",
            5: "NEW FILE/DIR",
        }

    def get_category(self) -> str:
        print("\n🗂️ Commit category:")
        for num, name in self.categories.items():
            print(f"{num}. {name}")

        while True:
            try:
                choice = int(input("> "))
                if choice in self.categories:
                    return self.categories[choice]
                else:
                    print("❌ Invalid choice, try again.")
            except ValueError:
                print("❌ Enter a number, not text.")

    def run(self):
        category = self.get_category()
        file_dirs = input("\n❓ Files/dirs changed (comma separated):\n")
        desc = input("\n📜 Description:\n")
        msg = f"[{category}: {file_dirs}] {desc}"
        print(f"\n✅ Commit message:\n{msg}")
        git_path = shutil.which("git")
        if not git_path:
            print("Git not defined in PATH!")
            return

        subprocess.run([git_path, "add", "."])
        subprocess.run([git_path, "commit", "-m", msg])


if __name__ == "__main__":
    CommitGen().run()
