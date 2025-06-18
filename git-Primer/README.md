# Git Primer

### Due Week 3 Lab Time

This is an individual exercise.

## Background

This course requires the use of Github as source control for your project. Every project **must** use Github and you will be graded throughout the term on your use of Git and Github. Consequently, you are required to complete this exercise to ensure you understand how to

(1) Use Git to clone, pull, push, commit, checkout
(2) Use Github to submit a pull request

This exercise is worth 2% of your course grade.

## Running the application

```
repository/
├── main.py
├── templates/
│   ├── index.html
│   └── calculator.html
```

To run this application use `python3 main.py`. You will need to first install `Python` which can be done online at https://www.python.org/downloads/ and you will need to install any necessary dependencies such as Flask using `pip install Flask` on the commandline after installing Python. **You are not required to actually run the application** when you show your tutor. You will simply need to show your tutor your Github commit history and open pull request.

## Exercises

There are some bugs in this code and features we need to add. To make sure you have correctly installed Flask and cloned this repo, when you run the application and open the link in your browser (http://127.0.0.1:5000/) you should see a welcome page that says "Welcome to COMP3900".

Setting up the repo
* You will be cloning my repo but working on your own. To do this, you must first setup your own personal Github account and create a **PRIVATE** repo called `comp3900_git_primer`. Please **do not fork this repo**.
* Next, clone this repo (the one we are currently in NOT your private one) and then `cd git-Primer` to go into the repo.
* We are going to transfer this to your Github repo. To do this, use the command `git remote set-url origin git@github.com:GITHUB_USERNAME/REPO_NAME.git` replacing `GITHUB_USERNAME` and `REPO_NAME` with the ones for the repo you created.
* Now run `git push` and you can get started with the exercise.

1. We need to make a small modification as this page should include COMP9900 as well. Add COMP9900 to the greeting message in a new branch. To create a new branch and switch to it you can use `git checkout -b welcome_message_renaming`. Then make the necessary changes and add them using `git add <filename>` and commit them with a meaningful commit message using `git commit -m <write your commit message here>`.
2. You will need to show your tutor you made this change so **DO NOT merge this branch into `main` or delete it.** However, you should push it to the remote branch using `git push`.
3. We are going to create a new branch based off the one we are currently on to fix some other issues. Use `git checkout -b welcome_and_calculator_fix` to switch to a new branch where we will debug the calculator. If you try using the calculator right now, you will see that it does not add the numbers but instead multiplies them.
4. Fix this issue and then commit your change to git. This time, we want to merge a branch called `incorrect_branch_name` into this branch (`welcome_and_calculator_fix`) using `git merge origin/incorrect_branch_name --allow-unrelated-histories`. However, when you try to merge it in, you will encounter a merge conflict as there are already changes in the other branch. Remove the other branch's changes and replace them with your fix to the COMP[39]900 welcome message.
5. You also notice your teammate has merged a .env file containing your secret `API key`, gross! Remove the problematic file from the staging area with `git rm --cached .env` and create a .gitignore file to exclude .env files! Add the newly created file with `git add .gitignore`, then commit and merge this change with a meaningful [conventional commit](https://www.conventionalcommits.org/en/v1.0.0-beta.2/) message.
7. Once the code has been merged, push it to Github (the remote version of your branch) using `git push`. If it tells you your branch does not have a remote version, then use the suggested command it gives you.
8. Now, on Github it will give you a message saying there were recent changes to a branch and ask you if you want to submit a pull request. Create the pull request but **DO NOT** accept it. You will need to show your tutor the unapproved pull request.
