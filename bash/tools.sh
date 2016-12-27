#!/usr/bin/env bash

# install basic packages
apt-get install cmatrix cmatrix-xfont # cool haxxor screen
apt-get install sl # train graphics
apt-get install tor obfsproxy obfs4proxy # the onion router (tor) suite
apt-get install nano # text-editor
apt-get install screen # virtual session manager
apt-get install figlet # cool text fonts
apt-get install git # git tool (git clone, git push, git log, etc...)
apt-get install zip unzip # zip toolkit
apt-get install ftp-upload # (read the name.)
apt-get install dos2unix # conversion tool
apt-get install openssl # security suite
apt-get install w3m # web browser (terminal based)

# programming/development
apt-get install apache2-utils
apt-get install gcc
apt-get install build-essential
apt-get install libssl-dev
apt-get install default-jre
apt-get install python-pip python3-pip
# apt-get install ncurses-dev

# python modules
apt-get install python-crypto
apt-get install python-mechanize
apt-get install python-requests

# networking tools
apt-get install libpcap-dev
apt-get install tshark
apt-get install tcpdump
apt-get install speedtest-cli
apt-get install darkstat

# system administration
apt-get install htop
apt-get install hping3

# server packages
apt-get install vsftpd # ftp server
apt-get install apache2 php7.0 libapache2-mod-php7.0 # apache server ~ verify: a2query -m php7.0
apt-get install squid # proxy server
apt-get install ircd-irc2 # irc server
apt-get install mysql-server # sql server

# client applications
apt-get install irssi # irc client

# pentesting tools
apt-get install nmap
apt-get install aircrack-ng
apt-get install wifite
apt-get install hydra

# libraries
apt-get install software-properties-common
dpkg --add-architecture i386

# custom packages
# wine
add-apt-repository ppa:wine/wine-builds
apt-get update
apt-get install --install-recommends winehq-devel
# setoolkit
cd ~
git clone https://github.com/trustedsec/social-engineer-toolkit/ set/
cd set/
./setup.py install
cd ~

