#!/bin/bash
##########
# Script info: Script to integrate TOR Monitoring with QRadar appliance
##########
# Download feed from https://www.dan.me.uk/torlist/
wget -U firefox https://www.dan.me.uk/torlist > /root/scripts/TOR_feed.txt

# Load data in to reference set:
/opt/qradar/bin/ReferenceSetUtil.sh load <RS name> /root/scripts/TOR_feed.txt
