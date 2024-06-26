
<div align="center">
<h1 align="center">
<img src="https://github.com/DannnyzZ/OSFortify/blob/main/OSFortify_logo_wide.jpg" >
<br>
</h1>
<p align="center">
</p>
 
<p align="center">
  <img src="https://img.shields.io/badge/PowerShell-5391FE.svg?style&logo=PowerShell&logoColor=white" alt="PowerShell" />
  <img src="https://img.shields.io/badge/Batch-Script-4EAA25.svg?style=flat&logo=Windows%20Terminal&logoColor=white" alt="Batch Script" />
  <img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/GitHub-007ACC.svg?style=flat&logo=GitHub&logoColor=white" alt="GitHub" />
  <img src="https://img.shields.io/badge/OS%20Hardening-FFA500.svg" alt="OS%20Hardening" />
  <img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
  <img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
  <img src="https://img.shields.io/badge/GPO%20%26%20Security%20Baseline-red.svg?style=flat&logo=Security%20Shield&logoColor=white" alt="GPO Security Baseline" />
</p>


![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-4825-25A9E0.svg?style=flat)
![Code Size](https://img.shields.io/badge/Code%20Size-0.5%20MB-25A9E0.svg?style=flat)
</div>

---


## 📒 Table of Contents
- [📍 Overview](#-overview)
- [⚙️ Features](#️-features)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✔️ Prerequisites](#️-prerequisites)
  - [💻 Installation](#-installation)
  - [🎮 Using OSFortify](#-using-OSFortify)
  - [⚠️ Warning](#%EF%B8%8F-warning)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)
- [🗃️ Changelog](#%EF%B8%8F-changelog)


---


## 📍 Overview

OSFortify is a sophisticated terminal-based utility designed to enhance system security, streamline operating system hardening, and facilitate efficient system administration. With a focus on cybersecurity, system integrity, and user-friendly interactions, OSFortify empowers users to manage various aspects of their system's services, features, and ports through a secure and organized interface.

The primary **purpose** of OSFortify is to provide an advanced yet accessible tool for users to bolster their system's security posture, elevate operating system hardening, and seamlessly administer critical system functions. By enabling users to interact with their system through a curated selection of options, OSFortify bridges the gap between cybersecurity and user experience.

OSFortify brings robust control to your system's **services, features, and ports**. It allows real-time status checks, seamless activation or deactivation during boot, and dynamic adjustments on-the-fly. 

With OSFortify, you can finely manage your system's components and bolster security of end-device by implementing comprehensive built-in security baseline, consisting of over 950 unique GPO policies.


---

## ⚙️ Features

| Feature                | Description                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **⚡️ Efficient Admininistration** | The program streamlines system administration by offering a user-friendly interface to manage services and features. This enhances operational efficiency by minimizing manual command-line interactions and simplifying routine tasks. |
| **🧩 Modularity** | The program's design demonstrates modularity by organizing functionalities into distinct modules and classes. Each module focuses on specific aspects of system security, administration, and hardening, enhancing maintainability and reusability. |
| **✔️ Secure Execution** | OSFortify emphasizes secure execution of commands and scripts, crucial for system integrity and cybersecurity. It ensures proper progress tracking during script execution and safeguards against unauthorized access. |
| **🔐 Enhanced Security** | OSFortify contributes to enhanced security by enabling users to selectively manage services, features, and ports. This granular control aids in system hardening, mitigating potential vulnerabilities, and bolstering overall cybersecurity measures. |
| **🔌 Flexibility** | The program's dynamic configuration switching and adaptable options provide flexibility to tailor system settings to specific needs. This accommodates various security profiles and allows users to optimize their systems for different scenarios. |
| **📶 Insightful Data** | OSFortify offers users valuable insights into their system's architecture through detailed system information retrieval. This aids decision-making, system understanding, and helps identify potential areas for further optimization. |
| **📝 Log controler** | OSFortify utilizes the Event Viewer to extract the most important logs across various categories, ensuring comprehensive visibility into your system's security posture. |
| **📕 Advanced Security Baseline** | The software goes beyond the standard Microsoft Security Baseline Toolkit v. 1.0, actively modifying 952 Microsoft GPO policies to provide enhanced security measures. This translates to a significant increase of 635 more policies compared to the Microsoft baseline. |
| **🔗 Comprehensive Functionality** | OSFortify encompasses a diverse array of essential services, features, and ports, collectively enhancing system security, hardening, and administration. These elements form a critical foundation for a robust and secure computing environment, fortifying against potential threats and vulnerabilities. |

---

## 🧩 Modules

*Services and Features* - OSFortify encompasses a comprehensive range of essential services and features, including guest user account management, FTP control, oversight of Windows Media Player, and management of USB ports. These functionalities contribute significantly to system security by offering control over potential entry points, data transfers, and media-related threats.

<details closed><summary>Services</summary>

| Service | Details |
| --- | --- |
| Windows Defender | Protocol: N/A. Function: Antivirus and antimalware tool. Use: System protection. Security: Reliable; ensure regular updates for best protection. |
| Windows Firewall | Protocol: N/A. Function: Filters incoming/outgoing network traffic. Use: Network security. Security: Essential for system protection; configure rules appropriately. |
| Windows Update | Protocol: N/A. Function: Provides system and software updates. Use: System maintenance. Security: Critical for patching vulnerabilities; keep automatic updates on. |
| Windows Remote Registry | Protocol: N/A. Function: Access to system registry remotely. Use: System administration. Security: Risky; disable unless specifically needed. |
| Windows Remote Management | Protocol: TCP. Function: Remote administration tool. Use: System administration. Security: Secure endpoints; restrict access. |
| Windows Management Instrumentation (WMI) | Protocol: N/A. Function: Management infrastructure for Windows. Use: System monitoring and management. Security: Potential target; ensure proper configuration. |
| Remote Desktop Protocol (RDP) | Protocol: TCP/UDP. Function: Remote desktop access. Use: Remote system management. Security: High-risk; enable Network Level Authentication and restrict access. |
| Windows Error Reporting | Protocol: N/A. Function: Sends error reports to Microsoft. Use: Debugging. Security: Minor risk; sensitive info might be sent. |
| Windows Remote Assistance | Protocol: N/A. Function: Remote system help and support. Use: Tech support. Security: Secure sessions; only use with trusted parties. |
| Windows Fax and Scan | Protocol: N/A. Function: Send/receive faxes; scan documents. Use: Office tasks. Security: Ensure secure configurations for fax transmissions. |
| Internet Printing Client | Protocol: N/A. Function: Allows printing over the internet. Use: Remote printing. Security: Ensure secure network and printer configurations. |
| Universal Plug and Play (UPnP) | Protocol: N/A. Function: Automatic device discovery and configuration. Use: Device connectivity. Security: Known vulnerabilities; disable unless needed. |
| Bluetooth | Protocol: N/A. Function: Short-range wireless communication. Use: Device pairing. Security: Vulnerable to "bluejacking"; turn off when not in use. |
| Windows Search | Protocol: N/A. Function: Search tool for files and apps. Use: File and application access. Security: Ensure indexing of sensitive data is restricted. |
| Print Spooler | Protocol: N/A. Function: Manages print tasks. Use: Printing tasks. Security: Known vulnerabilities; update regularly and restrict access. |
| Microsoft IIS | Protocol: TCP. Function: Web server software. Use: Hosting web applications. Security: Regularly update and harden configurations. |
| NetBIOS | Protocol: TCP/UDP. Function: Legacy network support. Use: Windows networking. Security: Known vulnerabilities; restrict or disable. |
| Link-Local Multicast Name Resolution (LLMNR) | Protocol: N/A. Function: Resolves single-label domains. Use: Network operations. Security: Vulnerable to spoofing; consider disabling. |
| Server Message Block Version 1 (SMB1) | Protocol: TCP/UDP. Function: File sharing protocol. Use: Network file sharing. Security: Deprecated due to vulnerabilities; disable. |
| Server Message Block Version 2 (SMB2) | Protocol: TCP/UDP. Function: Updated file sharing protocol. Use: Network file sharing. Security: More secure than SMB1; ensure up-to-date configurations. |
| Telnet | Protocol: TCP. Function: Remote command-line access. Use: Remote system administration. Security: Unencrypted; use SSH as a more secure alternative. |

</details>

*Windows Features* - The program covers an array of critical Windows features, including Windows Defender, Windows Firewall, Windows Update, remote management functionalities, and more. By providing control over these features, OSFortify enhances cybersecurity by allowing administrators to fortify defenses, manage remote access, and stay updated against known vulnerabilities.

<details closed><summary>Features</summary>

| Feature | Details |
| --- | --- |
| Guest user account | Protocol: N/A. Function: Provides limited access to a system without a personalized login. Use: Temporary or restricted access. Security: Risky; can be exploited if not properly restricted. |
| File Transfer Protocol (FTP) | Protocol: TCP. Function: Protocol for transferring files over a network. Use: File sharing and download/upload. Security: Unencrypted; use FTPS or SFTP for secure transfers. |
| Windows Media Player | Protocol: N/A. Function: Media player for viewing/hearing media files. Use: Multimedia playback. Security: Vulnerabilities may arise from codecs/plugins; ensure updates. |
| USB ports | Protocol: N/A. Function: Interface for connecting external devices. Use: Data transfer, device charging, peripheral connections. Security: Potential for malicious device connections or data theft; use device controls. |
| User Account Control | Protocol: N/A. Function: Controls the level of access rights a user has on a system. Use: Enhances security by limiting administrative privileges. Security: Essential for protecting against unauthorized system changes or malware execution. |
| Autorun | Protocol: N/A. Function: Automatically runs programs or scripts upon insertion of external media. Use: Automates tasks or installations. Security: Vulnerable to malware; disable for enhanced security. |
| Command Prompt | Protocol: N/A. Function: Command-line interpreter for executing commands and scripts. Use: System administration, troubleshooting, scripting. Security: High privileges; potential for misuse if not restricted. |
| PowerShell | Protocol: N/A. Function: Powerful command-line shell and scripting language. Use: System administration, automation, scripting. Security: High privileges; monitor usage and restrict access to trusted users. |

</details>

*Ports* - OSFortify encompasses an extensive list of important ports, such as SSH (Port 22), HTTPS (Port 443), RDP (Port 3389), and many more. These ports serve as critical communication channels, and their proper management through OSFortify enhances cybersecurity by preventing unauthorized access, securing data transfers, and protecting against potential exploits.

<details closed><summary>Ports</summary>

| Port | Details |
| --- | --- |
| Port 7 - Echo | *Protocol*: TCP/UDP. *Function*: Returns received data (echoes back). *Use*: Network testing. *Security*: Risky; often disabled or blocked due to potential exploits. |
| Port 20 - File Transfer Protocol (FTP) | Protocol: TCP. Function: Transfers files (data channel). Use: File sharing. Security: Use with caution; encrypted alternatives recommended. |
| Port 21 - File Transfer Protocol Control | Protocol: TCP. Function: Command channel for FTP. Use: File sharing control. Security: Use with caution; encrypted alternatives recommended. |
| Port 22 - Secure Shell (SSH) | Protocol: TCP. Function: Secure remote login and command execution. Use: Secure system management. Security: Highly secure; ensure strong keys and passwords. |
| Port 23 - Telnet | Protocol: TCP. Function: Remote login (plaintext). Use: Remote system management. Security: Risky; use SSH instead due to lack of encryption. |
| Port 25 - Simple Mail Transfer Protocol (SMTP) | Protocol: TCP. Function: Email transmission. Use: Mail servers. Security: Vulnerable to spam and misuse; ensure proper configurations. |
| Port 37 - Time | Protocol: TCP/UDP. Function: Provides system time. Use: Synchronizing system clocks. Security: Generally low risk; ensure only trusted sources are used. |
| Port 53 - Domain Name System (DNS) | Protocol: TCP/UDP. Function: Translates domain names to IP addresses. Use: Web browsing, app connectivity. Security: Risk of DNS spoofing; use DNSSEC where possible. |
| Port 69 - Trivial File Transfer Protocol (TFTP) | Protocol: UDP. Function: File transfers (simpler than FTP). Use: Often for network devices, firmware updates. Security: No authentication; use in secure environments only. |
| Port 80 - Hyper Text Transfer Protocol (HTTP) | Protocol: TCP. Function: Transfers web pages. Use: Web browsing. Security: Unencrypted; HTTPS (Port 443) is more secure. |
| Port 110 - Post Office Protocol 3 (POP3) | Protocol: TCP. Function: Retrieves email from a mail server. Use: Email clients. Security: Unencrypted; secure alternatives available (e.g., POP3S). |
| Port 111 - Remote Procedure Calls (RPC) | Protocol: TCP/UDP. Function: Executes remote commands. Use: Distributed systems. Security: Vulnerable if not properly secured; risk of DDoS and unauthorized access. |
| Port 123 - Network Time Protocol (NTP) | Protocol: UDP. Function: Synchronizes system clocks. Use: Clock synchronization. Security: Exploitable if misconfigured; use authenticated mode. |
| Port 135 - Microsoft Remote Procedure Call (MSRPC) | Protocol: TCP. Function: Executes remote procedures. Use: Microsoft distributed applications. Security: Risky; should be firewalled in untrusted environments. |
| Port 137 - Server Message Block (SMB) | Protocol: TCP/UDP. Function: Provides shared access to files, printers, etc. Use: File and printer sharing in Windows networks. Security: Vulnerable to various attacks; secure configurations and recent versions are essential. |
| Port 139 - Server Message Block/NetBIOS Session Service (SMB/NetBIOS-SSN) | Protocol: TCP. Function: Facilitates file, printer, and other shared resource access. Use: Windows networking. Security: Risk of unauthorized access; should be firewalled in untrusted environments. |
| Port 143 - Internet Message Access Protocol (IMAP) | Protocol: TCP. Function: Accesses email messages on a remote server. Use: Email clients. Security: Unencrypted; secure version IMAPS (Port 993) recommended. |
| Port 161 - Simple Network Management Protocol (SNMP) | Protocol: UDP. Function: Monitors and manages network devices. Use: Network management. Security: Versions prior to SNMPv3 lack encryption and are insecure. |
| Port 162 - Simple Network Management Protocol Trap (SNMP Trap) | Protocol: UDP. Function: Notification from network devices about specific conditions. Use: Network management. Security: Ensure filtering and proper configurations to avoid misuse. |
| Port 389 - Lightweight Directory Access Protocol (LDAP) | Protocol: TCP. Function: Accesses and maintains directory services. Use: Directory operations. Security: Unencrypted; use LDAPS (Port 636) for secure connections. |
| Port 443 - HTTP Secure (HTTPS) | Protocol: TCP. Function: Transfers encrypted web pages. Use: Secure web browsing. Security: Encrypted; ensure valid certificates for authenticity. |
| Port 445 - Microsoft-DS (Directory Services) SMB/Active Directory | Protocol: TCP. Function: Access to shared resources like files and printers. Use: Windows networking and domain services. Security: Potential target for ransomware and other attacks; secure appropriately. |
| Port 636 - Secure Lightweight Directory Access Protocol (SLDAP) | Protocol: TCP. Function: Accesses and maintains encrypted directory services. Use: Directory operations. Security: Encrypted; offers secure alternative to LDAP. |
| Port 993 - Internet Message Access Protocol Secure (IMAPS) | Protocol: TCP. Function: Accesses email messages securely on a remote server. Use: Secure email clients. Security: Encrypted; preferred over IMAP. |
| Port 995 - Post Office Protocol 3 Secure (POP3S) | Protocol: TCP. Function: Secure retrieval of email from a server. Use: Secure email clients. Security: Encrypted; preferred over POP3. |
| Port 989 - FTP over TLS/SSL (FTPS data) | Protocol: TCP. Function: Encrypted data channel for FTP. Use: Secure file sharing. Security: Encrypted; safer than regular FTP. |
| Port 990 - FTP over TLS/SSL (FTPS control) | Protocol: TCP. Function: Command channel for encrypted FTP. Use: Secure file sharing control. Security: Encrypted; safer than regular FTP. |
| Port 1433 - Microsoft SQL Server | Protocol: TCP. Function: SQL Server database access. Use: Database operations. Security: Potential target for attacks; firewall and restrict access. |
| Port 1434 - Microsoft SQL Server Browser Service | Protocol: UDP. Function: Provides info about SQL Server instances. Use: Database operations. Security: Limit exposure; can reveal sensitive info. |
| Port 1723 - Point-to-Point Tunneling Protocol (PPTP) | Protocol: TCP. Function: VPN tunnel creation. Use: VPNs. Security: Vulnerabilities known; consider more secure VPN protocols. |
| Port 1812 - RADIUS Authentication | Protocol: UDP. Function: Remote user authentication. Use: VPNs, networking. Security: Ensure secure configurations and strong encryption. |
| Port 1813 - RADIUS Accounting | Protocol: UDP. Function: Tracks resources usage of remote users. Use: VPNs, networking. Security: Ensure data integrity and confidentiality. |
| Port 3268 - Global Catalog Service | Protocol: TCP. Function: Directory service for AD domains. Use: Microsoft AD. Security: Ensure proper configurations for AD environment. |
| Port 3269 - Secure Global Catalog Service | Protocol: TCP. Function: Directory service for AD domains over SSL. Use: Microsoft AD. Security: Encrypted; ensure valid certificates. |
| Port 3389 - RDP/MS-WBT-server | Protocol: TCP/UDP. Function: Remote desktop access. Use: Remote system management. Security: High-risk; enable Network Level Authentication and restrict access. |
| Port 5060 - SIP (Non-encrypted) | Protocol: TCP/UDP. Function: Initiates/modifies VoIP calls. Use: VoIP services. Security: Unencrypted; risks of eavesdropping. |
| Port 5061 - SIP over TLS (Encrypted) | Protocol: TCP/UDP. Function: Secure VoIP call initiation. Use: Secure VoIP services. Security: Encrypted; preferred over non-encrypted SIP. |
| Port 5190 - AOL | Protocol: TCP. Function: Online services and instant messaging. Use: Communication. Security: Ensure latest software versions; avoid untrusted content. |
| Port 5631 - Symantec pcAnywhere (data) | Protocol: TCP. Function: Remote desktop data transfer. Use: Remote system access. Security: Ensure secure configurations and updates. |
| Port 5632 - Symantec pcAnywhere (status) | Protocol: UDP. Function: Remote desktop status communication. Use: Remote system access. Security: Ensure secure configurations and updates. |
| Port 5800 - VNC over HTTP | Protocol: TCP. Function: Web-based remote desktop access. Use: Remote system management. Security: Use strong passwords and consider tunneling over SSL. |
| Port 5900 - VNC Standalone | Protocol: TCP. Function: Remote desktop access. Use: Remote system management. Security: Risky; use strong passwords and restrict access. |
| Port 8080 - HTTP Proxy | Protocol: TCP. Function: Alternative port for web services. Use: Web applications, proxies. Security: Regularly monitor and restrict to known users. |

</details>

*Event Viewer Module* - OSFortify utilizes the Event Viewer to extract the most important logs across various categories, ensuring comprehensive visibility into your system's security posture.

<details closed><summary>Event Viewer Module</summary>

| Event Viewer Category | Details |
| --- | --- |
| Access Control | Logs related to access control include entries detailing attempts to access resources, such as files, folders, or registry keys, along with information about whether access was granted or denied. |
| Audit and Logging | This category encompasses logs generated by auditing processes, which record events such as changes to system configurations, security policy modifications, or user account creations. |
| Authentication and Authorization | Logs in this category capture authentication attempts (successful or failed), including logon events, user authentication methods, and authorization decisions made by the system. |
| Account Activity | Logs related to account activity track user actions within the system, such as account logins, logouts, password changes, or account lockouts due to multiple failed login attempts. |
| System Integrity | These logs monitor the integrity of system files and configurations, including entries related to system file modifications, changes to critical system settings, or attempts to tamper with system integrity mechanisms. |
| Critical System Events | Logs in this category record critical system events that may indicate potential security breaches or system malfunctions, such as system crashes, hardware failures, or unexpected shutdowns. |
| Other Security Events | This category includes logs for various security-related events that do not fit into the above categories. |

</details>

*Security Baseline Module* - OSFortify leverages LGPO via API to seamlessly implement and manage GPO policies, ensuring efficient and reliable policy enforcement. It also provides the capability to backup and restore GPO configurations, giving you peace of mind knowing that your policies are securely stored and easily recoverable in case of emergencies.
  
<details closed><summary>Security Baseline Module</summary>

| Security Baseline Category | Details |
| --- | --- |
| Audit Policy | Protocol: N/A. Function: Settings that determine which types of security events are recorded in the security log of a Windows system. Use: Governing the auditing of various activities such as logon events, file access, account management, and system events. Security: Essential for monitoring and maintaining system security; configure carefully to balance security needs with performance impact. |
| HKCU | Protocol: N/A. Function: HKEY_CURRENT_USER registry hive containing configuration settings for the currently logged-in user on a Windows system. Use: Storing user-specific settings such as desktop preferences, application settings, and environment variables. Security: Contains sensitive user information; protect from unauthorized access or modification. |
| HKLM | Protocol: N/A. Function: HKEY_LOCAL_MACHINE registry hive containing configuration settings for the local computer. Use: Storing system-wide settings such as hardware configuration, installed software information, and security policies. Security: Critical for system operation; restrict access to trusted administrators to prevent unauthorized changes. |
| Security Template | Protocol: N/A. Function: Predefined set of security configurations and policies for Windows systems to enforce security standards. Use: Applying settings related to user rights, password policies, audit policies, and other security configurations. Security: Ensures consistent security posture across systems; protect templates from unauthorized modification to maintain security integrity. |

> The comprehensive list of policies, along with a comparison to the default state of Windows 10 and the configurations provided by the Microsoft Security Compliance Toolkit version 1.0, is contained within an MS Excel file titled "Default vs Microsoft Compliance Toolkit vs OSFortify - GPO POLICIES.xlsx".

</details>

---

## 🚀 Getting Started

<div align="center">
  <img src="https://github.com/DannnyzZ/OSFortify/assets/119814239/6d2d6b0e-448c-4b7a-94d9-0a29b3c67ad7" alt="gui_screen">
</div>

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:

>  ` Windows 8/10/11`

>  ` Python`

>  ` Python Package Installer `

>  ` Python library: curses `

>  ` Python library: tkinter `

>  ` Internet connection `

### 💻 Installation

1. Install python
```sh
1.	Visit the official Python website: https://www.python.org/downloads/release/python-3117/
2.	Go to the Downloads section and download Python 3.11.7.
* WARNING - due to problems with curses library, OSFortify works only with Python 3.11.7. *
3.	Scroll down to the bottom of the page and select the installer that matches your system architecture (32-bit or 64-bit).
4.	Run the downloaded installer.
5.	In the installer, select the option to add Python to the system PATH, which will make it accessible from the command line.
6.	Make sure that in optional features you choose pip to be installed.
7.	Complete the installation by following the on-screen instructions.
```
2. Install dependencies
```sh
pip install tk windows-curses
```
3. Check version of python and pip:
```sh
python --version && pip --version
```
4. Download osfortify.py from this link:
```sh
https://github.com/DannnyzZ/OSFortify/blob/main/osfortify
```
5. Download OSFortify additional modules (OSFortify_modules.rar) and extract the archive to path:
```sh
C:\Users
```

The full path containing additional modules should look like this:
```sh
C:\Users\OSFortify
```


### 🎮 Using OSFortify

Main module:
1. Launch OSFortify from the PowerShell console:
```sh
python osfortify.py
```

*WARNING! Make sure You provide the correct location of OSFortify.*

Example of use:
```sh
python C:\Users\Danny\Desktop\osfortify.py
```

Secondary modules (Event Viewer, GPO):
1. Inside OSFortify instance, use corresponding button (P: Security policies, V: Event Viewer) to launch dedicated module:
2. Follow the instructions on the screen.
3. Enter the choosen option.
4. Confirm with ENTER.

![OSFortify_GUI_Event_Module](https://github.com/DannnyzZ/OSFortify/assets/119814239/38ddbc2e-3bf7-4d4d-863f-132a4682c262)
  
![OSFortify_GUI_GPO_Module](https://github.com/DannnyzZ/OSFortify/assets/119814239/fa2eeba2-5322-44fa-921f-bc59343f5552)


---


### ⚠️ Warning


**Using OSFortify Safely:**

1. Knowledge is Key: Understand changes' impact on security and stability.

2. Caution and Expertise: Modify with care, avoid vulnerabilities or data loss.

3. Backup Always: Prioritize system backups to ensure recovery options.

4. Authorized Access: Limit OSFortify access to knowledgeable personnel.

5. Controlled Testing: Experiment in safe environments before implementing changes.

6. Secure Scripts: Verify PowerShell scripts before execution.

**Use OSFortify wisely to enhance security while minimizing risks.**


## 🗺 Roadmap


> - [X] ` Task 1: Multiple bug fixes`
> - [X] ` Task 2: New features: tidy and colored output`
> - [X] ` Task 3: *BIG* feature 4: Network analysis: netstat, routing, DNS informations, local hosts, IPv4/IPv6 of device, Gateway, Netmask and many more!`
> - [X] ` Task 4: New features and services: PowerShell, Command prompt, User Account Control, Autorun!`
> - [X] ` Task 5: Module - Event Viewer support`
> - [X] ` Task 6: Module - Security Baseline GPO`

> - [ ] ` Incoming feature 1: Exporting results to PDF file`
> - [ ] ` Incoming feature 2: New services: HDMI, Mini-Jack, DVI, CD-DVD, CTRL+ALT+DEL on login prompt, Trivial File Transfer Protocol`
> - [ ] ` Incoming feature 3: One button evaluation of security state (Risk analysis)`
> - [ ] ` Incoming improvement 1: Improving istallaton process.`
> - [ ] ` Incoming improvement 2: utilizing secedit.exe to apply GPO's.`
> - [ ] ` New services: SSH
> - [ ] ` Incoming feature 4: drivers listing. `
> - [ ] ` Incoming feature 5: updating all software and drivers. `
> - [ ] ` Incoming feature 6: SNMP.`
> - [ ] ` Incoming feature 7: More unencrypted traffic.`

> - [ ] ` Future Update 1: Moving scripts to libraries, improving by that modularity and variety of features`
> - [ ] ` Proof of Concept: IT Auditing via SSH`

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `NEW_FIX`).
```sh
git checkout -b NEW_FIX
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Applied changes.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin NEW_FIX
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

Non-Commercial Use ONLY.

---

## 👏 Acknowledgments

  `ℹ️  Stack Overflow`
   
  `ℹ️  ChatGPT 4.0`
   
  `ℹ️  Readme-ai https://github.com/eli64s/readme-ai`

  `ℹ️  Logo.com https://logo.com`

  `ℹ️  Logo.com https://patorjk.com/software/taag`

  `ℹ️  Microsoft Security Compliance Toolkit 1.0 https://www.microsoft.com/en-us/download/details.aspx?id=55319`

---

## 🗃️ Changelog

OSFortify 1.7
- New section of objects: "Network"
  - Route: Displays the local routing table on the system.
  - Ping: Sends 20 ICMP echo requests to google.com and measures the round-trip time.
  - ARP: Shows the ARP (Address Resolution Protocol) cache, displaying the mapping of IP addresses to MAC addresses on the local network.
  - DNS: Retrieves unique DNS server addresses for both IPv4 and IPv6, then displays them separately.
  - Traceroute: Traces the route that packets take to reach the specified destination (google.com in this case).
  - Routing Table: Provides information about the system's routing table, including destination networks, gateway addresses, and interface indexes.
  - Ipconfig: Extracts information about network adapters, media state, connection-specific DNS suffix, link-local and autoconfigured IPv6 addresses, subnet masks, default gateways, IPv4 addresses, etc.
  - Netstat: Displays active network connections and listening ports, along with the processes using them.
  - Autonomous System Numbers: Retrieves and displays information about the Autonomous System Number (ASN) for a given IP address using the ip-api.com service. Displays IP address, ASN, and AS Name if available.
  - Netstat: Displays active network connections and listening ports, along with the processes using them.

 OSFortify 2.0
- New module - Event Viewer - gives possibilities to retrieve choosen logs from the system.
- New module - GPO Policies - gives possibilities to create backup of existing GPO's, implement OSFortify Security Baseline or restore to previous state of GPO policies.
- New functions:
  - PowerShell configurations
  - Command prompt configurations
  - Autorun
  - User Account Control
  - Saving configuration to file, now has a built-in raport generating function, which will create full raport of results on the designated path. Default path: C:\Users\OSFortify_Audit_Report.txt
 
 - Bug fixes: indentation
 - Additional comments to clarify code

 OSFortify 2.0.1 (not released yet)
 - Bug fixes
 - Additional error handling
 - Fixed GPO backup feature for some systems.

  
---
