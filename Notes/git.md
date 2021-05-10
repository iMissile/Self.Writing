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
`������ ���������� -> ��� �������� ������ ���������� -> ��������� ������� ������`
- [������ � ���������� ������� ������](https://support.microsoft.com/ru-ru/help/4026814/windows-accessing-credential-manager)
- [7.14 Git Tools - Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage)

# Git
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