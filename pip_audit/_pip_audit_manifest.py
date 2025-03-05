#!/usr/bin/env python
import sys
import subprocess
import os

def main(files):
    for file in files:
        if file.endswith("requirements.txt"):
            print(f"Auditing requirements file: {file}")
            subprocess.run(["pip-audit", "-r", file], check=True)
        elif file.endswith("pyproject.toml"):
            project_dir = os.path.dirname(file)
            print(f"Auditing project in directory: {project_dir}")
            subprocess.run(["pip-audit", project_dir], check=True)
        else:
            print(f"Skipping unsupported file: {file}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
