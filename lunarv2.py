import os
import sys
import time
import json
import re
import socket
import requests
import whois
import phonenumbers
from datetime import datetime
from colorama import init, Fore
import concurrent.futures
import dns.resolver
import ipaddress

init(autoreset=True)

# Color Scheme
PURPLE = "\033[95m"
DARK_PURPLE = "\033[35m"
LIGHT_PURPLE = "\033[38;5;141m"
BRIGHT_PURPLE = "\033[38;5;165m"
NEON_PURPLE = "\033[38;5;129m"
CYAN = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
ORANGE = "\033[38;5;208m"
BLUE = "\033[34m"
END = "\033[0m"

TERMINAL_WIDTH = 90

LOGO = f'''
{BRIGHT_PURPLE}╔══════════════════════════════════════════════════════════════════════════╗{END}
{BRIGHT_PURPLE}║                                                                            ║{END}
{NEON_PURPLE}║    {BRIGHT_PURPLE}█▓▒░           LUNAR v2 - ADVANCED OSINT TOOL              ░▒▓█    {END}║
{DARK_PURPLE}║    {LIGHT_PURPLE}█▓▒░                                                            ░▒▓█    {END}║
{BRIGHT_PURPLE}║    {NEON_PURPLE}█▓▒░    {BRIGHT_PURPLE},──.                                             ,──.     {NEON_PURPLE}░▒▓█    {END}║
{NEON_PURPLE}║    {BRIGHT_PURPLE}█▓▒░    {DARK_PURPLE}│  │   ,──.,──.,──,──,  ,──,──.,──.──.,──.  ,──.     {BRIGHT_PURPLE}░▒▓█    {END}║
{BRIGHT_PURPLE}║    {NEON_PURPLE}█▓▒░    {BRIGHT_PURPLE}│  │   │  ││  ││      ╲' ,─.  ││  .──' ╲  `'  ╱     {NEON_PURPLE}░▒▓█    {END}║
{NEON_PURPLE}║    {BRIGHT_PURPLE}█▓▒░    {LIGHT_PURPLE}│  '──.'  ''  '│  ││  │╲ '─'  ││  │     ╲    ╱     {BRIGHT_PURPLE}░▒▓█    {END}║
{BRIGHT_PURPLE}║    {NEON_PURPLE}█▓▒░    {NEON_PURPLE}`─────' `────' `──''──' `──`──'`──'      `──'     {NEON_PURPLE}░▒▓█    {END}║
{DARK_PURPLE}║    {LIGHT_PURPLE}█▓▒░                                                            ░▒▓█    {END}║
{BRIGHT_PURPLE}║    {NEON_PURPLE}█▓▒░           [LEGAL OSINT & NETWORK ANALYSIS]               ░▒▓█    {END}║
{BRIGHT_PURPLE}║                                                                            ║{END}
{BRIGHT_PURPLE}╚══════════════════════════════════════════════════════════════════════════╝{END}
'''

def set_terminal_size():
    if os.name == 'nt':
        os.system(f'mode con: cols={TERMINAL_WIDTH} lines=45')
        os.system('color 07')

def center_text(text, width=TERMINAL_WIDTH):
    lines = text.split('\n')
    centered_lines = []
    for line in lines:
        line_length = 0
        i = 0
        while i < len(line):
            if line[i:i+2] == '\033[':
                i = line.find('m', i) + 1
            else:
                line_length += 1
                i += 1
        padding = (width - line_length) // 2
        centered_lines.append(' ' * padding + line)
    return '\n'.join(centered_lines)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_color(text, color=BRIGHT_PURPLE, center=False, end="\n"):
    if center:
        print(center_text(f"{color}{text}{END}"), end=end)
    else:
        print(f"{color}{text}{END}", end=end)

