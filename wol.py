#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author:  LitMeng
# wechat:  louisxie0712
# website: litmeng.com

import socket
import struct
import sys

VERSION = '1.0.0'
HELP = '''
Version: {0}
Usage: wol.py [-m mac_address]

Options:
    -?,-h           : this help
    -v              : show version and exit
    -m mac_address  : where the magic packet will send to. (eg. 2C-4D-54-CF-9E-50 or 2C:4D:54:CF:9E:50)
'''


def help():
    print(HELP.format(VERSION))


# 获取本机IP
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def wake_on_lan(mac_address):
    print('start send magic packet to ' + mac_address)
    mac_address_fmt = mac_address.replace('-', '').replace(':', '')
    host_ip = get_host_ip()
    host = (host_ip[: host_ip.rindex('.') + 1] + '255', 9)
    data = ''.join(['FFFFFFFFFFFF', mac_address_fmt * 16])
    send_data = b''

    for i in range(0, len(data), 2):
        send_data = b''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, host)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        help()
        sys.exit(0)

    args = sys.argv[1:]
    for index, arg in enumerate(args):
        if not arg.startswith('-'):
            continue
        if arg[1:] == '?' or arg[1:] == 'h':
            help()
        if arg[1:] == 'v':
            print(VERSION)
        if arg[1:] == 'm':
            mac_address = args[index + 1]
            wake_on_lan(mac_address)
