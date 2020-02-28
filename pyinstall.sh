#!/bin/bash

sudo yum update
sudo yum -y install libffi-devel zlib-devel bzip2-devel readline-devel sqlite-devel wget curl llvm ncurses-devel openssl-devel lzma-sdk-devel redhat-rpm-config
sudo yum -y install python-pip
sudo pip install --upgrade
curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

If $SHELL == "/bin/zsh"
then
	cat <<EOF>> ~/.zshrc
	export PATH="/home/$USERNAME/.pyenv/bin:$PATH"
	eval "$(pyenv init -)"
	eval "$(pyenv virtualenv-init -)"
EOF
	source ~/.zshrc
else
	cat <<EOF>> ~/.bashrc
	export PATH="/home/$USERNAME/.pyenv/bin:$PATH"
	eval "$(pyenv init -)"
	eval "$(pyenv virtualenv-init -)"
EOF
	source ~/.bashrc
fi

pyenv install 3.8.2
pyenv install 2.7.0
pyenv global 3.8.2

pyenv virtualenv 3.8.2 py_virt_env_3.8.2
pyenv virtualenv 2.7.0 py_virt_env_2.7.0
pyenv activate py_virt_env_3.8.2

