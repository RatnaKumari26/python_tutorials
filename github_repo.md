# Git
- Git is a version control system, We can track our history and work together.
- They classified into two categories:- 
    - Centralized
    - Distributed
### Centralized 
- All team members connect to a server and work together but problem with centralized is if server goes down we cannot colaborate.
### Distributed
- All team members will get thier induvial server to work.
## Git commands
- git init= Turns any directory into a Git repository.
- git clone= The 'git clone' command is used to create a copy of a specific repository or branch within a repository.
- git add= The 'git add' command adds new or changed files in your working directory to the Git staging area.
- git commit= 'git commit' creates a commit, which is like a snapshot of your repository.
- git push= 'git push' uploads all local branch commits to the corresponding remote branch.
- git pull= 'git pull' updates your current local working branch, and all of the remote tracking branches.
### Staging files
- We use 'echo' commad to add text file into the folder.
- To track our file 'git status' through colors:
    - red= Not in staging area
    - green= Files are in staging area
### Commiting Changes
- git commit -m "message about file to commit"
- They are two seperate commits
    - Bug fix
    - Typo
### Skipping the staging area
- To skip the staging area use 'git commit -a(all)'-->modified files -m(message)
- 'git commit -am'= Fix the bug
### Removing files
- Use rm(file name)
- File will be deleted but,To remove it from staging area use 'git add(file name')
- Atlast commit it with a message like "file remove"
### Renaming or moving files
- Use mv(file name)
- It will be renamed we have to commit it.
### Ignoring files
- create a new files and add text files and know the status.
- Now add file .gitignore,next go to code .gitignore.
- Add gitignore and commit changes.
### Short status
- git status -s, the left column is a staging area and right column is working directory.
- If 'A' comes means added the file and 'M' means modified file.
### Viewing the staged and unstaged changes
- The exact lines code that we have staged. we use 'git diff --staged'.
### Viewing the history
- To check the history use 'git log'
- 'git log --online' this shows short summary of the commit, Also we know to the orderwise use 'git log --online --reverse'.
### Unstaging files
- To unstage file,know the status then use 'git restore --staged (file name).
