#Exercitiul 5

import argparse
import os
import socket
import psutil
import platform

def get_memory_info():
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "user": memory.used,
        "free": memory.free
    }
def get_cpu_info():
    return { "cores": psutil.cpu_count(logical=False), "threads": psutil.cpu_count(logical=True)}


def system_information():
    parser = argparse.ArgumentParser(
        description = ' Get system information '
    )
    parser.add_argument('-d', '--distro' , action='store_true', help= 'Get distro information')
    parser.add_argument('-m', '--memory', action='store_true', help='Get memory information')
    parser.add_argument('-c', '--cpu', action='store_true', help='Get CPU information')
    parser.add_argument('-u', '--user', action='store_true', help='Get user information')
    parser.add_argument('-l', '--load', action='store_true', help='Get load average information')
    parser.add_argument('-i', '--ip', action='store_true', help='Get IP information')

    args = parser.parse_args()

    if args.distro:
        print("Distro info: ", platform.system())
    if args.memory:
        print("Memory info: ",get_memory_info())
    if args.cpu:
        print("CPU info: ", get_cpu_info())
    if args.user:
        print("User info: ", platform.node())
    if args.load:
        print("Load average info: ",os.getloadavg() )
    if args.ip:
        print("IP info:", socket.gethostbyname("www.google.com")) # using it for google to show that it works because i cant make it work to show my ip address
                                                                  # probably because of some network configurations that have been done on this laptop


system_information()