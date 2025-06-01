# Git Operations Lab Report

## Cover Page
- **GitHub Profile Name**: [Your GitHub Username]
- **Repository Name**: [Your Repository Name]

## Lab Steps Documentation

### Step 1: Creating a New Folder with Text File
1. Created a new folder named "lab1"
2. Created a text file named "sample.txt" inside the folder

### Step 2: Creating a Public Git Repository
1. Logged into GitHub account
2. Created a new public repository
3. Repository was initialized with a README.md file

### Step 3: Pushing to Repository using SSH
1. Generated SSH key pair (if not already present)
2. Added SSH public key to GitHub account
3. Initialized local git repository
4. Added remote origin using SSH URL
5. Pushed initial commit to main branch

### Step 4: Creating Multiple Branches
Created the following branches:
1. `develop` - Development branch
2. `feature` - Feature development branch
3. `bugfix` - Bug fixing branch

Commands used:
```bash
git branch develop
git branch feature
git branch bugfix
```

### Step 5: Creating Pull Requests
Created two pull requests:
1. From `feature` to `develop` branch
2. From `develop` to `main` branch

### Step 6: Merging Branches
Successfully merged:
1. `feature` branch into `develop`
2. `develop` branch into `main`

## Verification
All operations were completed successfully, and the repository now contains:
- Multiple branches (`main`, `develop`, `feature`, `bugfix`)
- Merged pull requests
- Initial project files

## Notes
- All Git operations were performed using SSH for secure authentication
- Branch protection rules were followed during merges
- Pull requests were used for code review and proper documentation

---
*Note: Please replace [Your GitHub Username] and [Your Repository Name] with your actual GitHub username and repository name.* 