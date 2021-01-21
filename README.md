# bashrc
Repo for shared linux environment

Default environment startup configurations; much of the environment is shared across machines, so only a few of these scripts are specific to each machine. Such specific scripts will be labeled

bashrc_pfe
bashrc_freyr
vimrc_pfe

etc. To use the environment

ln -s 

the appropriate script to what's actually called on login for the machine. For example

ln -s ~/environment/bashrc ~/.bashrc
