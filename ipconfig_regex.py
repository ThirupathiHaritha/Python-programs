import re
str="""
   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::492:af5a:aeb0:827b%21
   IPv4 Address. . . . . . . . . . . : 192.168.56.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

Unknown adapter McAfee VPN:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi 2:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi 3:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : bbrouter
   Link-local IPv6 Address . . . . . : fe80::3454:44ba:9d86:7dac%14
   IPv4 Address. . . . . . . . . . . : 192.168.1.5
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1

Ethernet adapter Bluetooth Network Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :"""
Ipv4=re.findall(r'IPv4 Address[.\s]*:\s*([\d.]+)',str)
Subnet=re.findall(r'Subnet Mask[.\s]*:\s*([\d.]+)',str)
Default=re.findall(r'Default Gateway[.\s]*:\s*([\d.]+)',str)
print(Ipv4)
print(Subnet)
print(Default)
