'''
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=113 time=83.3 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 83.296/83.296/83.296/0.000 ms
'''

import sys
import subprocess

ips = sys.argv[1:]

for ip in ips:
    resp = ''
    try:
        resp = subprocess.check_output(['ping', '-c', '1', ip]).decode()
    except:
        pass
    if resp:
        resp = resp.split(f'\n\n--- {ip} ping statistics ---\n')[1].split('\n')[0]
        resp = resp.split(', ')

        # print(resp)
        result = f'IP Address: {ip} | Responded: '

        result += 'Yes | '
        result += f"Response Time: {resp[3].split(' ')[1]}"

        print(result)
    else:
        print(f"IP Address: {ip} | Responded: No")
