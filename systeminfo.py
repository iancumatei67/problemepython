import os
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(os.name)
print(ip_address)