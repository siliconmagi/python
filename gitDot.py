import os

# rsync dotfiles to folder
os.system('rsync -avz ~/.config/fish/config.fish ~/p/dotfiles')
os.system('rsync -avz ~/.tmux.conf.local ~/p/dotfiles')
os.system('rsync -avz ~/.bashrc ~/p/dotfiles')
os.system('rsync -avz ~/.vimrc ~/p/dotfiles')
os.chdir('/home/zeal/p/dotfiles')
print(os.getcwd())

# push changes to github
os.system('git add -A')
os.system('git commit -m "rsync"')
os.system('git push')
