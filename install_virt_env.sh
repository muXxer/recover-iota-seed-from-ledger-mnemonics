#!/bin/bash

## Functions
_bold=$(tput bold)
_reset=$(tput sgr0)

_red=$(tput setaf 1)
_green=$(tput setaf 2)

function print_ok   { printf "${_bold}${_green}%s${_reset}\n" "$@"; }
function print_err  { printf "${_bold}${_red}%s${_reset}\n" "$@"; }

## Linux Distribution check
print_ok "Checking linux distribution..."

if ! type "gawk" &> /dev/null; then
  print_err "ERROR: gawk is missing! If you're on Debian or Ubuntu, please run 'sudo apt install -y gawk'"
  exit 1
fi

linux_id=`gawk -F= '/^ID=/{print $2}' /etc/os-release`
linux_version_id=`gawk -F= '/^VERSION_ID=/{print $2}' /etc/os-release`
if [ ${linux_id} = 'debian' ];
then
    if [ ${linux_version_id} != '"9"' ];
    then
        print_err "ERROR: This script was tested under Debian 9 (stretch) only! Exiting..."
        exit 1
    fi
elif [ ${linux_id} = 'ubuntu' ];
then
    if ! [[ "${linux_version_id}" =~ ^('"16.04"'|'"16.10"'|'"17.04"'|'"17.10"'|'"18.04"')$ ]];
    then
        print_err "ERROR: This script was tested under Ubuntu 16.04 till 18.04 only! Exiting..."
        exit 1
	fi
else
    print_err "ERROR: This script was created for Debian and Ubuntu only! Exiting..."
    exit 1
fi

print_ok "Updating Packages..."
sudo apt update && sudo apt dist-upgrade -y

print_ok "Installing packages for Python3 virtual environment..."
sudo apt install -y virtualenv python3-dev python3-pip python3-virtualenv python3-venv

print_ok "Creating python virtual environment..."
python3 -m venv .pyenv
. .pyenv/bin/activate
pip install setuptools --upgrade
pip install wheel
pip install -r requirements.txt
print_ok "Creating python virtual environment done!"
