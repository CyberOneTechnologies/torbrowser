####################################################################################
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Darknet Tor Install░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Developed by Aarsyth░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░░░░░░░░░░░░GitHub Repository: https://github.com/CyberOneTechnologies/░░░░░░░░░░░#
#░░░░░░░░░░░░░░░░░For support, reach out on Discord: Aarsyth#0563░░░░░░░░░░░░░░░░░░#
####################################################################################
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░░░░░░░░█████╗░██╗░░░██╗██████╗░███████╗██████╗░░█████╗░███╗░░██╗███████╗░░░░░░░░░#
#░░░░░░░██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║██╔════╝░░░░░░░░░#
#░░░░░░░██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝██║░░██║██╔██╗██║█████╗░░░░░░░░░░░#
#░░░░░░░██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗██║░░██║██║╚████║██╔══╝░░░░░░░░░░░#
#░░░░░░░╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚███║███████╗░░░░░░░░░#
#░░░░░░░░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝░░░░░░░░░#
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
####################################################################################
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
####################################################################################
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░Description:░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#----------------------------------------------------------------------------------#
#░This script will be responsible for downloading the appropriate Tor Browser░░░░░░#
#░package from the official Tor Project website, verifying the downloaded package,░# 
#░Python's os and subprocess modules to execute system commands and requests module# 
#░to download files.░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░# 
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░Note that this is a simplified version. Further refinements may be required for░░#
#░full functionality and error handling.░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░#
####################################################################################


import os

def create_hidden_service_directory():
    hidden_service_path = '/var/lib/torbrowser/config/hidden_service/'
    os.makedirs(hidden_service_path, exist_ok=True)
    os.chmod(hidden_service_path, 0o700)

def get_bridge_info():
    bridge_address = input("Enter the bridge address: ")
    bridge_fingerprint = input("Enter the bridge fingerprint: ")
    return bridge_address, bridge_fingerprint

def create_config(bridge_address, bridge_fingerprint):
    torrc_config = f"""
# This is the torrc file that will be written by the setup_config.py script.
# It contains configuration options for the Tor service.
# The options written here will be overwritten by the script when it runs.

# SOCKS proxy configuration
SOCKSPort 9050
SOCKSPolicy accept 127.0.0.1
SOCKSPolicy accept ::1

# Enable directory authorities for bootstrap
UseBridges 1
Bridge obfs4 {bridge_address} {bridge_fingerprint}

# Hidden service configuration
HiddenServiceDir /var/lib/torbrowser/config/hidden_service/
HiddenServicePort 80 127.0.0.1:8080
"""

    with open('../config/torrc', 'w') as file:
        file.write(torrc_config)

def main():
    print("Tor Configuration Setup")
    create_hidden_service_directory()
    bridge_address, bridge_fingerprint = get_bridge_info()
    print("Creating torrc configuration...")
    create_config(bridge_address, bridge_fingerprint)
    print("Configuration setup is complete!")

if __name__ == "__main__":
    main()
