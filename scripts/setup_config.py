import os

def create_config():
    torrc_config = """
    ## Configuration file for a typical Tor user
    ## Last updated 9 October 2010 for Tor 0.2.2.1-alpha.
    ## (may or may not work for much older or much newer versions of Tor.)
    
    ########## Tor opens a SOCKS proxy on port 9050 by default -- even if you don't
    ## configure one below. Set "SOCKSPort 0" if you plan to run Tor only
    ## as a relay, and not make any local application connections yourself.
    #SOCKSPort 9050 # Default: Bind to localhost:9050 for local connections.
    #SOCKSPort 192.168.0.1:9100 # Bind to this address:port too.

    """
    with open('../config/torrc', 'w') as file:
        file.write(torrc_config)

def main():
    print("Creating torrc configuration...")
    create_config()
    print("Configuration setup is complete!")

if __name__ == "__main__":
    main()
