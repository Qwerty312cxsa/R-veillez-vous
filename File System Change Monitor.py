import os
import time

def monitor_directory(path):
    before = dict ([(f, None) for f in os.listdir (path)])
    while True:
        time.sleep(2)
        after = dict ([(f, None) for f in os.listdir (path)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added:
            print(f"📂 Added: {', '.join(added)}")
        if removed:
            print(f"🗑️ Removed: {', '.join(removed)}")
        before = after

if __name__ == "__main__":
    directory = input("📁 Enter directory to monitor: ")
    monitor_directory(directory)
