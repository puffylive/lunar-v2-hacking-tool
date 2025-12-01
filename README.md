# 🌙 Lunar v2.1 - Complete OSINT Suite

<div align="center">

![Lunar v2.1 Banner](https://via.placeholder.com/800x200/5A189A/FFFFFF?text=LUNAR+v2.1+COMPLETE+OSINT+SUITE)

**Advanced Open Source Intelligence & Network Analysis Tool**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-9D4EDD.svg?style=for-the-badge)](LICENSE)
[![Windows](https://img.shields.io/badge/Windows-10|11-0078D6.svg?style=for-the-badge&logo=windows&logoColor=white)](https://windows.com)
[![Version](https://img.shields.io/badge/Version-2.1.0-7B2CBF.svg?style=for-the-badge)]()

</div>

## ✨ Overview

**Lunar v2.1** is a comprehensive OSINT (Open Source Intelligence) tool designed for security professionals, network administrators, and ethical hackers. Featuring a sleek purple-themed terminal interface, it provides 12 powerful modules for network analysis, intelligence gathering, and security auditing - all in one unified tool.

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/puffylive/lunar-osint.git
cd lunar-osint

# Install dependencies
pip install -r requirements.txt

# Or install manually
pip install requests colorama dnspython
```

### Basic Usage

```bash
# Run Lunar v2.1
python lunar_v2.1.py
```

## 📋 Complete Feature List

### 1. 📱 **Discord Resolver Simulation**
- Educational simulation of Discord IP resolution
- Generates realistic but fake data for training
- Includes legal disclaimers and ethical warnings

### 2. 🌐 **Enhanced IP Lookup with VPN Detection**
- Multi-source IP geolocation (ip-api.com, ipinfo.io)
- VPN/Proxy detection algorithms
- Threat intelligence integration
- Export to JSON format

### 3. 📡 **Advanced Network Scanner**
- Local network device discovery
- Multi-threaded scanning (50+ concurrent threads)
- Service detection on common ports
- Results export to text files
- Live progress indicators

### 4. 📞 **Phone Number Intelligence**
- Country code detection
- Carrier lookup (US numbers)
- Spam risk assessment
- Format validation and cleaning

### 5. 🔐 **Password Security Analyzer**
- Password strength scoring (0-8 scale)
- HaveIBeenPwned breach checking (k-anonymity)
- Security feedback and recommendations
- Strong password generator
- Pattern detection (sequential, common words)

### 6. 🕵️ **Username Cross-Platform Search**
- Checks 15+ platforms simultaneously
- Concurrent multi-threading
- Results categorization by platform type
- Export to organized text files
- Live progress tracking

### 7. 🗺️ **Advanced Port Scanner**
- Scan 30+ common ports
- Service identification
- Security risk assessment
- Risky port warnings
- Export to formatted reports

### 8. 📊 **DNS Records Analyzer**
- Complete DNS record lookup (A, AAAA, MX, NS, TXT, CNAME, SOA)
- Results organization and display
- JSON export capability
- Domain verification

### 9. 🚀 **Social Media Profile Finder**
- Check 20+ social media platforms
- Profile categorization (Social, Gaming, Creative, etc.)
- Direct profile links
- Comprehensive results export
- Multi-threaded checking

### 10. 📧 **Email Breach Checker** 
- *Requires external API key*
- Integration guide provided
- Future implementation ready

### 11. 🌐 **WHOIS Domain Lookup**
- *Requires python-whois module*
- Installation instructions included
- Registration data retrieval

### 12. 🛡️ **Vulnerability Scanner**
- *Coming in v2.2*
- Planned feature placeholder

## 🛠️ Installation Guide

### Prerequisites

- **Python 3.8+** (Download from [python.org](https://python.org))
- **Windows 10/11** or **Linux/macOS** with terminal
- **Internet connection** (for API calls and lookups)
- **Administrator/root privileges** (for network scanning)

### Step-by-Step Installation

1. **Download Python** (if not installed):
   ```bash
   # Verify Python installation
   python --version
   # Should return: Python 3.8+
   ```

2. **Install Required Packages**:
   ```bash
   # Minimum required packages
   pip install requests colorama
   
   # For full functionality
   pip install requests colorama dnspython ipaddress
   
   # Optional for future features
   pip install python-whois phonenumbers beautifulsoup4
   ```

3. **Download Lunar v2.1**:
   ```bash
   # Method 1: Clone from GitHub
   git clone https://github.com/puffylive/lunar-osint.git
   
   # Method 2: Download zip file
   # Extract and navigate to folder
   ```

4. **Run the Tool**:
   ```bash
   cd lunar-osint
   python lunar_v2.1.py
   ```

## 📖 Detailed Usage Guide

### Module 1: Discord Resolver Simulation

**Purpose**: Educational tool for understanding how Discord resolvers work (simulated data only)

```bash
Select option [0-12]: 1
Enter Discord User ID: 123456789012345678
```

**Output**:
- Simulated IP address
- Fake geolocation data
- Educational warnings
- Legal disclaimers

### Module 2: Enhanced IP Lookup

**Purpose**: Comprehensive IP intelligence with threat assessment

```bash
Select option [0-12]: 2
Enter IP Address: 8.8.8.8
```

**Output**:
- Geolocation (Country, City, Region)
- ISP and Organization
- VPN/Proxy detection
- Threat score (if available)
- Google Maps link
- JSON export

### Module 3: Network Scanner

**Purpose**: Discover devices on your local network

```bash
Select option [0-12]: 3
```

**Features**:
- Automatic network detection
- Multi-threaded scanning (254 IPs in 1-2 minutes)
- Service detection on common ports
- Hostname resolution
- Progress bar visualization
- Text file export

### Module 4: Phone Number Analysis

**Purpose**: Validate and analyze phone numbers

```bash
Select option [0-12]: 4
Enter Phone Number (with country code): +14155552671
```

**Analysis Includes**:
- Country detection
- Carrier lookup (US numbers)
- Format validation
- Spam risk assessment
- Number cleaning

### Module 5: Password Security Analyzer

**Purpose**: Check password strength and breach status

```bash
Select option [0-12]: 5
Enter Password to Check: ********
```

**Checks Performed**:
- Length assessment
- Character complexity
- Common pattern detection
- HaveIBeenPwned breach check
- Strength scoring (0-8)
- Secure password suggestions

### Module 6: Username Search

**Purpose**: Check username availability across platforms

```bash
Select option [0-12]: 6
Enter Username: puffylive
```

**Platforms Checked**:
- GitHub, Twitter, Instagram, Reddit
- Steam, Twitch, YouTube, TikTok
- Discord, Spotify, Pinterest, Tumblr

**Output**:
- Available platforms list
- Results categorization
- Text file export
- Direct links

### Module 7: Port Scanner

**Purpose**: Scan target for open ports and services

```bash
Select option [0-12]: 7
Enter Target IP or Hostname: 192.168.1.1
```

**Ports Scanned**:
- Common ports (21, 22, 80, 443, etc.)
- Service identification
- Security risk assessment
- Risky port warnings

### Module 8: DNS Records Lookup

**Purpose**: Retrieve DNS information for domains

```bash
Select option [0-12]: 8
Enter Domain (example.com): google.com
```

**Record Types**:
- A (IPv4 addresses)
- AAAA (IPv6 addresses)
- MX (Mail servers)
- NS (Name servers)
- TXT (Text records)
- CNAME (Canonical names)
- SOA (Start of authority)

### Module 9: Social Media Finder

**Purpose**: Locate social media profiles by username

```bash
Select option [0-12]: 9
Enter Username: puffylive
```

**Platform Categories**:
- Social Networks (Facebook, Twitter, Instagram)
- Gaming/Streaming (Twitch, Discord, Steam)
- Creative (GitHub, Behance, DeviantArt)
- Video (YouTube, TikTok)
- Other (Reddit, Pinterest, Spotify)

## ⚙️ Technical Architecture

### Multi-threading Implementation
Lunar v2.1 uses concurrent futures for parallel processing:
- **Network Scanner**: 50+ concurrent threads
- **Username Search**: 10+ concurrent threads
- **Port Scanner**: 20+ concurrent threads
- **Social Media Finder**: 15+ concurrent threads

### Error Handling
- Comprehensive try-catch blocks
- Connection timeout management
- Graceful degradation
- User-friendly error messages

### Data Export Formats
- **JSON**: For structured data (IP lookup, DNS records)
- **TXT**: For human-readable reports
- **Timestamps**: Automatic filename generation

### Color System
- ANSI escape codes for cross-platform compatibility
- Purple theme with 5 gradient levels
- Status-based coloring (Green/Success, Red/Error, Yellow/Warning)

## 📁 File Structure

```
lunar-osint/
├── lunar_v2.1.py          # Main application
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
├── LICENSE               # MIT License
├── screenshots/          # Tool screenshots
│   ├── main-menu.png
│   ├── ip-lookup.png
│   └── network-scan.png
├── examples/             # Example output files
│   ├── ip_lookup_example.json
│   ├── network_scan_example.txt
│   └── username_search_example.txt
└── docs/                 # Additional documentation
    ├── api-integration.md
    └── legal-guidelines.md
```

## 🔧 Advanced Configuration

### Custom API Keys
For enhanced functionality, you can add API keys:

1. **AbuseIPDB API** (for threat scores):
   ```python
   # In the enhanced_ip_lookup function
   headers = {'Key': 'YOUR_API_KEY_HERE', 'Accept': 'application/json'}
   ```

2. **HaveIBeenPwned API** (for email checking):
   ```python
   # Requires paid API key for email checking
   # Free tier available for password checking
   ```

### Network Settings
Adjust scan parameters in the code:
```python
# Network Scanner settings
MAX_WORKERS = 50          # Concurrent threads
TIMEOUT = 0.3            # Socket timeout in seconds
PORTS_TO_CHECK = [80, 443, 22, 21]  # Custom port list
```

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **"ModuleNotFoundError"** | Run `pip install -r requirements.txt` |
| **Network scan too slow** | Reduce MAX_WORKERS or increase TIMEOUT |
| **Colors not displaying** | Ensure terminal supports ANSI colors |
| **API rate limiting** | Wait 1-2 minutes between requests |
| **Permission denied** | Run as administrator (for network scans) |
| **DNS resolution fails** | Install dnspython: `pip install dnspython` |

### Debug Mode
Enable verbose logging by modifying the code:
```python
# Add at beginning of functions
DEBUG = True
if DEBUG:
    print(f"[DEBUG] Starting {function_name}...")
```

## ⚖️ Legal & Ethical Use

### Important Disclaimers

1. **Educational Purpose Only**: Lunar v2.1 is designed for educational and authorized security testing only.

2. **Legal Compliance**: Always ensure you have proper authorization before:
   - Scanning networks you don't own
   - Testing systems without permission
   - Collecting data from third parties

3. **Discord Resolver Simulation**: The Discord module generates **fake data only**. Real Discord IP resolution violates Discord's Terms of Service and may be illegal.

4. **Privacy Respect**: Do not use this tool to:
   - Harass or stalk individuals
   - Access unauthorized systems
   - Collect personal data without consent

### Authorized Use Cases
- ✅ Security auditing of your own networks
- ✅ Educational demonstrations
- ✅ Authorized penetration testing
- ✅ Personal security assessments
- ✅ Research and development

### Prohibited Use Cases
- ❌ Unauthorized network scanning
- ❌ Harassment or stalking
- ❌ Commercial exploitation without modification
- ❌ Illegal surveillance
- ❌ Violating terms of service

## 📄 License

**MIT License**

Copyright (c) 2024 PuffyLive

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 👤 Author

**PuffyLive** - OSINT Tool Developer
- Tool: Lunar v2.1 Complete OSINT Suite
- Version: 2.1.0
- Release Date: December 2024

## 🙏 Acknowledgments

- **ip-api.com** for free geolocation API
- **HaveIBeenPwned** for password breach checking
- **Python community** for excellent libraries
- **Open source contributors** for inspiration

## 🔗 Useful Links

- [Python Official Website](https://python.org)
- [MIT License Information](https://opensource.org/licenses/MIT)
- [OSINT Framework](https://osintframework.com)
- [Security Best Practices](https://owasp.org)

## ⭐ Support

If you find Lunar v2.1 useful:
1. ⭐ **Star the repository** on GitHub
2. 🐛 **Report issues** and bugs
3. 🔄 **Share** with other security professionals
4. 💡 **Suggest features** for future versions

---

<div align="center">

**🌙 "See the unseen, know the unknown"**

*Lunar v2.1 - Complete OSINT Suite*

</div>

---

### Quick Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `python lunar_v2.1.py` | Launch Lunar v2.1 | - |
| `pip install dnspython` | Install DNS module | Required for Module 8 |
| `Ctrl + C` | Exit program | Any time during operation |
| `--help` | Show help (future) | Planned for v2.2 |
