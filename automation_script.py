import os
import subprocess
from datetime import datetime

# Step 1: Pull the latest changes from the repository
def git_pull():
    print("Pulling the latest changes...")
    result = subprocess.run(["git", "pull"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error pulling changes: {result.stderr}")
        exit(1)

# Step 2: Modify the placeholder file
def update_file():
    print("Updating the activity_log.txt file...")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("activity_log.txt", "a") as file:
        file.write(f"Update at {timestamp}\n")
    print("File updated.")

# Step 3: Commit and push the changes back to the repository
def git_push():
    print("Pushing changes to the repository...")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Automated update"], check=True)
    result = subprocess.run(["git", "push"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error pushing changes: {result.stderr}")
        exit(1)

# Main function to execute the steps
def main():
    git_pull()
    update_file()
    git_push()

if __name__ == "__main__":
    main()

