#!/bin/bash
##################################################################
## IF YOU ARE GOING TO EDIT THIS FILE... NO WHITE SPACE PLEASE! ##
##                AND COMMENT EVERYTHING YOU DO!                ##
## ALSO... DONT BE A DICK. USE YOUR TABS.                       ##
##################################################################
# Terminal Colors
red=$'\e[1;31m'
grn=$'\e[1;32m'
yel=$'\e[1;33m'
blu=$'\e[1;34m'
mag=$'\e[1;35m'
cyn=$'\e[1;36m'
end=$'\e[0m'
# All the stuff needed....
install_part_1(){
  if [ -e "PART 1" ]; then
    rm -rf PART 1
    curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/PART%201" > PART 1
  else
    curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/PART%201" > PART 1
  fi
  printf "%s\n${mag}Going to install PART 1.${end}\n"
  git clone https://github.com/RiskyAINetwork/Samantha.git
  mv ./Samantha/* ./
  mkdir samantha
  mv ./Samantha/samantha/* ./samantha
  rm -rf ./Samantha/samantha/
  mv ./Samantha ./samantha
  git clone https://github.com/RiskyAINetwork/Ai-DB.git
  printf "%s$(tput setaf 10)${cyn}Finished installing PART 1.${end}\n"
  rm -rf PART 2
}
install_part_2(){
  printf "%s\n${mag}Going to install PART 2.${end}\n"
  printf "%s\n${mag}Going to move install files to housekeeping folder.${end}\n"
  curl -L "" > Update.sh
  rm -rf Download.sh
  rm -rf setup.sh
  rm -rf Start.sh
  curl "" > Start.sh
  if [[ -d "housekeeping" && ! -L "housekeeping" ]]; then
    printf "%s\n${mag}Found the folder. Going to download the files.${end}\n"
    cd install_files
    if [ -e "Update.sh" ]; then
      rm -rf Update.sh
      curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Update.sh" > Update.sh
    else
      if [ -e "update.sh" ]; then
        rm -rf update.sh
        curl "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Update.sh" > Update.sh
      else
        curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Update.sh" > Update.sh
      fi
    fi
    if [ -e "Download.sh" ]; then
      rm -rf Download.sh
      curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Download.sh" > Download.sh
    else
      if [ -e "download.sh" ]; then
        rm -rf download.sh
        curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Download.sh" > Download.sh
      else
        curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Download.sh" > Download.sh
      fi
    fi
    if [ -e "Setup.sh" ]; then
      rm -rf Setup.sh
      curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Setup.sh" > Setup.sh
    else
      if [ -e "setup.sh" ]; then
        rm -rf setup.sh
        curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Setup.sh" > Setup.sh
      else
        curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Setup.sh" > Setup.sh
      fi
    fi
    if [ -e "Start.sh" ]; then
      rm -rf Start.sh
      curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Setup.sh" > Start.sh
    else
      if [ -e "start.sh" ]; then
        rm -rf start.sh
        curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Setup.sh" > Start.sh
      else
        curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Setup.sh" > Start.sh
      fi
    fi
    printf "%s$(tput setaf 10)${yel}Finished downloading files into folder.${end}\n"
  else
    printf "%s\n${mag}Could not find directory. Going to make it.${end}\n"
    mkdir housekeeping
    cd housekeeping
    curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Update.sh" > Update.sh
    curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Download.sh" > Download.sh
    curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Setup.sh" > Setup.sh
    curl -L "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/Setup.sh" > Start.sh
    printf "%s$(tput setaf 10)${yel}Finished making Folder and downloading files.${end}\n"
  fi
  printf "%s$(tput setaf 10)${cyn}Finished installing PART 2.${end}\n"
  rm -rf PART 2
}
application_run(){
  sleep 3
  printf "%s\n${mag}Going to start the AI.${end}\n"
  cd
  cd Samantha
  sleep 2
  clear
  python application.py Finished.
}
# Clean console incase it is dirty with other commands.
cd ~/
cd
rm -rf Samantha
if [[ -d "Samantha" && ! -L "Samantha" ]]; then
  cd Samantha
  if [ -e "INSTALL" ]; then
    if [ -e "PART 1" ]; then
      install_part_1
      install_part_2
      application_run
    else
      if [ -e "PART 2" ]; then
        install_part_2
        application_run
      else
        printf "%s\n${red}Could not find any of the install Parts!${end}\n"
        if [ -e "PART 1" ]; then
          install_part_1
          install_part_2
          application_run
        else
          if [ -e "PART 2" ]; then
            install_part_2
            application_run
          else
            application_run
            application_run
          fi
        fi
      fi
    fi
  else
    if [ -e "PART 1" ]; then
      install_part_1
      install_part_2
      application_run
    else
      if [ -e "PART 2" ]; then
        install_part_2
        application_run
      else
        application_run
        application_run
      fi
    fi
  fi
else
  mkdir Samantha
  cd Samantha
  curl "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/INSTALL" > INSTALL
  curl "https://raw.githubusercontent.com/RsikyAINetwork/Ai-Setup/master/PART%201" > PART 1
  install_part_1
  install_part_2
  application_run
fi
