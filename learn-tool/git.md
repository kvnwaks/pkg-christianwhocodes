# Git Reference Notes

A comprehensive reference covering the most important Git commands, flags, and concepts.

---

## Table of Contents
1. [git init](#git-init)
2. [git branch](#git-branch)
3. [git switch](#git-switch)
4. [git remote](#git-remote)
5. [git add](#git-add)
6. [git commit](#git-commit)
7. [git reset](#git-reset)
8. [git push](#git-push)
9. [git pull](#git-pull)
10. [git fetch](#git-fetch)
11. [git merge](#git-merge)
12. [git rebase](#git-rebase)
13. [git clone](#git-clone)
14. [git tag](#git-tag)
15. [git prune](#git-prune)
16. [git config](#git-config)
17. [Key Concepts](#key-concepts)

## The Three-Stage Pipeline

The most important mental model in Git. Every change flows through three stages:

```
Working Directory  →  Staging Area (Index)  →  Repository (History)
   (your files)          (git add)               (git commit)
```

- **Working Directory** — where you edit files normally
- **Staging Area** — a holding area where you assemble exactly what goes into the next commit
- **Repository** — the permanent history of snapshots (commits)

---

## 1. `git init`

Initializes a new Git repository in the current directory by creating a hidden `.git` folder.

| Flag / Usage | What it does |
|---|---|
| `git init` | Creates a `.git` folder, turning the current directory into a repo |
| `git init <folder>` | Creates a new repo inside a named folder (creates it if it doesn't exist) |
| `--bare` | Creates a bare repo (no working directory) — used for remote/server repos |
| `-b <name>` / `--initial-branch` | Sets the name of the initial branch instead of the default `master` |
| `-q` / `--quiet` | Suppresses output messages |


```bash
# Initialize a repo in the current directory
git init

# Initialize with 'main' as the default branch name
git init -b main

# Initialize a new named project folder
git init my-project
```

---
## 2. `git branch`

Lists, creates, renames, or deletes branches. A branch is just a moveable pointer to a commit.

| Flag / Usage | What it does |
|---|---|
| `git branch` | Lists all local branches (`*` marks the current one) |
| `git branch <name>` | Creates a new branch at the current commit (does not switch to it) |
| `-a` / `--all` | Lists both local and remote-tracking branches |
| `-r` / `--remotes` | Lists only remote-tracking branches |
| `-d <name>` | Deletes a branch safely (only if fully merged) |
| `-D <name>` | Force-deletes a branch even with unmerged changes |
| `-m <old> <new>` | Renames a branch |
| `-v` | Shows the last commit on each branch |
| `--merged` / `--no-merged` | Filters branches by merge status into the current branch |

> **Tip:** A branch is considered "merged" when all its commits are reachable from the target branch. After merging, it's safe to delete with `-d`. If not merged, deletion requires force: `-D`.


```bash
# List all local branches
git branch

# Create a new branch (stay on current branch)
git branch feature/login

# List local + remote branches
git branch -a

# Delete a merged branch
git branch -d feature/login

# Rename a branch
git branch -m old-name new-name
```

---
## 3. `git switch`

Switches to a different branch. The modern replacement for `git checkout <branch>`.

| Flag / Usage | What it does |
|---|---|
| `git switch <branch>` | Switches to an existing branch |
| `-c <name>` / `--create` | Creates a new branch and switches to it immediately |
| `-C <name>` | Creates the branch (or resets it if it exists), then switches |
| `--detach` | Switches to a commit in detached HEAD mode — for inspecting old commits |
| `-` | Switches back to the previous branch (like `cd -` in a terminal) |
| `--orphan <name>` | Creates a new branch with no commit history |


```bash
# Switch to an existing branch
git switch main

# Create and switch to a new branch in one step
git switch -c feature/signup

# Switch back to the previous branch
git switch -
```

---
## 4. `git remote`

Manages connections to remote repositories (e.g. GitHub, GitLab).

| Flag / Usage | What it does |
|---|---|
| `git remote` | Lists the names of all configured remotes |
| `-v` / `--verbose` | Lists remotes with their full fetch and push URLs |
| `show <name>` | Shows detailed info about a remote |
| `add <name> <url>` | Adds a new remote |
| `remove <name>` | Removes a remote |
| `rename <old> <new>` | Renames a remote |
| `set-url <name> <url>` | Changes the URL of an existing remote |


```bash
# See all remotes and their URLs
git remote -v

# Add a remote called 'origin'
git remote add origin https://github.com/user/repo.git

# Change a remote's URL
git remote set-url origin https://github.com/user/new-repo.git

# Remove a remote
git remote remove origin
```

---
## 5. `git add`

Stages changes — moves files into the staging area, ready for a commit.

| Flag / Usage | What it does |
|---|---|
| `git add <file>` | Stages a specific file |
| `git add .` | Stages all changes in the current directory and subdirectories |
| `-A` / `--all` | Stages all changes everywhere in the repo (new, modified, deleted) |
| `-p` / `--patch` | Interactively choose which chunks (hunks) of changes to stage |
| `-u` / `--update` | Stages modifications and deletions, but not new untracked files |
| `-n` / `--dry-run` | Shows what would be staged without actually staging anything |

### Staging vs Unstaging

| Goal | Command |
|---|---|
| Stage everything | `git add .` or `git add -A` |
| Unstage everything (keep files) | `git reset` |
| Unstage a single file (keep it) | `git reset <file>` |


```bash
# Stage a specific file
git add index.html

# Stage everything
git add .

# Interactively choose what to stage (chunk by chunk)
git add -p

# Unstage everything but keep the changes
git reset
```

---
## 6. `git commit`

Saves staged changes as a permanent snapshot in the repository history.

| Flag / Usage | What it does |
|---|---|
| `git commit` | Opens your default editor to write a commit message |
| `-m "<msg>"` | Commits with an inline message — the most common usage |
| `-a` / `--all` | Auto-stages all tracked modified/deleted files and commits (skips `git add` for existing files) |
| `--amend` | Modifies the most recent commit — change the message or add forgotten files |
| `--amend --no-edit` | Amends the last commit without changing its message |
| `--allow-empty` | Creates a commit with no changes — useful for triggering CI pipelines |
| `-v` | Shows a diff of changes in the commit message editor |


```bash
# Commit with an inline message
git commit -m "add login page"

# Stage all tracked files and commit in one step
git commit -am "fix typo"

# Fix the last commit message
git commit --amend -m "corrected message"

# Add a forgotten file to the last commit without changing the message
git add forgotten-file.js
git commit --amend --no-edit
```

---
## 7. `git reset`

Moves the current branch pointer and optionally modifies the staging area or working directory.

| Command | Moves commits? | Clears staging? | Touches files? |
|---|---|---|---|
| `git reset` / `git reset HEAD` / `git reset --mixed HEAD` | No | Yes | No |
| `git reset HEAD~1` / `git reset --mixed HEAD~1` | Yes (undoes 1) | Yes | No |
| `git reset --soft HEAD~1` | Yes (undoes 1) | No | No |
| `git reset --hard HEAD~1` | Yes (undoes 1) | Yes | ⚠️ Yes |

**Memory aid:** soft stops at commits → mixed goes one level further to staging → hard goes all the way to your files.

> `HEAD` = the latest commit on the current branch  
> `HEAD~1` = one commit back, `HEAD~2` = two commits back, etc.


```bash
# Unstage everything (keep all changes in working directory)
git reset

# Undo last commit and unstage changes (keep files)
git reset --mixed HEAD~1

# Undo last commit but keep changes staged
git reset --soft HEAD~1

# ⚠️ Undo last commit and discard ALL changes permanently
git reset --hard HEAD~1
```

---
## 8. `git push`

Uploads local branch commits to a remote repository.

| Flag / Usage | What it does |
|---|---|
| `git push` | Pushes the current branch to its configured upstream remote |
| `git push <remote> <branch>` | Pushes a specific branch to a specific remote |
| `-u` / `--set-upstream` | Pushes and sets the upstream tracking reference — only needed once per new branch |
| `--force` / `-f` | ⚠️ Force-pushes, overwriting remote history. Dangerous on shared branches |
| `--force-with-lease` | Safer force-push — only succeeds if no one else has pushed since your last fetch |
| `--tags` | Pushes all local tags to the remote |
| `-d <branch>` | Deletes a remote branch |

> **Tip:** Use `git push -u origin <branch>` the first time you push a new branch. After that, plain `git push` is enough.


```bash
# First push of a new branch (sets upstream)
git push -u origin feature/login

# Subsequent pushes (upstream already set)
git push

# Safer force push
git push --force-with-lease

# Delete a remote branch
git push origin -d feature/old-branch
```

---
## 9. `git pull`

Fetches changes from the remote **and** merges them into the current branch. Equivalent to `git fetch` + `git merge` in one step.

| Flag / Usage | What it does |
|---|---|
| `git pull` | Fetches from the tracked remote and merges into the current branch |
| `git pull <remote> <branch>` | Pulls a specific remote branch |
| `--rebase` | Replays your local commits on top of the fetched commits instead of merging — cleaner history |
| `--no-rebase` | Explicitly uses merge strategy |
| `--ff-only` | Only pulls if it can fast-forward — aborts if a merge would be needed |
| `--no-commit` | Performs the merge but doesn't auto-commit — lets you inspect first |


```bash
# Pull and merge
git pull

# Pull and rebase (cleaner, linear history)
git pull --rebase

# Only pull if it won't create a merge commit
git pull --ff-only
```

---
## 10. `git fetch`

Downloads changes from a remote **without** merging them. Safe to run anytime — it never touches your working files.

| Flag / Usage | What it does |
|---|---|
| `git fetch` | Fetches all branches from origin without merging |
| `git fetch <remote>` | Fetches from a specific remote |
| `git fetch <remote> <branch>` | Fetches only a specific branch |
| `--all` | Fetches from all configured remotes at once |
| `--prune` / `-p` | Removes local references to remote branches that no longer exist |
| `--tags` | Fetches all tags from the remote |

> **fetch vs pull:** `git fetch` only downloads. `git pull` downloads and merges. Use fetch to preview changes before integrating.


```bash
# Fetch all remote branches (don't merge yet)
git fetch

# Fetch and clean up deleted remote branches
git fetch --prune

# Set prune as default so it always runs on fetch
git config --global fetch.prune true
```

---
## 11. `git merge`

Integrates changes from one branch into the current branch.

| Flag / Usage | What it does |
|---|---|
| `git merge <branch>` | Merges the specified branch into the current branch |
| `--ff` (fast-forward) | Default when possible. Moves pointer forward — no merge commit created |
| `--no-ff` | Forces a merge commit even when fast-forward is possible |
| `--squash` | Collapses all branch commits into one staged change to commit manually |
| `--abort` | Cancels an in-progress merge and restores pre-merge state |
| `--continue` | Resumes a merge after resolving conflicts |
| `-m "<msg>"` | Sets the merge commit message inline |

### Fast-forward vs No-fast-forward

```
Fast-forward (main hasn't moved):        No-fast-forward (main has moved):

Before:  C1─C2        feature: C3─C4    Before:  C1─C2─C5   main
              └─C3─C4  main at C2                      └─C3─C4  feature

After:   C1─C2─C3─C4  main              After:   C1─C2─C5─┐
         (pointer slides forward)                      └─C3─C4─M  main
```

### Resolving Merge Conflicts

| Step | Action |
|---|---|
| 1. Conflict occurs | Git pauses — run `git status` to see affected files |
| 2. Open the file | Edit between `<<<<<<< HEAD` and `>>>>>>>` markers. Everything between `<<<<<<< HEAD` and `=======`; below that to `>>>>>>>` is the incoming branch. |
| 3. Resolve manually | Keep what you want, delete all conflict markers |
| 4. Stage the fix | `git add <file>` |
| 5. Complete | `git merge --continue` or `git commit` |
| Bail out | `git merge --abort` |


```bash
# Switch to main and merge a feature branch
git switch main
git merge feature/login

# Force a merge commit even when fast-forward is possible
git merge --no-ff feature/login

# Squash all feature commits into one
git merge --squash feature/login
git commit -m "add login feature"

# Bail out of a messy merge
git merge --abort
```

---
## 12. `git rebase`

Replays your local commits on top of another branch's commits — making it look like you started your work after the latest remote changes.

### How rebase works step by step

```
Before:                          After rebase:
  C1─C2─R1─R2  (remote/main)      C1─C2─R1─R2─L1'─L2'  (main)
        └─L1─L2  (your local)                  ↑
                                    Your commits replayed on top
                                    with new hashes (L1', L2')
```

1. Git detaches your commits (L1, L2) and sets them aside
2. Moves your branch pointer to the tip of the remote (R2)
3. Replays your commits one by one on top (L1→L1', L2→L2')

> **Key:** L1' and L2' have the same changes as L1 and L2 but have new commit hashes because their parent changed. This is what "rewriting history" means.

### Rebase vs Merge

| | fetch + merge | fetch + rebase |
|---|---|---|
| Creates merge commit? | Yes | No |
| History shape | Branching | Linear |
| Rewrites commits? | No | Yes |
| Safe on shared branches? | Yes | ⚠️ No |
| Best for | Team branches, PRs | Your own local branches |

> **Golden rule:** Never rebase commits that have already been pushed and shared with others.


```bash
# Pull using rebase instead of merge
git pull --rebase

# Or do it manually
git fetch
git rebase origin/main

# Set rebase as the default pull strategy
git config --global pull.rebase true
```

---
## 13. `git clone`

Copies a remote repository onto your local machine. Automatically sets up `origin` pointing back to the source.

| Flag / Usage | What it does |
|---|---|
| `git clone <url>` | Clones into a folder named after the repo |
| `git clone <url> <folder>` | Clones into a specific folder name |
| `--branch <name>` / `-b` | Checks out a specific branch or tag instead of the default |
| `--depth <n>` | Shallow clone with only the last `n` commits — much faster for large repos |
| `--single-branch` | Only clones the history of the checked-out branch |
| `--recurse-submodules` | Also clones any submodules (without this, submodule folders appear empty) |
| `--bare` | Clones a bare repo (no working directory) |

### Shallow clones (`--depth`)

- Still a fully connected repo — `origin` is set up normally
- `git fetch`, `git pull`, `git push` all work normally
- Limitations: `git log` is truncated, `git bisect` won't work properly, `git blame` may be incomplete
- To convert back to a full clone: `git fetch --unshallow`


```bash
# Standard clone
git clone https://github.com/user/repo.git

# Clone into a specific folder
git clone https://github.com/user/repo.git my-folder

# Shallow clone — latest snapshot only (fast, used in CI/CD)
git clone --depth 1 https://github.com/user/repo.git

# Clone a specific branch
git clone -b develop https://github.com/user/repo.git

# Un-shallow a repo to get full history
git fetch --unshallow
```

---
## 14. `git tag`

Marks a specific commit with a permanent, human-readable label. Most commonly used for version releases.

| Flag / Usage | What it does |
|---|---|
| `git tag` | Lists all existing tags |
| `git tag <name>` | Creates a lightweight tag at the current commit |
| `-a <name>` / `--annotate` | Creates an annotated tag (with tagger name, date, message) — recommended for releases |
| `-m "<msg>"` | Sets the tag message inline (used with `-a`) |
| `git tag <name> <commit>` | Tags a specific past commit |
| `-d <name>` | Deletes a tag locally |
| `-l "<pattern>"` | Lists tags matching a pattern |
| `git show <tag>` | Shows tag details and the commit it points to |

### Lightweight vs Annotated Tags

| | Lightweight | Annotated |
|---|---|---|
| What it stores | Just a pointer | Pointer + tagger name, email, date, message |
| Use case | Quick personal bookmarks | Public releases |
| Command | `git tag v1.0.0` | `git tag -a v1.0.0 -m "First release"` |

### Tags and Remotes

> ⚠️ Tags are **not** pushed automatically with `git push`. You must push them explicitly.


```bash
# Create an annotated tag (recommended for releases)
git tag -a v1.0.0 -m "First stable release"

# List all tags
git tag

# List tags matching a pattern
git tag -l "v1.*"

# Push a single tag to remote
git push origin v1.0.0

# Push all local tags to remote
git push origin --tags

# Delete a tag locally
git tag -d v1.0.0

# Delete a tag on the remote
git push origin --delete v1.0.0
```

---
## 15. `git prune`

Removes objects or stale references that are no longer reachable.

| Flag / Usage | What it does |
|---|---|
| `git prune` | Removes unreachable loose objects from the local object store. Rarely run manually. |
| `-n` / `--dry-run` | Shows what would be pruned without deleting anything |
| `-v` / `--verbose` | Lists each object being pruned |
| `git remote prune <remote>` | Removes local tracking refs to remote branches deleted on the remote |
| `git fetch --prune` | Fetches and prunes stale remote-tracking refs in one step — the most common usage |
| `git gc` | Full garbage collection — internally calls prune among other cleanup tasks |

> **In practice:** You'll rarely type `git prune` directly. Use `git fetch --prune` to clean up dead remote branches, and let `git gc` handle the rest automatically.


```bash
# Clean up stale remote-tracking branches (most common use)
git fetch --prune

# Or manually
git remote prune origin

# Set prune to run automatically on every fetch
git config --global fetch.prune true

# Full garbage collection
git gc
```

---
## 16. `git config`

Gets or sets Git configuration values — identity, editor, aliases, and behaviour.

### Scopes

| Flag | Scope | Stored in |
|---|---|---|
| `--global` | All repos for the current user | `~/.gitconfig` |
| `--local` | Current repo only (default) | `.git/config` |
| `--system` | Every user on the machine | `/etc/gitconfig` |

### Common settings

| Setting | What it does |
|---|---|
| `user.name` | Sets the name that appears on your commits |
| `user.email` | Sets the email that appears on your commits |
| `core.editor` | Sets the default text editor for commit messages |
| `init.defaultBranch` | Sets the default branch name for new repos |
| `fetch.prune` | Automatically prunes stale remote refs on every fetch |
| `pull.rebase` | Makes `git pull` use rebase by default |
| `alias.<name>` | Creates a shortcut for a longer Git command |
| `--list` | Lists all current config settings |
| `--unset <key>` | Removes a config setting |

### Editor values

| Editor | Value |
|---|---|
| VS Code | `"code --wait"` |
| Neovim | `"nvim"` |
| Vim | `"vim"` |
| Nano | `"nano"` |
| Zed | `"zed --wait"` |

> Terminal-based editors (Vim, Neovim, Nano) don't need `--wait` because the terminal blocks naturally until you exit them. GUI editors (VS Code, Zed) need `--wait` so the terminal pauses until you close the file tab.


```bash
# Set your identity (required for commits)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Set Neovim as your default editor
git config --global core.editor "nvim"

# Set VS Code as your default editor
git config --global core.editor "code --wait"

# Set default branch name for new repos
git config --global init.defaultBranch main

# Always prune on fetch
git config --global fetch.prune true

# Use rebase instead of merge on pull
git config --global pull.rebase true

# Create an alias: 'git st' instead of 'git status'
git config --global alias.st status

# List all current config
git config --list
```

---
## 17. Key Concepts

### HEAD
A pointer to the current commit you're working from. Usually points to the tip of your current branch.
- `HEAD` = current commit
- `HEAD~1` = one commit back
- `HEAD~2` = two commits back

---

### Fast-forward merge
When `main` hasn't moved since you branched off, Git can simply slide the `main` pointer forward to your branch tip — no merge commit needed. History stays linear.

A merge commit is only required when both branches have new commits since the split point (they've diverged).

---

### Rebase in plain English
Rebase makes it look like **you went second** — as if you had pulled your teammate's latest commits first, then written your own code on top. It replays your commits onto the tip of the remote branch, creating new copies with new hashes.

```
Before:  ...─R1─R2  (remote)
               └─L1─L2  (your local)

After:   ...─R1─R2─L1'─L2'  (your local rebased)
```

---

### Semantic Versioning for tags
The standard naming convention for release tags:

```
v MAJOR . MINOR . PATCH
  │        │        └── Bug fixes
  │        └─────────── New features (backwards compatible)
  └──────────────────── Breaking changes

Example: v1.4.2
```

---

### Quick command reference

| Task | Command |
|---|---|
| Start a new repo | `git init -b main` |
| Clone a repo | `git clone <url>` |
| Check status | `git status` |
| Stage all changes | `git add .` |
| Unstage everything | `git reset` |
| Commit | `git commit -m "message"` |
| View log (visual) | `git log --oneline --graph` |
| Create & switch branch | `git switch -c <name>` |
| Merge a branch | `git merge <branch>` |
| Fetch without merging | `git fetch` |
| Pull with rebase | `git pull --rebase` |
| Push (first time) | `git push -u origin <branch>` |
| Tag a release | `git tag -a v1.0.0 -m "release"` |
| Push tags | `git push origin --tags` |
