#!/usr/bin/env python3

import socket
from fp.fp import FreeProxy
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	

proxy = FreeProxy(country_id=['US', 'BR'], timeout=0.3, rand=True).get()
print(proxy)

