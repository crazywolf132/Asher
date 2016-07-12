#!/bin/bash

# Any subsequent(*) commands which fail will cause the shell script to exit immediately
set -e

# Supported versions of node: v4.x, v5.x
PYTHON_VERSION="2.*"

# Terminal Colors
red=$'\e[1;31m'
grn=$'\e[1;32m'
yel=$'\e[1;33m'
blu=$'\e[1;34m'
mag=$'\e[1;35m'
cyn=$'\e[1;36m'
end=$'\e[0m'

# Ensure we are using sudo
if [ "$(whoami)" = "root" ];
then
	echo "This script cannot use root permissions, try: ./${0##*/} "
	exit 0
fi

cat << "EOF"
R.A.I.N

01010010 00101110 01000001 00101110 01001001 00101110 01001110




Risky Artificial Intelligence Network.

01010010 01101001 01110011 01101011 01111001 00100000 01000001 01110010 01110100 01101001 01100110 01101001 01100011 01101001 01100001 01101100 00100000 01001001 01101110 01110100 01100101 01101100 01101100 01101001 01100111 01100101 01101110 01100011 01100101 00100000 01001110 01100101 01110100 01110111 01101111 01110010 01101011 00101110

EOF

printf "%sThis script will install the Samantha AI and it's dependencies.\n"

# Ensure the use would like to start the install
read -r -p "Would you like to continue? [y/N] " response
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then
    printf "%sExcellent! ${red}Please do not exit this script until it is complete.${end}\n"
else
    exit 1
fi

printf "%s\n${mag}Installing Homebrew...${end}\n"
#/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
#/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
printf "%s$(tput setaf 10)Homebrew is now installed!${end}"

printf "%s\nChecking for python...\n"
if which python > /dev/null 2>&1;
then
    printf "%s$(tput setaf 10) ${grn}python is already installed, great job!${end}\n"
else
    # Install Python
    printf "%s${blu}Downloading and Installing python${end}\n"
    #Installing it...
    brew install python
    #Finished installing
    printf "%s$(tput setaf 10)python is now installed!${end}\n"
fi

# Getting the code
printf "%s\n${blu}Cloning Git Repo...${end}\n"
cd
#Going to delete the files if they exist
rm -rf Samantha
git clone https://github.com/crazywolf132/Samantha.git
printf "%s\n$(tput setaf 10)Samantha is now downloaded${end}\n"

# Installing dependencies.
printf "%s${blu}Cloning Git Python...${end}\n"
cd
rm -rf GitPython
git clone https://github.com/gitpython-developers/GitPython.git
# Done downloading
printf "%s\n$(tput setaf 10)Git python is now downloaded!${end}\n"
# Begin install
cd GitPython
python setup.py install
# Finished install
printf "%s\n$(tput setaf 10)Git python is now installed!${end}\n"
# Now removing the remains
cd ../
rm -R GitPython


cd Samantha

# Download Database
printf "%s${blu}Grabbing Database$...{end}\n"
git clone https://github.com/crazywolf132/Ai-DB


# Install package to make Samantha speak
printf "%s${blu}Installing espeak...${end}\n"
brew install espeak


printf "%s${blu}Installing all updates for R.A.I.N...${end}\n"
printf "%s${yel}This may take a while. Go grab a beer :)${end}\n"
pip install fuzzywuzzy
pip install jsondb
pip install jsondatabase
pip install nltk
pip install pymongo
pip install python-twitter
pip install textblob
pip install python-Levenshtein


# The mirror is now installed, yay!
cat << "EOF"

        |        R.A.I.N is now installed!
       / \
      / _ \      Once you fill out your config you can start the Ai with:
     |.o '.|     sudo bash Finish.sh
     |'._.'|
     |     |
   ,'|  |  |`.
  /  |  |  |  \
  |,-'--|--'-.|

EOF
# ASCII art found on http://textart.io/
exit 0
