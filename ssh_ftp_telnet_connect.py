# install these modules first "pip install modulename"

import paramiko
from ftplib import FTP
import telnetlib

# Select Protocol
protocol = input("Enter for ssh 's', ftp 'f' or telnet 't': ")

# Connect to the remote server
if protocol == "s":
    # Give Hostname and Credentials
    shost = input("hostname: ")
    susername = input("username: ")
    spassword = input("password: ")
    # Create an SSH client and connect to the server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(shost, username=susername, password=spassword)
    print("SSH connection established")
    # Perform some SSH commands here...
    ssh.close()
elif protocol == "f":
    # Give Hostname and Credentials
    fhost = input("hostname: ")
    fusername = input("username: ")
    fpassword = input("password: ")
    # Create an FTP client and connect to the server
    ftp = FTP(fhost)
    ftp.login(user=fusername, passwd=fpassword)
    print("FTP connection established")
    # Perform some FTP commands here...
    ftp.quit()
elif protocol == "t":
    # Give Hostname and Credentials
    thost = input("hostname: ")
    tusername = input("username: ")
    tpassword = input("password: ")
    # Create a Telnet client and connect to the server
    tn = telnetlib.Telnet(thost)
    tn.read_until(b"login: ")
    tn.write(tusername.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(tpassword.encode('ascii') + b"\n")
    print("Telnet connection established")
    # Perform some Telnet commands here...
    tn.close()
else:
    print("Invalid protocol selected")
