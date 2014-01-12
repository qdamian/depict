# Install tools available in travis VMs like npm, phantomjs, xvfb, etc

set -e

# apt packages (including latest version of node.js & npm)
apt-get -y install python-software-properties
add-apt-repository -y ppa:chris-lea/node.js
apt-get -y update
apt-get -y install git python-pip nodejs curl phantomjs firefox daemon
curl https://npmjs.org/install.sh | sh
npm install -g grunt-cli

pip install virtualenv travis-solo

# xvfb
curl https://gist.github.com/fedesilva/957876/raw/f4e585ad6c40fe570a88a0dc9f0c340e675397d2/xvfb_daemon.sh > /etc/init.d/xvfb
chmod +x /etc/init.d/xvfb
