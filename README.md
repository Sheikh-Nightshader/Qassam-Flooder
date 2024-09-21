# Qassam-Flooder
Multi Purpose Denial of Service with proxy support. Uses Layer 4 and Layer 7 Attack methods, and custom fake useragents to mask an attack. Supports UDP, TCP, HTTP and Slowloris attack methods This is a power tool and should be used with care. I take no responsibility for the use or misuse of this tool. To futher the understanding of DDOS here it is...

usage: qassam.py [-h] -c {udp,tcp,http,slowloris} [-u URL] [-i IP] [-p PORT] [-t TIMES] [-th THREADS]
                 [-pfile PROXYFILE]

PowerFlood - DDoS Tool by Sheikh

options:
  -h, --help            show this help message and exit
  -c {udp,tcp,http,slowloris}, --choice {udp,tcp,http,slowloris}
                        Flood type
  -u URL, --url URL     URL for HTTP flood
  -i IP, --ip IP        Target IP address
  -p PORT, --port PORT  Port number
  -t TIMES, --times TIMES
                        Number of packets to send
  -th THREADS, --threads THREADS
                        Number of threads
  -pfile PROXYFILE, --proxyfile PROXYFILE
                        File with proxie
