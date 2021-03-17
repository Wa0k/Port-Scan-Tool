# Port-Scan-Tool
Created by: Louis ONILLON/@Wa0k

License: MIT License

Published on : 17/03/2021

Version 1.0.0

Contact : wa0k@mailo.com

# Description
Port scanners are valuable tools in diagnosing network and connectivity  issues. However, attackers use port scanners to
detect possible access points for infiltration and to identify what kinds of devices you are running on the network, 
like firewalls, proxy servers or VPN servers.

For instance, on Linux, Nmap is the best known tool for network port scanning.

#Port Scanning Responses
A port scanner sends a TCP or UDP network packet and asks the port about their current status. The three types of 
responses are below:
 - **Open, Accepted**: the computer responds and asks if there is anything it can do for you.
 - **Closed, Not Listening**: the computer responds that this port is currently in use and unavailable at this time.
 - **Filtered, Dropped, Blocked**: the computer doesn’t even bother to respond. Port scans generally occur early in the 
   cyber kill chain, during reconnaissance and intrusion. Attackers use port scans to detect targets with open and 
   unused ports that they can repurpose for infiltration, command and control, and data exfiltration or discover what 
   applications run on that computer to exploit a vulnerability in that application.
   
This script can only two of the tree responses above : open and closed.