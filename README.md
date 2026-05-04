# MATH1604-python-quiz-analysis

## Project Structure
- data/ -> raw downlaoded files
- output/ -> processed and collated results
- reviews/ -> individual Jupyter notebooks
- scripts/ -> all Python modules (M1-M4)


## Team Guidelines (Important)
Please read before starting your module.

### Function Requirements
- Follow the function names EXACTLY as shown in the assessment brief slides
- Do NOT rename functions or parameters
- Keep the same number of parameters

This is important so that M4 (full pipeline) can integrate everything smoothly.


### Module Responsibilities
- M1: Extract answer sequences (by Aziz)
- M2: Download and collate answer files (by Yu Xuan)
- M3: Generate statistics and visualisations (by Sarah)
- M4: Full pipeline integration (by Justin)


### Coding expectations
- Write clean, readable code
- Use functions (do not write everything in one script)
- Add simple comments explaining your logic
- Test your function works independently before integration


### Integration Rule 
Your function should work with:
- Inputs: exactly as defined in the slides
- Outputs: clean and usable for the next module


### Github Workflow
- Commit regularly with clear messages (try not to use default messages)
- Do not overwrite other people's code without permission
- Inform the Whatsapp group before making major changes


### Communication
If you are unsure about anything:
- Ask in the Whatsapp group
- Do not guess and change function definitions



## Setup Guide (VS Code + Git + Github Workflow)

### 1. Install Required Software
- [Download VS Code](https://code.visualstudio.com/)
- [Download Git](https://git-scm.com/downloads)


### 2. First-time Git Setup
Open terminal in VS Code and run:

git config --global user.name "Your Name"


git config --global user.email "yourgithubemail@example.com"


### 3. Clone the Repository 
1. Go to GitHub Repository
2. Click Code -> HTTPS -> Copy link
3. In VS Code:
- Press Ctrl + Shift + P
- Type: Git: Clone
- Paste the link -> select folder -> open project


### 4. Daily Workflow (IMPORTANT)
### Step 1 - Pull latest code
VS Code Source Control (left panel): press git pull


### Step 2 - Create new branch
Click bottom-left corner (branch name) → Create new branch

Example:
- m1-extraction
- m2-preparation
- m3-analysis
- m4-pipeline-update


### Step 3 - Code your part
Edit your assigned file in the scripts/ folder


### Step 4 - Save changes
Press: Ctrl + S


### Step 5 - Commit changes
Go to Source Control (left panel):
1. Click + (stage changes)
2. Write commit message (example):
- M1: Implement extraction logic
3. Click Commit


### Step 6 - Push branch
Click: Publish Branch or Sync Changes


### Step 7 - Create pull request 
1. Go to Github
2. Click "Compare & Pull Request"
3. Add title and description
4. Click "Create Pull Request"


### Step 8 - Merge pull request
Before merging, double confirm the changes with another group member.

Then click: Merge pull request -> Confirm merge


### Step 9 - Update local code
Back in VS Code: Git pull


### Rules
- Do NOT push directly into main 
- Do NOT skip git pull before
- Always create a new branch before coding
- Always use Pull requests


### Key concepts
- Push = upload your code to Github
- Pull = download latest code from Github
- Branch = your personal working version
- Pull request (PR) = request to merge your work into main


### Workflow Summary
pull -> branch -> code -> save -> commit -> push -> PR -> merge -> pull
