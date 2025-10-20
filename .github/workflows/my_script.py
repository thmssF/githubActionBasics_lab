#!/usr/bin/env python

import os, platform, subprocess, socket

#command = "cat /proc/cpuinfo"
#print(subprocess.check_output(command, shell=True).strip())

kb = float(1024)
mb = float(kb ** 2)
gb = float(kb ** 3)


def load_avg():
    print()
    print('---------- Load Average ----------')
    print()
    print("Load avg (1 mins)  :",round(os.getloadavg()[0],2))
    print("Load avg (5 mins)  :",round(os.getloadavg()[1],2))
    print("Load avg (15 mins) :",round(os.getloadavg()[2],2))

def system():
    core = os.cpu_count()
    host = socket.gethostname()
    print()
    print('---------- System Info ----------')
    print()
    print("Hostname     :",host)
    print("System       :",platform.system(),platform.machine())
    print("Kernel       :",platform.release())
    print('Compiler     :', platform.python_compiler())
    print('CPU          :', core,"(Core)")

def cpu():
    print()
    print('---------- CPU ----------')
    print()
    print("CPU Usage    : ",cpuUsage,"GiB")


def main():
    system()
    load_avg()


main()
