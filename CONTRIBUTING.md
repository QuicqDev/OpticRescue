# Contributing to this repository

## Getting Started

Before you begin:          
- Please go through the following links to understand the branch and commit naming conventions 
- [Branch Naming Conventions](https://stackoverflow.com/a/6065944/7454706)
- [Commit Naming Conventions](https://dev.to/i5han3/git-commit-message-convention-that-you-can-follow-1709)

# Branch Naming Conventions

**Branch naming conventions**

 1. Use grouping tokens (words) at the beginning of your branch names.
 2. Define and use short lead tokens to differentiate branches in a way that is meaningful to your workflow.
 2. Use slashes to separate parts of your branch names.
 3. Do not use bare numbers as leading parts.
 5. Avoid long descriptive names for long-lived branches.



**Group tokens**

Use "grouping" tokens in front of your branch names. 

    group1/foo
    group2/foo
    group1/bar
    group2/bar
    group3/bar
    group1/baz

The groups can be named whatever you like to match your workflow. 


**Short well-defined tokens**

Choose short tokens, so they do not add too much noise to every one of your branch names:

    wip       Works in progress; stuff I know won't be finished soon
    feat      Feature I'm adding or expanding
    bug       Bug fix or experiment
    junk      Throwaway branch created to experiment
    docs     Requirements or contributing guidelines
    build     Anything that affects build of project

**Do not use bare numbers**

Do not use bare numbers (or hex numbers) as part of your branch naming scheme. Inside tab-expansion of a reference name, git may decide that a number is part of a sha-1 instead of a branch name.  

    $ git checkout CR15032<TAB>
    Menu:   fix/CR15032    test/CR15032

**Avoid long descriptive names**

Long branch names can be very helpful when you are looking at a list of branches.  But it can get in the way when looking at decorated one-line logs as the branch names can eat up most of the single line and abbreviate the visible part of the log.

On the other hand long branch names can be more helpful in "merge commits".


# Commit naming conventions

A typical git commit message will look like :      
`<type>(<scope>): <subject>`

#### "type" must be one of the following mentioned below!
- `build`: Build related changes (eg: npm related/ adding external dependencies)
- `chore`: A code change that external user won't see (eg: change to .gitignore file or .prettierrc file)
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation related changes
- `refactor`: A code that neither fix bug nor adds a feature. (eg: You can use this when there is semantic changes like renaming a variable/ function name)
- `perf`: A code that improves performance
- `style`: A code that is related to styling
- `test`: Adding new test or making changes to existing test

#### "scope" is optional         
Scope must be noun and it represents the section of the section of the codebase

#### "subject"
use imperative, present tense (eg: use "add" instead of "added" or "adds")
don't use dot(.) at end
don't capitalize first letter

## Thank you and credits
Thank you for contributing. Lets help the community.
The commit and branch conventions are taken from the below resources please visit them.
- [Branch Naming Conventions](https://stackoverflow.com/a/6065944/7454706)
- [Commit Naming Conventions](https://dev.to/i5han3/git-commit-message-convention-that-you-can-follow-1709)