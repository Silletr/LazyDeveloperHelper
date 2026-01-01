import subprocess


def last_tag():
    subprocess.run(["git", "fetch", "--tags"], check=True)
    result = subprocess.run(
        ["git", "describe", "--tags", "--abbrev=0"],
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def generate_changelog():
    to_tag = "HEAD"
    try:
        from_tag = last_tag()
    except subprocess.CalledProcessError:
        from_tag = None

    cmd = ["git", "log", "--pretty=format:%h %s"]
    if from_tag:
        cmd.append(f"{from_tag}..{to_tag}")

    try:
        result = subprocess.run(cmd, text=True, capture_output=True, check=True)

        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")


if __name__ == "__main__":
    generate_changelog()
