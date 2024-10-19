import subprocess
import sys

def check_dependency(dep):
    try:
        subprocess.check_call([sys.executable, "-m", dep, "--version"])
        print(f"✅ {dep} is installed")
    except subprocess.CalledProcessError:
        print(f"❌ {dep} is not installed")

if __name__ == "__main__":
    dependencies = input("🔍 Enter dependencies to check (comma-separated): ").split(",")
    for dep in dependencies:
        check_dependency(dep.strip())
