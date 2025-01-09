import os
import subprocess
import logging
from datetime import datetime

# Logging configuration:
logging.basicConfig(
    filename='automation_log.txt', #Log file where logs will be stored
    level=logging.INFO, #Info level and above
    format='%(asctime)s - %(levelname)s - %(message)s', #format for logs entry
                    )

# Step 1: Pull the latest changes from the repository
def  ():
    logging.info("Pulling the latest changes...")
    result = subprocess.run(["git", "pull"], capture_output=True, text=True)
    if result.returncode == 0:
        logging.info(f"Success: {result.stdout}")
    else:
        logging.error(f"Error pulling changes: {result.stderr}")
        exit(1)

# Step 2: Modify the placeholder file
def update_file():
    logging.info("Updating the activity_log.txt file...")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("activity_log.txt", "a") as file:
            file.write(f"Update at {timestamp}\n")
        logging.info("File updated successfully.")
    except Exception as e:
        logging.error(f"Error updating file: {e}")
        exit(1)
        
# Step 3: Commit and push the changes back to the repository
def git_push():
    logging.info("Pushing changes to the repository...")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Automated update"], check=True)
    result = subprocess.run(["git", "push"], capture_output=True, text=True)
    if result.returncode == 0:
        logging.info(f"Success: {result.stdout}")
    else:
        logging.error(f"Error pushing changes: {result.stderr}")
        exit(1)

# Main function to execute the steps
def main():
    git_pull()
    update_file()
    git_push()

if __name__ == "__main__":
    main()

