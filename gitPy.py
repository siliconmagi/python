import os

# rsync dotfiles to folder
os.chdir('/home/zeal/p/python')
print(os.getcwd())

# push changes to github
os.system('git add -A')
os.system('git commit -m "rsync"')
os.system('git push')
