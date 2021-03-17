#!/usr/bin/env python
# -*- coding: Utf-8 -*-

""" Port scan tool:
    ===============

    This computer program allows you to check network ports and return the
    status for each differently scanned port : open or closed.
"""

import sys
import os
import socket
import argparse
from datetime import datetime

__author__ = "ONILLON Louis"
__copyright__ = "Copyright (c) 2021 Wa0k, Crackss"
__license__ = "MIT License"
__version__ = "1.0.0"
__contact__ = "wa0k@mailo.com"
__date__ = "17/03/2021"
__status__ = "Production"
__username__ = "W@0k"


def scan(host_ip: str, port_list: list, port_range: list):
    """ Scans the remote host port.

    :param host_ip: the address IP of the remote host
    :param port_list: the list of all ports to be scanned
    :param port_range: the range in which to perform the analysis
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if port_list:
            for port in port_list:
                if sock.connect_ex((host_ip, port)) == 0:
                    print("Port {}: open".format(port))
                else:
                    print("Port {}: closed".format(port))
        elif port_range:
            for port in range(port_range[0], port_range[1]+1):
                if sock.connect_ex((host_ip, port)) == 0:
                    print("Port {}: open".format(port))
                else:
                    print("Port {}: closed".format(port))
        else:
            for port in range(1, 65535):
                if sock.connect_ex((host_ip, port)) == 0:
                    print("Port {}: open".format(port))
                else:
                    print("Port {}: closed".format(port))
    except KeyboardInterrupt:
        print("The process was suddenly stopped by the user.")
        sys.exit()
    except socket.gaierror:
        print("The host name could not be resolved.")
        sys.exit()
    except socket.error:
        print("Oops, a connection problem has occurred.")
        sys.exit()
    else:
        t2 = datetime.now()
        total = t2 - t1
        print("Scan successfully completed in : {} seconds.".format(total))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port scan tool - Wa0k",
                                     usage="%(prog)s [-h] target_host [-p ports | -r port_range]")

    parser.add_argument(dest="target_host",
                        metavar="target host",
                        action="store",
                        help="IP address of the target host.")

    port_group = parser.add_argument_group(title="Port options")

    port_group.add_argument("-p", "--port",
                            dest="port",
                            metavar="port",
                            action="store",
                            type=int,
                            nargs="*",
                            help="ports that will be scanned.")

    port_group.add_argument("-r", "-range",
                            dest="port_range",
                            metavar="port",
                            type=int,
                            nargs=2,
                            help="scans on the specified port range (from port 1 to port 2).")

    args = parser.parse_args()
    os.system("cls")
    t1 = datetime.now()
    print("--" * 40)
    print("[*] Scanning in progress on :", args.target_host)
    print("[*] Datetime :", t1)
    print("--" * 40)

    if args.port and args.port_range:
        parser.error("Cannot used -p options with -r options.")
    elif args.port_range:
        assert(args.port_range[0] < args.port_range[1]), "Incorrect port range."
    else:
        scan(args.target_host, args.port, args.port_range)
