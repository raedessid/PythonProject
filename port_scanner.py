# port_scanner.py
import nmap

def scan_ports(target_ip):
    scanner = nmap.PortScanner()
    try:
        scanner.scan(target_ip, '1-1024', '-sV')
        results = []
        if 'tcp' in scanner[target_ip]:
            for port in scanner[target_ip]['tcp']:
                state = scanner[target_ip]['tcp'][port]['state']
                service = scanner[target_ip]['tcp'][port]['name']
                product = scanner[target_ip]['tcp'][port].get('product', 'Unknown')
                version = scanner[target_ip]['tcp'][port].get('version', 'Unknown')
                results.append((port, service, f"{product} {version}"))
        return results
    except Exception as e:
        print(f"Error: {e}")
        return []
