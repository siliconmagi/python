import os
from time import localtime, strftime
time = strftime("%Y-%m-%d %H:%M:%S", localtime())

print(os.getcwd())

# rsync dotfiles to folder
os.chdir('/home/zeal/p/python')
print(os.getcwd())

# push changes to github
os.system('git add -A')
os.system('git commit -m time')
os.system('git push')
