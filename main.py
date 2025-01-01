import os
import datetime

# Set up the repository
repo_name = "daily-contributions"
os.system(f"mkdir {repo_name}")
os.chdir(repo_name)
os.system("git init")

# Create a file to commit
file_name = "contribution.txt"
with open(file_name, "w") as f:
    f.write("Daily contribution")

# Loop to make a commit for each of the 30 days
start_date = datetime.datetime.now() - datetime.timedelta(days=30)
for i in range(30):
    commit_date = start_date + datetime.timedelta(days=i)
    os.system(f"echo '{commit_date}' >> {file_name}")
    os.system("git add .")
    os.system(f'git commit --date="{commit_date.isoformat()}" -m "Daily contribution for {commit_date.date()}"')

# Push the changes to GitHub (replace with your repository URL)
os.system("git remote add origin https://github.com/TheVedantPatil/Pixel.git")
os.system("git branch -M main")
os.system("git push -u origin main")