# ������� ���� �� ���������� ���� ��������� ����� ���������� git ���������
������� ������ � ����� ������ �� GitLab (https://gitlab.com/X5-logs)
����������� ������ � ���� �� �������

git clone https://gitlab.com/X5-logs/x5-scan-n-go.git
���������� VPN � ���� ��������� (���� ��� ����������).

�������� ����� � �������������� ��������� ������������ (���������� git ���������)

git remote add x5scm https://scm.x5.ru/bms/x5-scan-n-go.git
������ ��������� ������������ ����� ������� ���:

git remote -v
���������� ������ �� ���������� git ���������

git push x5scm master
����� �������� ����� � ������.
��� �� �������� ����� �� https://scm.x5.ru/bms/ �������� ����� �������.


��������� ������ �� ������������� ������ �� RStudio, ����������� �� Docker:

git clone https://scm.x5.ru/bms/x5-scan-n-go.git
��� ������������� ������ ������ ������ ����� �������� (origin)

��������� ���� �� ���������� ���� ��������� ����� ���������� git ���������
������� ��� commit

��������� ��������� � ������������� ������ �� ���������� git ���������

git push origin master
��� � ������� ������ Push �� ������� Git � RStudio.

���������� VPN � ���� ��������� (���� ��� ����������).

�������� ��������� � ������� �� ����������� git ��������� �� ���� �������

git pull x5scm master
��������� ��������� � ������� �� ������ �������� � ��� GitLab

git push origin master
Commit-� �� ���� ����� ��� �� �����.

# ������� ����������� �� ������ ������� � ������
- ��������� �������� �����. ������� � ����������� ������.
	- [Project import/export](https://docs.gitlab.com/ee/user/project/settings/import_export.html)
	- [Migrating projects to a GitLab instance](https://docs.gitlab.com/ee/user/project/import/)
1. �������. Project�s homepage. Click Settings in the sidebar. -> General/Export
2. Projects/Gitlab Import

# Q&A
- [GitLab Docs](https://docs.gitlab.com/ee/README.html)
- ��� ������� ������� � ��������� ������������? `git remote add X5` (������)
- [git. Adding a remote](https://docs.github.com/en/free-pro-team@latest/github/using-git/adding-a-remote)
- COOL! [git stash � ��� ��, ��� � �����](http://stepansuvorov.com/blog/2012/11/git-stash-%D1%8D%D1%82%D0%BE-%D1%82%D0%BE-%D1%87%D1%82%D0%BE-%D1%8F-%D0%B8%D1%81%D0%BA%D0%B0%D0%BB/)
```
git stash
git pull
git stash apply
```
- COOL! [How to clone a specific branch in git](https://coderwall.com/p/y7hf6w/how-to-clone-a-specific-branch-in-git)
- COOL! [Clone only one branch {duplicate}](https://stackoverflow.com/questions/4811434/clone-only-one-branch/14930421#14930421)
```
git clone learned --single-branch option to limit cloning to a single branch (surprise!); tags that do not point into the history of the branch are not fetched.
Git actually allows you to clone only one branch, for example:
git clone -b mybranch --single-branch git://sub.domain.com/repo.git
```
- [Clone at Git Repo to a Different Directory](https://til.hashrocket.com/posts/z0f393xq0s-clone-at-git-repo-to-a-different-directory)

�����, ����������� ����� 'huawei' ��������
`git clone -b huawei https://gitlab.com/TV-stat/mts-tv-stat.reports.git ./mts-tv-stat.reports.hw`
- [7.12 ����������� Git - �������� �������](https://git-scm.com/book/ru/v2/%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B-Git-%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%BE%D0%B2). � ���� ������� ��� ����� ������ ������� `git bundle`.
- [Reducing the repository size using Git](https://docs.gitlab.com/ee/user/project/repository/reducing_the_repo_size_using_git.html)
	- COOL! [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)
Removes large or troublesome blobs like git-filter-branch does, but faster. And written in Scala
- [��� ������� ����� �� ������� Git-�, ��� git filter-branch � ������������� �������](https://det-random.livejournal.com/43291.html)
- [BFG Repo-Cleaner by rtyley](https://rtyley.github.io/bfg-repo-cleaner/)
A simpler, faster alternative to git-filter-branch for deleting big files and removing passwords from Git history.
- [How can I delete a commit in Git?](https://www.git-tower.com/learn/git/faq/delete-commits)
- [17. �������� �������� �� �����](https://githowto.com/ru/removing_commits_from_a_branch)
- COOL! [Remove files from Git commit](https://stackoverflow.com/questions/12481639/remove-files-from-git-commit)
- COOL [Take GitHub to the command line](https://cli.github.com/)
- [How to update your Git credentials on Windows](https://cmatskas.com/how-to-update-your-git-credentials-on-windows/)
`Control Panel -> Credential Manager -> Generic Credentials`,
`������ ���������� -> ��� �������� ������ ���������� -> ��������� ������� ������->������� ������ Windows`
- [������ � ���������� ������� ������](https://support.microsoft.com/ru-ru/help/4026814/windows-accessing-credential-manager)
- [7.14 Git Tools - Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage)

# Git
- [Git cheat sheet, extended edition](https://jan-krueger.net/git-cheat-sheet-extended-edition)
- [Clone at Git Repo to a Different Directory](https://til.hashrocket.com/posts/z0f393xq0s-clone-at-git-repo-to-a-different-directory)
`$ git clone https://github.com/cool_user/codez.git ~/codez-v2`
- ��� ������� ���� ������ � git:
`git clone --branch phase_2 https://gitlab.com/TV-stat/mts-tv-stat.reports.git mts-tv-stat.reports.ph2`
- ��� �������� ������������ ������������ � SmartGit? ������� �����: 'C:\Users\<user>\AppData\Roaming\syntevo\SmartGit\18.1\repositories.xml'
- [Not possibly to explicitly disable Auto DevOps on a project?](https://gitlab.com/gitlab-org/gitlab-ce/issues/51760)
- [Enabling/disabling Auto DevOps](https://docs.gitlab.com/ee/topics/autodevops/)
- [How can I switch to another branch in git?](https://stackoverflow.com/questions/47630950/how-can-i-switch-to-another-branch-in-git)
- [How do you clone a Git repository into a specific folder?](https://stackoverflow.com/questions/651038/how-do-you-clone-a-git-repository-into-a-specific-folder). `git clone git@github.com:whatever folder-name`
- COOL! ������ ������� ������������ ����������� �� ��������� ������: `git clone -c http.sslverify=false -b "dev" https://gitlab.com/ishutov/beluga-distr.git beluga-distr-dev`
- ��������� ������ �� ������� �����������: `git remote set-url x5scm https://scm.x5.ru/bms-analytics/x5-bms-diagnostics2.git`
� ����� ������ ����������:
```
git remote -v
origin  https://gitlab.com/X5-logs/x5-bms-diagnostics2.git (fetch)
origin  https://gitlab.com/X5-logs/x5-bms-diagnostics2.git (push)
x5scm   https://scm.x5.ru/bms-analytics/x5-bms-diagnostics2.git (fetch)
x5scm   https://scm.x5.ru/bms-analytics/x5-bms-diagnostics2.git (push)
```
- [How To Switch Branch on Git](https://devconnected.com/how-to-switch-branch-on-git/)
- [Git: Pull All Branches](https://careerkarma.com/blog/git-pull-all-branches/)
`git fetch --all`, `git pull --all`
- [A3.8 Appendix C: ������� Git - �������� �����������](https://git-scm.com/book/ru/v2/Appendix-C%3A-%D0%9A%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B-Git-%D0%92%D0%BD%D0%B5%D1%81%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B9)
- [remote: fatal: pack exceeds maximum allowed size after migrate #3758](https://github.com/git-lfs/git-lfs/issues/3758)
`git rev-list --reverse master | ruby -ne 'i ||= 0; i += 1; puts $_ if i % 2000 == 0' | xargs -I{} git push origin +{}:refs/heads/master`
	- COOL! [git push up to a certain commit](https://pradeeppant.com/2019/05/06/git-push-up-to-a-certain-commit/)
	- COOL! [https://miteshshah.github.io/linux/git/how-to-push-single-commit-with-git/](https://miteshshah.github.io/linux/git/how-to-push-single-commit-with-git/)
```
[mitesh@Matrix ~]$ git log --pretty=oneline
de7e2a469a28d4d74fd4597369cebabd0832636a Test commit for new post
f61b48cb8b1877721e2596a6aa65648a68bb605e new post
```
������� `git rev-list --reverse master` ���� ������ �������� � ������ ��������������� �������, �� ������ �� �������� �������
������ �������� ������ �� ��������: `git push x5scm 10955ac50fb90220c03d077d2cb4e79d01a3bea0:refs/heads/master`. ������ ������� -- � ����� ����� :
```
library(tidyverse)
library(processx)
library(stringi)


# m <- processx::run("git", args = c("log", "--pretty=oneline"))
# �������� ������ �������� �� ���� �������� � �� �������� �������
sha <- processx::run("git", args = c("rev-list", "--reverse", "master"))

unlist(stri_split_lines(sha$stdout, omit_empty = TRUE)) %>%
  # walk(~{print(.x)})
  walk(~{
    processx::run("git", args = c("push", "x5scm", paste0(.x, ":refs/heads/master")),
                  # ���� ������� ���� ������, ���������� ������
                  error_on_status = FALSE, echo_cmd = TRUE, echo = TRUE)
      # print()
  })
```
- ������� �������� �������� [Updates Were Rejected Because the Tip of Your Current Branch Is Behind: Solution](https://www.positioniseverything.net/updates-were-rejected-because-the-tip-of-your-current-branch-is-behind)
- [Fix git �tip of your current branch is behind its remote counterpart� - 4 real-world solutions](https://codewithhugo.com/fix-git-failed-to-push-updates-were-rejected/)
- SmartGit. [Modifying the History](https://docs.syntevo.com/SmartGit/HowTos/Modifying-the-History.html)
- SmartGit. [Interactive Rebase](https://docs.syntevo.com/SmartGit/Latest/Rebase-Interactive.html)
- [Rewriting history](https://www.atlassian.com/git/tutorials/rewriting-history). `Git commit --amend` and other methods of rewriting history
- COOL! [How do I make Git ignore file mode (chmod) changes?]()https://stackoverflow.com/questions/1580596/how-do-i-make-git-ignore-file-mode-chmod-changes	

## ���������� �� �������� �����
- [��������� 5 ������ Git: revert, checkout, reset, merge � rebase](https://proglib.io/p/sravnenie-5-komand-git-revert-checkout-reset-merge-i-rebase-2020-05-25)
- [Git Revert](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)

# GitHub authentication
- [Git push results in �Authentication Failed�](https://stackoverflow.com/questions/17659206/git-push-results-in-authentication-failed). ������� ������� ��� �����������, ������ Windows Credential Manager

## �������� `.gitignore`
- [gitignore - Specifies intentionally untracked files to ignore](https://git-scm.com/docs/gitignore)
- [gitignore.io](https://www.gitignore.io). Create useful .gitignore files for your project

*.log
*.bundle
*.html
*.Rds
*.RDS
*.rds
*.xlsx

data/*
!data/.gitkeep

output/*
!output/.gitkeep

# �������� � Mercurial (Bitbucket �����)
������� ���������, ������������� ��������� ����������� � �������� � `https://github.com/iMissile/bb-import/`
1. ������ TortoseHG 5.0.2. �������� � ����������� ���� ������� `hg-git` � `convert`.
2. �������� ������� Mercurial ����������� � ��������� �����.
3. ��������� � ��� ���� ����������� ����������� ������ ��� ���������� �������� ���� ������ � ������ ����������.
`hg manifest --all | C:\Rtools\mingw_64\opt\bin\python.exe rename.py > rename.txt`
4. ������� �������� bare ����������� git (� �����-������ �����)
`git init --bare bare_repo`
5. � ���������� � Mercurail ������������ ���������� ����� `hg` �� ����������� � ������ ������ � bare git �����������
`hg bookmarks hg`
`hg push path\to\bare_repo`
6. ������ ������� ���� non-bare �����������, �������� ������ -- ���������� ����� hg, ����� �� �������� ������ 'remote HEAD refers to nonexisting ref, unable to checkout'
`git clone -b hg git_bare_repo git_regular_repo`, ��������, `git clone -b hg D:\tmp\0\bare_repo D:\tmp\0\bb_import`
7. ������� ������ ����������� � GitHub
8. ��������� remote � ��������� ����������� �� github: 
`git remote set-url origin https://github.com/iMissile/bb-import.git`
9. �������� ��� � ������
`git push -u --all`
10. ����������� � ������ ����� hg � master, ���������� ����������� github ��� ������������� ���������� ����������� ����:
```
git branch -m hg master
git fetch origin
git branch -u origin/master master
git remote set-head origin -a
```
11. �Ѩ, ������! ����� �� ������� �����, ����������� ����.

- [Free Mercurial Hosting With Helix TeamHub](https://www.perforce.com/hth/mercurial-hosting)
	- [Migrating existing Mercurial (HG) repositories to Helix TeamHub](https://www.perforce.com/manuals/teamhub-user/Content/HTH-User/mercurial.html)
	- [Code Repository Software. Mercurial. Git. SVN. Maven. Ivy. Docker. And more.](https://www.perforce.com/products/helix-teamhub)
- [Converting Mercurial Repositories to Git on Windows](https://helgeklein.com/blog/converting-mercurial-repositories-to-git-on-windows/)
- [Converting Mercurial folder to a Git repository](https://stackoverflow.com/questions/10710250/converting-mercurial-folder-to-a-git-repository/31827990#31827990)
- [the Hg-Git mercurial plugin](https://hg-git.github.io/)
- [About GitHub Importer](https://docs.github.com/en/github/importing-your-projects-to-github/importing-source-code-to-github/about-github-importer)
If you have source code in Subversion, Mercurial, Team Foundation Version Control (TFVC), or another Git repository, you can move it to GitHub using GitHub Importer.
- [������� � Mercurial �� GIT � Atlassian Bitbucket � ����������� ������ � ���������](https://habr.com/ru/post/483454/). � ������������:
���������� ��������������� �� Mercurial � Git �����������, ���������� ������������� ����� ������, � ��������� �� TortoiseHg 3.5.2 ��� Windows.

����������� ������� �� ������ TortoiseHg 5.0.2 (�� ������ ������ �������, ��� ����� ������, ��� � ����� �����, ����������� ����������� ����������, ��� �� ���������� hg-git �� ��������, ��� �� ��� ��� ��). ��� ������ ��� ����� �������� � ���� ���������� hg-git, ������� ������ ���������� ������������� �� ���� �������������.
`hg manifest --all | C:\Rtools\mingw_64\opt\bin\python.exe rename.py > rename.txt`

```
#!/usr/bin/python
# -*- coding: cp1251 -*-

import sys
for path in sys.stdin:
    old = path[:-1] # strip newline
    new = old.decode("cp1251").encode("utf-8")
    print 'rename "%s" "%s"' % (old, new)
```
- `hg convert --filemap rename.txt D:\tmp\0\iwork.HG.clone D:\tmp\0\hg_temp`. ������ convert ���� �������� � extension HG ��� TortoisehHG
- `hg push D:\tmp\0\bare_repo`
- `git clone D:\tmp\0\bare_repo -b hg D:\tmp\0\bb_import` # ��������� ���������� �����
- ������ ������� ����������� �� �������� ���
- ������ ��� ���� �����: `git push -u --all`
�������� ������ "remote HEAD refers to nonexisting ref, unable to checkout". [warning: remote HEAD refers to nonexistent ref, unable to checkout](https://stackoverflow.com/questions/11893678/warning-remote-head-refers-to-nonexistent-ref-unable-to-checkout)
������� � ������� `git branch -a`. ����� ������� `hg`
[���������](https://stackoverflow.com/questions/10710250/converting-mercurial-folder-to-a-git-repository/31827990#31827990)
The hg bookmark is necessary to prevent problems as otherwise hg-git pushes to the currently checked out branch confusing Git. This will create a branch named hg in the Git repository. To get the changes in master use the following commands (only necessary in the first run, later just use git merge or rebase):
������ � ����� �����������
```
$ cd git-repo
$ git checkout -b hg
```

- [Mercurial convert with --filemap fails with any dummy rename](https://stackoverflow.com/questions/57430015/mercurial-convert-with-filemap-fails-with-any-dummy-rename)

- [How to Convert a Mercurial Repository to Git on Windows](https://markheath.net/post/how-to-convert-mercurial-repository-to)
 	- Step 1 � Clone hg-git
 	- Step 2 - Add hg-git as an extension
	- Step 3 � Create a bare git repo to convert into
		`git init --bare git_repo`
	- Step 4 � Push to Git from Mercurial
		`hg bookmarks hg`
		`hg push path\to\git_repo`
	- Step 5 � Get a non-bare git repository
		`git clone git_bare_repo git_regular_repo`
- **�������**
	- ��� hg ����������� �� ��������� ������, ������� ��� �� Helix TeamHub
	- GitHub Importer -- ����������� � Helix �� GH


## ������� �� personal_token
- [SmartGit, unable to push, �remote: HTTP Basic: Access denied�](https://stackoverflow.com/questions/60272933/smartgit-unable-to-push-remote-http-basic-access-denied)
��� ������� � win ���������� ������� ������� ��������� ������� `git config credential.helper`
If it returns "manager", open your Windows Credentials Manager and check if credentials are already stored for gitlab.com.
If so, delete it, then push again: Git should ask for your credentials. Do enter your PAT (Personal Access Token) as password.

- ��� ����������� ������ � windows credential manager ���������� ��� ������� � �������.
	- [Accessing Credential Manager](https://support.microsoft.com/en-us/windows/accessing-credential-manager-1b5c916a-6a16-889f-8581-fc16e8165ac0)
	- [������ � ���������� ������� ������](https://support.microsoft.com/ru-ru/windows/%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF-%D0%BA-%D0%B4%D0%B8%D1%81%D0%BF%D0%B5%D1%82%D1%87%D0%B5%D1%80%D1%83-%D1%83%D1%87%D0%B5%D1%82%D0%BD%D1%8B%D1%85-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-1b5c916a-6a16-889f-8581-fc16e8165ac0)
```
Credential Manager lets you view and delete your saved credentials for signing in to websites, connected applications, and networks.
To open Credential Manager, type *credential manager* in the search box on the taskbar and select Credential Manager Control panel.
Select Web Credentials or Windows Credentials to access the credentials you want to manage.
```
`������ ���������� / ��������� ������� ������`
- [microsoft/Git-Credential-Manager-Core](https://github.com/microsoft/Git-Credential-Manager-Core). Secure, cross-platform Git credential storage with authentication to GitHub, Azure Repos, and other popular Git hosting services.
!!! Windows
GCM Core is included with Git for Windows, and the latest version is included in each new Git for Windows release. This is the preferred way to install GCM Core on Windows. During installation you will be asked to select a credential helper, with GCM Core being set as the default.
!! [Git-Credential-Manager-Core/docs/usage.md](https://github.com/microsoft/Git-Credential-Manager-Core/blob/main/docs/usage.md). After installation, Git will use Git Credential Manager Core and you will only need to interact with any authentication dialogs asking for credentials. GCM Core stays invisible as much as possible, so ideally you�ll forget that you�re depending on GCM at all.

Assuming GCM Core has been installed, use your favorite terminal to execute the following commands to interact directly with GCM.
```
git credential-manager-core [<command> [<args>]]
```
- [How one may check whether credential manager in Git has password stored for a given domain?](https://stackoverflow.com/questions/51803825/how-one-may-check-whether-credential-manager-in-git-has-password-stored-for-a-gi)

# ��� ���� ������� � �����������
��������� ������ `fatal: unsafe repository (REPO is owned by someone else)`
- [Git security vulnerability announced](https://github.blog/2022-04-12-git-security-vulnerability-announced/)
Upgrade your local installation of Git, especially if you are using Git for Windows, or you use Git on a multi-user machine.
- �������� [`safe.directory`](https://git-scm.com/docs/git-config/2.35.2#Documentation/git-config.txt-safedirectory)
`git config --global --add safe.directory D:/iwork.GL/habr-articles`
- [How to add directory recursively on git safe.directory?](https://stackoverflow.com/questions/71855882/how-to-add-directory-recursively-on-git-safe-directory)
	- ������� 1
	From Git 2.36, you can also add * representing 'all' to the safe.directory. It's not recursive as you asked, but it may help depending upon your situation i.e.
```
git config --global --add safe.directory *
```
	- ������� 2
What I did for now, but may not be the perfect solution, is to find all .git folders and add them through a find command.
```
find /full/path -name '.git' -type d -exec bash -c 'git config --global --add safe.directory ${0%/.git}' {} \;
```

# ��������� �������� �����������
- [Server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none](https://stackoverflow.com/questions/21181231/server-certificate-verification-failed-cafile-etc-ssl-certs-ca-certificates-c)
Eventually, add the `http.sslverify` to your `.git/config`.
```
[http]
        sslVerify = false
```
- [Git push requires username and password](https://stackoverflow.com/questions/6565357/git-push-requires-username-and-password)
When you use https for Git pull & push, just configure remote.origin.url for your project, to avoid input username (or/and password) every time you push.

How to configure remote.origin.url:
```
URL format:
    https://{username:password@}github.com/{owner}/{repo}
```
What worked for me was to edit .git/config and use
```
[remote "origin"]
        url = https://<login>:<password>@gitlab.com(...).git
```
It goes without saying that this is an insecure way of storing your password but there are environments/cases where this may not be a problem.