#!/usr/bin/python
import re
import subprocess

script = '''
    if [ "$GIT_AUTHOR_EMAIL" = "" ]; then
        GIT_COMMITTER_NAME="Ghost";
        GIT_AUTHOR_NAME="Ghost";
        GIT_COMMITTER_EMAIL="ghost@xinhua.dev";
        GIT_AUTHOR_EMAIL="ghost@xinhua.dev";
        git commit-tree "$@";
'''

with open('./authors.txt', mode='r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        match = re.match(r'^(\S+)\s*=\s*(.+)\s<(\S+)>$', line)
        if match is None:
            continue
        (oldemail, name, email) = match.groups()

        temp = '''
    elif [ "$GIT_AUTHOR_EMAIL" = "%s" ]; then
        GIT_COMMITTER_NAME="%s";
        GIT_AUTHOR_NAME="%s";
        GIT_COMMITTER_EMAIL="%s";
        GIT_AUTHOR_EMAIL="%s";
        git commit-tree "$@";
''' % (oldemail, name, name, email, email)

        script = script + temp


script = script + '''
    else
        git commit-tree "$@";
    fi
'''

cmd = '''
git filter-branch -f --commit-filter '%s' --tag-name-filter cat -- --all
''' % script

print(cmd)

yes = input('Are you sure to execute the above command (y/n) ')
if yes == 'y':
    subprocess.run(cmd, shell=True)
else:
    print('exit')