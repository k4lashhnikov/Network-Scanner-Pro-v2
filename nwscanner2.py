import scapy.all as scapy
import argparse
import sys
import colorama
from colorama import Fore, Style


def print_banner():
    banner = f"""
{Fore.MAGENTA}
 ███╗   ██╗██╗    ██╗███████╗
 ████╗  ██║██║    ██║██╔════╝
 ██╔██╗ ██║██║ █╗ ██║███████╗
 ██║╚██╗██║██║███╗██║╚════██║
 ██║ ╚████║╚███╔███╔╝███████║
╚═╝  ╚═══╝ ╚══╝╚══╝ ╚══════╝

{Style.RESET_ALL}Author:💀💀 @k4lashhnikov 💀💀 | Security & Ethical Hacking
    """
    print(banner)

def get_user_input():
    parser = argparse.ArgumentParser(description="Network Scanner Using ARP")
    parser.add_argument("-i", "--ip", dest="ip_address", required=True, help="IP Address or Range (ex: 192.168.1.0/24)")
    args = parser.parse_args()
    return args.ip_address

def scan_network(ip):
    try:
        print(f"\n{Fore.YELLOW}📡 Scanning Network...{Style.RESET_ALL}\n")
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = broadcast/arp_request
        answered, _ = scapy.srp(packet, timeout=1, verbose=False)

        print(f"{Fore.GREEN}IP Address\t\tMAC Address\n-----------------------------------------{Style.RESET_ALL}")
        for sent, received in answered:
            print(f"{Fore.BLUE}{received.psrc}\t\t{received.hwsrc}{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Scan Interrupted by User")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[!]Error Scanning Network: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    colorama.init(autoreset=True)
    print_banner()
    user_ip = get_user_input()
    scan_network(user_ip)