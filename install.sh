#!/usr/bin/env bash

YELLOW="\e[93m"
GREEN="\e[32m"
RED="\e[31m"
END="\e[0m"

# check_root.exe
if [[ $EUID -ne 0 ]]; then
  echo ''
  echo -e '${RED} [X] please run this as root. ${END}'
  echo ''
  exit 1
fi

# update the system prior to install
clear
echo ''
echo -e "${YELLOW}[!] updating & upgrading... ${END}"
echo ''
sudo apt-get update -y && sudo apt-get upgrade -y
echo ''
echo  -e "${GREEN}[+] finished updating & upgrading! ${END}"


# install serial killer + his rulebook
if ! [ -x "$(command -v john)" ]; then
  echo -e "${RED}[X] JtR (john the ripper) is not found on the system. proceeding to install... ${END}"
  echo ''
  sudo apt-get install john -y
  echo ''
  echo -e "${GREEN}[+] JtR has been installed. ${END}"
  echo -e "${YELLOW}[!] installing username rule for JtR... ${END}"  # install username rule, thank you Dzmitry Savitski! <3
  echo ''
  curl https://gist.githubusercontent.com/dzmitry-savitski/65c249051e54a8a4f17a534d311ab3d4/raw/5514e8b23e52cac8534cc3fdfbeb61cbb351411c/user-name-rules.txt >> /etc/john/john.conf
  echo ''
  echo -e "${GREEN}[+] added rule list to /etc/john/john.conf ${END}"
  echo -e "${GREEN}[+] finished! :)"
  echo ''
  exit 0
else
  echo -e "${GREEN}[+] JtR found on the machine! ${END}"
  echo -e "${YELLOW}[!] installing username rule for JtR... ${END}"  # install username rule, thank you Dzmitry Savitski! <3
  echo ''
  curl https://gist.githubusercontent.com/dzmitry-savitski/65c249051e54a8a4f17a534d311ab3d4/raw/5514e8b23e52cac8534cc3fdfbeb61cbb351411c/user-name-rules.txt >> /etc/john/john.conf
  echo ''
  echo -e "${GREEN}[+] added rule list to /etc/john/john.conf ${END}"
  echo -e "${GREEN}[+] finished! :)"
  echo ''
  exit 0
fi
