#/bin/python3

import os
# 1. Display the OS version – if Windows, display the Windows details; if
# executed on Linux, display the Linux details.
print ("1. Your Linux os version is: ")
os. system ("uname -a")

#2.Display the private IP address
print ("2a. Your Private IP address is: ")
os.system("ifconfig |sed -n 2p |awk '{print $2}'")

#public IP address
print ("2b.Your public IP address is: ")
os.system("curl -s ifconfig.me")

#the default gateway
print("2c.Your default gateway is: ")
os.system ("route -n |sed -n 3p |awk '{print $2}'")

#3. Display the hard disk size; free and used space.
os.system ("df -H")

#4. Display the top five (5) directories and their size.
os.system ("cd / && ls -lSH")

#5. Display the CPU usage; refresh every 10 seconds
os.system ("sar -u 10 5")

#Note -u is an option to refresh the CPU usage every 10seconds and 5 is for count
