from bs4 import BeautifulSoup
import requests
import html5lib
import re

global __Variaveis
__Variaveis = {
    'proxys':[],
    'proxys_ip':[],
    'proxys_port':[]
}

site = requests.get('https://www.freeproxy.world/?type=socks5')
sopa = BeautifulSoup(site.text ,'html5lib')

proxy_list = sopa.find('tbody')
proxy_ips = proxy_list.find_all(class_='show-ip-div')
proxy_ports = proxy_list.find_all(href=re.compile('/?port'))

try:
    for i in range(len(proxy_ips)):
        __Variaveis['proxys_ip'].append(proxy_ips[i].string.replace('\n', ''))
except Exception as err:
    print(f'o erro está: {err}')

try:
    for c in range(len(proxy_ports)):
        __Variaveis['proxys_port'].append(proxy_ports[c].string)
except Exception as err:
    print(f'o erro está: {err}')

try:
    for z in range(len(proxy_ips)):
        __Variaveis['proxys'].append(f"{__Variaveis['proxys_ip'][z]}:{__Variaveis['proxys_port'][z]}")
except Exception as err:
    print(f'o erro está: {err}')

with open('proxys.txt', 'w') as file:
    file.write(str(__Variaveis['proxys']).replace('[', '').replace(']', '').replace('\'', '').replace(',', '\n').replace(' ', ''))


print(':)'*80)