def print_banner():
    clear_screen()
    set_terminal_size()
    print("\n" + LOGO)
    print_color("╔══════════════════════════════════════════════════════════════════════════╗", NEON_PURPLE)
    print_color("║                      Advanced Intelligence Gathering                    ║", BRIGHT_PURPLE)
    print_color("╚══════════════════════════════════════════════════════════════════════════╝", NEON_PURPLE)
    print()

# ==================== DISCORD OSINT (LEGAL) ====================
def discord_user_lookup():
    """Get public Discord user information (legal method)"""
    print_color("\n" + "─" * 60, NEON_PURPLE, True)
    print_color("📱 DISCORD USER LOOKUP", BRIGHT_PURPLE, True)
    print_color("─" * 60, NEON_PURPLE, True)
    
    discord_id = input(f"\n{LIGHT_PURPLE}Enter Discord User ID (18-digit number): {BRIGHT_PURPLE}").strip()
    print(END, end="")
    
    if not discord_id.isdigit() or len(discord_id) != 18:
        print_color("❌ Invalid Discord ID format. Must be 18 digits.", RED, True)
        return None
    
    print_color("\n🔍 Querying Discord API...", CYAN, True)
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Method 1: Direct API call (may be rate limited)
        response = requests.get(f'https://discord.com/api/v9/users/{discord_id}', 
                              headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            print_color("\n✅ Discord User Found!", GREEN, True)
            print_color("═" * 50, NEON_PURPLE, True)
            
            results = [
                f"{NEON_PURPLE}┌────────────────────────────────────────────────────┐{END}",
                f"{BRIGHT_PURPLE}│              DISCORD USER INFORMATION              │{END}",
                f"{NEON_PURPLE}├────────────────────────────────────────────────────┤{END}",
                f"{LIGHT_PURPLE}│  User ID:      {CYAN}{data.get('id', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  Username:     {CYAN}{data.get('username', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  Discriminator:{CYAN}{data.get('discriminator', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  Avatar:       {CYAN}{'Yes' if data.get('avatar') else 'No':<35}{END}│",
                f"{LIGHT_PURPLE}│  Bot:          {CYAN}{'Yes' if data.get('bot') else 'No':<35}{END}│",
                f"{NEON_PURPLE}└────────────────────────────────────────────────────┘{END}"
            ]
            
            if data.get('avatar'):
                avatar_url = f"https://cdn.discordapp.com/avatars/{discord_id}/{data['avatar']}.png?size=1024"
                results.append(f"\n{BRIGHT_PURPLE}📷 Avatar URL: {CYAN}{avatar_url}{END}")
            
            print("\n".join(results))
            
        elif response.status_code == 404:
            print_color("❌ User not found or account deleted.", RED, True)
        elif response.status_code == 429:
            print_color("⚠️ Rate limited. Try again later.", YELLOW, True)
        else:
            print_color(f"❌ API Error: {response.status_code}", RED, True)
            
    except Exception as e:
        print_color(f"❌ Error: {str(e)}", RED, True)
    
    return None

def discord_webhook_analyzer():
    """Analyze Discord webhook URLs for information"""
    print_color("\n" + "─" * 60, NEON_PURPLE, True)
    print_color("🔗 DISCORD WEBHOOK ANALYZER", BRIGHT_PURPLE, True)
    print_color("─" * 60, NEON_PURPLE, True)
    
    webhook_url = input(f"\n{LIGHT_PURPLE}Enter Discord Webhook URL: {BRIGHT_PURPLE}").strip()
    print(END, end="")
    
    if "discord.com/api/webhooks/" not in webhook_url:
        print_color("❌ Invalid Discord webhook URL.", RED, True)
        return
    
    print_color("\n🔍 Analyzing webhook...", CYAN, True)
    
    try:
        # Extract webhook ID and token
        parts = webhook_url.split('/')
        webhook_id = parts[-2] if len(parts) > 1 else "Unknown"
        webhook_token = parts[-1] if len(parts) > 0 else "Unknown"
        
        # Try to get webhook info
        response = requests.get(f"https://discord.com/api/v9/webhooks/{webhook_id}/{webhook_token}", 
                              timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            print_color("\n✅ Webhook Information Found!", GREEN, True)
            print_color("═" * 50, NEON_PURPLE, True)
            
            info_lines = [
                f"{NEON_PURPLE}┌────────────────────────────────────────────────────┐{END}",
                f"{BRIGHT_PURPLE}│              WEBHOOK INFORMATION                   │{END}",
                f"{NEON_PURPLE}├────────────────────────────────────────────────────┤{END}",
                f"{LIGHT_PURPLE}│  Webhook ID:   {CYAN}{data.get('id', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  Name:         {CYAN}{data.get('name', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  Channel ID:   {CYAN}{data.get('channel_id', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  Guild ID:     {CYAN}{data.get('guild_id', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  Application:  {CYAN}{data.get('application_id', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  Avatar:       {CYAN}{'Yes' if data.get('avatar') else 'No':<35}{END}│",
                f"{NEON_PURPLE}└────────────────────────────────────────────────────┘{END}"
            ]
            
            print("\n".join(info_lines))
            
        else:
            print_color("❌ Invalid or expired webhook.", RED, True)
            
    except Exception as e:
        print_color(f"❌ Error: {str(e)}", RED, True)

# ==================== ENHANCED IP LOOKUP ====================
def enhanced_ip_lookup():
    """Enhanced IP lookup with multiple data sources"""
    print_color("\n" + "─" * 60, NEON_PURPLE, True)
    print_color("🌐 ENHANCED IP LOOKUP", BRIGHT_PURPLE, True)
    print_color("─" * 60, NEON_PURPLE, True)
    
    ip = input(f"\n{LIGHT_PURPLE}Enter IP Address: {BRIGHT_PURPLE}").strip()
    print(END, end="")
    
    # Validate IP
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print_color("❌ Invalid IP address.", RED, True)
        return
    
    print_color("\n🔍 Gathering intelligence from multiple sources...", CYAN, True)
    time.sleep(1)
    
    results = {}
    
    try:
        # Source 1: ip-api.com
        response1 = requests.get(f'http://ip-api.com/json/{ip}', timeout=10)
        if response1.status_code == 200:
            data1 = response1.json()
            if data1.get('status') == 'success':
                results['ip_api'] = data1
        
        # Source 2: ipinfo.io (more detailed)
        response2 = requests.get(f'https://ipinfo.io/{ip}/json', timeout=10)
        if response2.status_code == 200:
            results['ipinfo'] = response2.json()
        
        # Source 3: Check for VPN/Proxy
        response3 = requests.get(f'https://vpnapi.io/api/{ip}?key=demo', timeout=10)
        if response3.status_code == 200:
            results['vpn_check'] = response3.json()
        
        print_color("\n✅ Data collected successfully!", GREEN, True)
        
        # Display combined results
        print_color("═" * 50, NEON_PURPLE, True)
        
        # Basic info from ip-api
        if 'ip_api' in results:
            data = results['ip_api']
            info = [
                f"{NEON_PURPLE}┌────────────────────────────────────────────────────┐{END}",
                f"{BRIGHT_PURPLE}│              IP GEOLOCATION DATA                   │{END}",
                f"{NEON_PURPLE}├────────────────────────────────────────────────────┤{END}",
                f"{LIGHT_PURPLE}│  IP:           {CYAN}{data.get('query', ip):<35}{END}│",
                f"{LIGHT_PURPLE}│  Country:      {CYAN}{data.get('country', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  Region:       {CYAN}{data.get('regionName', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  City:         {CYAN}{data.get('city', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  ISP:          {CYAN}{data.get('isp', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  Organization: {CYAN}{data.get('org', 'N/A'):<35}{END}│",
                f"{LIGHT_PURPLE}│  ASN:          {CYAN}{data.get('as', 'N/A'):<35}{END}│",
            ]
            
            # Add VPN detection
            if 'vpn_check' in results:
                vpn_data = results['vpn_check']
                security = vpn_data.get('security', {})
                vpn_status = "Yes" if security.get('vpn') else "No"
                proxy_status = "Yes" if security.get('proxy') else "No"
                tor_status = "Yes" if security.get('tor') else "No"
                
                info.append(f"{LIGHT_PURPLE}│  VPN:          {CYAN}{vpn_status:<35}{END}│")
                info.append(f"{LIGHT_PURPLE}│  Proxy:        {CYAN}{proxy_status:<35}{END}│")
                info.append(f"{LIGHT_PURPLE}│  TOR:          {CYAN}{tor_status:<35}{END}│")
            
            info.append(f"{NEON_PURPLE}└────────────────────────────────────────────────────┘{END}")
            
            # Add map link if coordinates available
            if data.get('lat') and data.get('lon'):
                map_link = f"\n{BRIGHT_PURPLE}📍 Map: {CYAN}https://www.google.com/maps?q={data['lat']},{data['lon']}{END}"
                info.append(center_text(map_link))
            
            print("\n".join(info))
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"enhanced_ip_lookup_{timestamp}.json"
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        
        print_color(f"\n💾 Full data saved to: {filename}", GREEN, True)
        
    except Exception as e:
        print_color(f"❌ Error: {str(e)}", RED, True)

# ==================== NETWORK SCANNER ====================
def network_scanner():
    """Scan local network for devices"""
    print_color("\n" + "─" * 60, NEON_PURPLE, True)
    print_color("📡 NETWORK SCANNER", BRIGHT_PURPLE, True)
    print_color("─" * 60, NEON_PURPLE, True)
    
    print_color("\n🔍 Detecting local network...", CYAN, True)
    
    try:
        # Get local IP
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        print_color(f"\n🏠 Your IP: {local_ip}", BRIGHT_PURPLE, True)
        
        # Extract network prefix
        ip_parts = local_ip.split('.')
        network_prefix = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}."
        
        print_color(f"\n🌐 Scanning network: {network_prefix}1-254", CYAN, True)
        print_color("This may take a moment...", YELLOW, True)
        
        found_devices = []
        
        def scan_ip(ip):
            try:
                socket.setdefaulttimeout(0.5)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((ip, 80))
                s.close()
                if result == 0:
                    try:
                        hostname = socket.gethostbyaddr(ip)[0]
                    except:
                        hostname = "Unknown"
                    return (ip, hostname)
            except:
                pass
            return None
        
        # Scan first 20 IPs for demonstration
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            futures = []
            for i in range(1, 21):  # Scan first 20 IPs
                ip = f"{network_prefix}{i}"
                futures.append(executor.submit(scan_ip, ip))
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    found_devices.append(result)
        
        if found_devices:
            print_color(f"\n✅ Found {len(found_devices)} device(s):", GREEN, True)
            print_color("═" * 50, NEON_PURPLE, True)
            
            for ip, hostname in found_devices:
                print_color(f"📍 {ip} - {hostname}", LIGHT_PURPLE, True)
        else:
            print_color("❌ No devices found.", RED, True)
            
    except Exception as e:
        print_color(f"❌ Error: {str(e)}", RED, True)

# ==================== DOMAIN WHOIS LOOKUP ====================
def domain_whois_lookup():
    """Perform WHOIS lookup on domain"""
    print_color("\n" + "─" * 60, NEON_PURPLE, True)
    print_color("🔍 DOMAIN WHOIS LOOKUP", BRIGHT_PURPLE, True)
    print_color("─" * 60, NEON_PURPLE, True)
    
    domain = input(f"\n{LIGHT_PURPLE}Enter Domain (example.com): {BRIGHT_PURPLE}").strip().lower()
    print(END, end="")
    
    if not domain or '.' not in domain:
        print_color("❌ Invalid domain format.", RED, True)
        return
    
    print_color(f"\n🔍 Querying WHOIS for {domain}...", CYAN, True)
    
    try:
        w = whois.whois(domain)
        
        if w.domain_name:
            print_color("\n✅ WHOIS Information Found!", GREEN, True)
            print_color("═" * 50, NEON_PURPLE, True)
            
            info_lines = [
                f"{NEON_PURPLE}┌────────────────────────────────────────────────────┐{END}",
                f"{BRIGHT_PURPLE}│              DOMAIN WHOIS DATA                     │{END}",
                f"{NEON_PURPLE}├────────────────────────────────────────────────────┤{END}",
                f"{LIGHT_PURPLE}│  Domain:       {CYAN}{w.domain_name or 'N/A':<35}{END}│",
            ]
            
            if w.registrar:
                info_lines.append(f"{LIGHT_PURPLE}│  Registrar:    {CYAN}{w.registrar:<35}{END}│")
            
            if w.creation_date:
                creation = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
                info_lines.append(f"{LIGHT_PURPLE}│  Created:      {CYAN}{str(creation):<35}{END}│")
            
            if w.expiration_date:
                expiry = w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date
                info_lines.append(f"{LIGHT_PURPLE}│  Expires:      {CYAN}{str(expiry):<35}{END}│")
            
            if w.name_servers:
                ns = w.name_servers[0] if isinstance(w.name_servers, list) else w.name_servers
                info_lines.append(f"{LIGHT_PURPLE}│  Name Server:  {CYAN}{ns:<35}{END}│")
            
            info_lines.append(f"{NEON_PURPLE}└────────────────────────────────────────────────────┘{END}")
            
            print("\n".join(info_lines))
            
            # Save results
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"whois_{domain}_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump(w, default=str, indent=2)
            
            print_color(f"\n💾 WHOIS data saved to: {filename}", GREEN, True)
        else:
            print_color("❌ Domain not found or WHOIS lookup failed.", RED, True)
            
    except Exception as e:
        print_color(f"❌ Error: {str(e)}", RED, True)

# ==================== EMAIL VERIFICATION ====================
def email_verification():
    """Verify email address and check for breaches"""
    print_color("\n" + "─" * 60, NEON_PURPLE, True)
    print_color("📧 EMAIL VERIFICATION & BREACH CHECK", BRIGHT_PURPLE, True)
    print_color("─" * 60, NEON_PURPLE, True)
    
    email = input(f"\n{LIGHT_PURPLE}Enter Email Address: {BRIGHT_PURPLE}").strip().lower()
    print(END, end="")
    
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print_color("❌ Invalid email format.", RED, True)
        return
    
    print_color(f"\n🔍 Analyzing {email}...", CYAN, True)
    
    try:
        # Check email format and extract domain
        domain = email.split('@')[1]
        
        # Check domain MX records
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            mx_servers = [str(mx.exchange) for mx in mx_records]
            mx_valid = True
        except:
            mx_servers = ["No MX records found"]
            mx_valid = False
        
        print_color("\n✅ Email Analysis Complete!", GREEN, True)
        print_color("═" * 50, NEON_PURPLE, True)
        
        info_lines = [
            f"{NEON_PURPLE}┌────────────────────────────────────────────────────┐{END}",
            f"{BRIGHT_PURPLE}│              EMAIL ANALYSIS                        │{END}",
            f"{NEON_PURPLE}├────────────────────────────────────────────────────┤{END}",
            f"{LIGHT_PURPLE}│  Email:        {CYAN}{email:<35}{END}│",
            f"{LIGHT_PURPLE}│  Domain:       {CYAN}{domain:<35}{END}│",
            f"{LIGHT_PURPLE}│  MX Valid:     {CYAN}{'Yes' if mx_valid else 'No':<35}{END}│",
        ]
        
        if mx_servers:
            info_lines.append(f"{LIGHT_PURPLE}│  MX Server:    {CYAN}{mx_servers[0]:<35}{END}│")
        
        # Note about breach checking
        info_lines.append(f"{LIGHT_PURPLE}│  Breach Check: {CYAN}{'API Key Required':<35}{END}│")
        
        info_lines.append(f"{NEON_PURPLE}└────────────────────────────────────────────────────┘{END}")
        
        print("\n".join(info_lines))
        
        print_color("\nℹ️  Note: Full breach checking requires HaveIBeenPwned API key", YELLOW, True)
        
    except Exception as e:
        print_color(f"❌ Error: {str(e)}", RED, True)

# ==================== MAIN MENU ====================
def display_main_menu():
    print_color("\n" + "═" * 60, NEON_PURPLE, True)
    print_color(" MAIN MENU - LUNAR v2", BRIGHT_PURPLE, True)
    print_color("═" * 60, NEON_PURPLE, True)
    
    menu_options = [
        "1. 📱 Discord User Lookup (Public Info)",
        "2. 🔗 Discord Webhook Analyzer",
        "3. 🌐 Enhanced IP Geolocation",
        "4. 📡 Network Device Scanner",
        "5. 🔍 Domain WHOIS Lookup",
        "6. 📧 Email Verification & Analysis",
        "7. 📞 Phone Number Analysis",
        "8. 🔐 Password Security Check",
        "9. 🕵️ Username Search (Multi-Platform)",
        "10. 🗺️ Port Scanner",
        "11. 📊 DNS Records Lookup",
        "12. 🚀 Social Media Finder",
        "0. ❌ Exit"
    ]
    
    for option in menu_options:
        print_color(option, LIGHT_PURPLE, True)

def get_centered_input(prompt, color=LIGHT_PURPLE, input_color=BRIGHT_PURPLE):
    clean_prompt = ''
    i = 0
    while i < len(prompt):
        if prompt[i:i+2] == '\033[':
            i = prompt.find('m', i) + 1
        else:
            clean_prompt += prompt[i]
            i += 1
    
    padding = (TERMINAL_WIDTH - len(clean_prompt) - 2) // 2
    print(' ' * padding + f"{color}{prompt}{input_color}", end='')
    user_input = input()
    print(END, end='')
    return user_input.strip()

def main():
    if os.name == 'nt':
        os.system('title 🌙 Lunar v2 - Advanced OSINT Tool - By PuffyLive')
    
    while True:
        print_banner()
        display_main_menu()
        
        choice = get_centered_input("\nSelect option [0-12]: ")
        
        if choice == '0':
            print_color("\n👋 Thank you for using Lunar v2!", BRIGHT_PURPLE, True)
            time.sleep(1)
            break
        
        elif choice == '1':
            discord_user_lookup()
        elif choice == '2':
            discord_webhook_analyzer()
        elif choice == '3':
            enhanced_ip_lookup()
        elif choice == '4':
            network_scanner()
        elif choice == '5':
            domain_whois_lookup()
        elif choice == '6':
            email_verification()
        elif choice == '7':
            print_color("\n📞 Phone Number Analysis - Coming in v2.1", YELLOW, True)
        elif choice == '8':
            print_color("\n🔐 Password Security Check - Coming in v2.1", YELLOW, True)
        elif choice == '9':
            print_color("\n🕵️ Username Search - Coming in v2.1", YELLOW, True)
        elif choice == '10':
            print_color("\n🗺️ Port Scanner - Coming in v2.1", YELLOW, True)
        elif choice == '11':
            print_color("\n📊 DNS Records Lookup - Coming in v2.1", YELLOW, True)
        elif choice == '12':
            print_color("\n🚀 Social Media Finder - Coming in v2.1", YELLOW, True)
        else:
            print_color("\n❌ Invalid selection. Please try again.", RED, True)
        
        input(f"\n{LIGHT_PURPLE}Press Enter to continue...{END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_color("\n\n⚠️ Program terminated by user", RED, True)
        sys.exit(0)
    except Exception as e:
        print_color(f"\n❌ Unexpected error: {e}", RED, True)
        sys.exit(1)
