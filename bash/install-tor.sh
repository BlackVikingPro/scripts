#!/usr/bin/env bash

apt-get update && apt-get upgrade
apt-get autoclean && apt-get clean

# install apache2 and PHP7
apt-get install apache2 php7.0 libapache2-mod-php7.0
/etc/init.d/apache2 start

# install tor
apt-get install tor obfsproxy obfs4proxy
/etc/init.d/tor start

clear
mkdir /var/lib/tor/hidden_service

echo Update this in the Torrc file
echo
echo HiddenServiceDir /var/lib/tor/hidden_service/
echo HiddenServicePort 80 127.0.0.1:80
echo
echo Sleeping for 5 seconds...
sleep 5

nano /etc/tor/torrc

chmod 700 /var/lib/tor/hidden_service

# restart tor
/etc/init.d/tor restart

clear
echo Tor Hidden Service is restarted and should be online. Showing hostname now...
echo
cat /var/lib/tor/hidden_service/hostname
sleep 10

echo Thanks for using this script! I hope it helped automate this easily!!
