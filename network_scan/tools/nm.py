import nmap3, socket
from netaddr import IPNetwork

def get_current_network():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    current_ip = s.getsockname()[0]
    s.close()
    return str(IPNetwork(f'{current_ip}/255.255.255.0').cidr)


def scan_network():
    nmap = nmap3.Nmap()
    subnet_net = get_current_network()
    result = nmap.scan_top_ports(subnet_net)
    print(result)

def scan_ip():
    ipadd = input("What IP you want to scan? ")
    nmap = nmap3.Nmap()
    result = nmap.scan_top_ports(ipadd)
    print(result)

def scan_os():
    net_user = input("What network/IP do you want to scan? ")
    nmap = nmap3.Nmap()
    os_result = nmap.nmap_os_detection(net_user)
    print(os_result)