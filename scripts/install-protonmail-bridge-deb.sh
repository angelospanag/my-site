#!/bin/sh

# DEB filename
DEB_FILENAME="protonmail-bridge_1.6.3-1_amd64.deb"

# Download Protonmail Bridge deb
wget https://protonmail.com/download/bridge/${DEB_FILENAME}

# Download and install gpg key
wget https://protonmail.com/download/bridge_pubkey.gpg
gpg --dearmor --output debsig.gpg bridge_pubkey.gpg
sudo mkdir -p /usr/share/debsig/keyrings/E2C75D68E6234B07
sudo mv debsig.gpg /usr/share/debsig/keyrings/E2C75D68E6234B07

# Download and install policy file
wget https://protonmail.com/download/bridge.pol
sudo mkdir -p /etc/debsig/policies/E2C75D68E6234B07
sudo mv bridge.pol /etc/debsig/policies/E2C75D68E6234B07

# Verify and install Protonmail Bridge
sudo apt install -y debsig-verify
debsig-verify ./${DEB_FILENAME}
if [ $? -ne 0 ]; then
    echo "Error, ${DEB_FILENAME} not verified"
else
    echo "Success, ${DEB_FILENAME} verified"
    sudo apt install -y ./${DEB_FILENAME}
fi

# Cleanup
rm ./bridge_pubkey.gpg
rm ./${DEB_FILENAME}
