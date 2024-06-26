
      ################################
      # OSFortify v2.0 by DannnyzZ ##
      ################################

# V2.0 
# - Added software inventory
# Autorun
# Powershell security
# Terminal security
# Added checking for update in not windows related software
# Added GPO module
# Added Event Viewer & logging module
# Added UAC hardening
# Added Terminal hardening

# Add managing services:
# Powershell

#Future 
# Add exporting after execution to pdf


# BLOCK PORT

import os
import subprocess
import curses
import ctypes
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess

# FUNCTION - CONSOLE WINDOW SETTINGS
hwnd = ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.MoveWindow(hwnd, 0, 0, 660, 740, True)

# S C R I P T S # S C R I P T S # S C R I P T S # S C R I P T S # S C R I P T S # S C R I P T S # S C R I P T S # S C R I P T S # S C R I P T S # 

# LIST OF OBJECTS (TICKMARK STATUS, NAME, GROUP, VALUES)



################################################# O B J E C T S 1 ###############################################################################



objects = [
    # SERVICES
    {
        "group": "Services",
        "name": "Windows Defender",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Defender   |" -ForegroundColor Cyan

                $serviceStatus = Get-Service -Name 'WinDefend' | Select-Object -Property Name, Status, StartType
                $defender = Get-MpComputerStatus
                $defenderPreferences = Get-MpPreference

                if ($defender.AntivirusEnabled) {
                    Write-Output "`n      Windows Defender is enabled."
                    $defenderVersion = $defender.AntivirusSignatureVersion
                    Write-Output "      Windows Defender version: $defenderVersion"
                    $defenderSignatureVersion = $defender.AntivirusSignatureUpdateDateTime
                    Write-Output "      Windows Defender signature version: $defenderSignatureVersion"
                    if ($defender.SignatureUpdateAvailable) {
                        Write-Output "      New Windows Defender updates are available."
                    } else {
                        Write-Output "      Windows Defender is up to date. No available updates."
                    }
                    if ($defenderPreferences.DisableRealtimeMonitoring) {
                        Write-Output "      Real-time monitoring is disabled."
                    } else {
                        Write-Output "      Real-time monitoring is enabled."
                    }
                    if ($defenderPreferences.DisableRealtimeMonitoring -eq $false) {
                        Write-Output "      Real-time protection is enabled."
                    } else {
                        Write-Output "      Real-time protection is disabled."
                    }
                    if ($defenderPreferences.DisableBehaviorMonitoring -eq $false) {
                        Write-Output "      Behavior monitoring is enabled."
                    } else {
                        Write-Output "      Behavior monitoring is disabled."
                    }
                    if ($defenderPreferences.DisableOnAccessProtection -eq $false) {
                        Write-Output "      On-access protection is enabled."
                    } else {
                        Write-Output "      On-access protection is disabled."
                    }
                    if ($defenderPreferences.ExclusionPath) {
                        Write-Output "`n      The following paths are excluded from scans:"
                        foreach ($path in $defenderPreferences.ExclusionPath) {
                            Write-Output "        $path"
                        }
                    } else {
                        Write-Output "      There are no path exclusions."
                    }
                } else {
                    Write-Output "      Windows Defender is not enabled."
                }
            } catch {
                Write-Output "      Error: Unable to retrieve Defender status."
            }
            ''',
            ''' try { Set-Service -Name 'WinDefend' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'WinDefend' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'WinDefend' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'WinDefend' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Windows Firewall",
        "tickmark": False,
        "values": [
            '''
            try {
                $profiles = @("Domain", "Public", "Private")
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Firewall   |" -ForegroundColor Cyan
                foreach($profile in $profiles){
                    $firewallStatus = (Get-NetFirewallProfile -Name $profile).Enabled
                    Write-Output "`n      Firewall status for $profile profile: $(if($firewallStatus -eq 'True'){'Enabled'} else {'Disabled'})"
                }
            } catch {
                Write-Output "      Error: Unable to retrieve Firewall status."
            }
            ''',
            ''' try { Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True } catch { Write-Output '      Error: Unable to enable Windows Firewall.' } ''',
            ''' try { Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False } catch { Write-Output '      Error: Unable to disable Windows Firewall.' } ''',
            ''' try { Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True } catch { Write-Output '      Error: Unable to enable Windows Firewall.' } ''',
            ''' try { Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False } catch { Write-Output '      Error: Unable to disable Windows Firewall.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Windows Update",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Update   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'wuauserv' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Output "|   Windows Updates   |"
                
                $session = New-Object -ComObject "Microsoft.Update.Session"
                $searcher = $session.CreateUpdateSearcher()
                $updates = $searcher.Search("Type='Software' and IsInstalled=0")
                if ($updates.Updates.Count -gt 0) {
                    $latestUpdate = $updates.Updates | Sort-Object -Property Date -Descending | Select-Object -First 1
                    Write-Output "`n      New Updates Available: $($updates.Updates.Count)"
                    Write-Output "      Latest Update Title: $($latestUpdate.Title)"
                    Write-Output "      KB Article IDs: $($latestUpdate.KBArticleIDs -join ', ')"
                } else {
                    Write-Output "`n      Windows is up to date. No available updates."
                }
            } catch {
                Write-Output "      Error: Unable to retrieve Windows Update status."
            }
            ''',
            ''' try { Set-Service -Name 'wuauserv' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'wuauserv' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'wuauserv' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'wuauserv' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Windows Remote Registry",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Remote Registry   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'RemoteRegistry' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'RemoteRegistry' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'RemoteRegistry' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'RemoteRegistry' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'RemoteRegistry' -Force } catch { Write-Output '      Error: Unable to stop the service.' } '''
        ]
    },
    {
        "group": "Services",
        "name": "Windows Remote Management",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Remote Management   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'winrm' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'winrm' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'winrm' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'winrm' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'winrm' -Force } catch { Write-Output '      Error: Unable to stop the service.' } '''
        ]
    },
    {
        "group": "Services",
        "name": "Windows Management Instrumentation (WMI)",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Management Instrumentation (WMI)   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'winmgmt' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'winmgmt' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'winmgmt' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'winmgmt' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'winmgmt' -Force } catch { Write-Output '      Error: Unable to stop the service.' } '''
        ]
    },
    {
        "group": "Services", "name": "Remote Desktop Protocol (RDP)", "tickmark": False, "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Remote Desktop Protocol (RDP)   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'TermService' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'TermService' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'TermService' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'TermService' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'TermService' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services", "name": "Windows Error Reporting", "tickmark": False, "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Error Reporting   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'WerSvc' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'WerSvc' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'WerSvc' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'WerSvc' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'WerSvc' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Windows Remote Assistance",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Remote Assistance   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'SessionEnv' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'SessionEnv' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'SessionEnv' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'SessionEnv' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'SessionEnv' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Windows Fax and Scan",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Fax and Scan   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'fax' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'fax' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'fax' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'fax' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'fax' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Internet Printing Client",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Internet Printing Client   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'PrintNotify' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'PrintNotify' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'PrintNotify' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'PrintNotify' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'PrintNotify' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Universal Plug and Play (UPnP)",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Universal Plug and Play (UPnP)   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'SSDPSRV' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'SSDPSRV' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'SSDPSRV' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'SSDPSRV' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'SSDPSRV' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Bluetooth",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Bluetooth   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'bthserv' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'bthserv' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'bthserv' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'bthserv' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'bthserv' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Windows Search",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Search   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'WSearch' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'WSearch' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'WSearch' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'WSearch' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'WSearch' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Print Spooler",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Print Spooler   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'Spooler' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'Spooler' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'Spooler' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'Spooler' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'Spooler' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Microsoft IIS",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Microsoft IIS   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'W3SVC' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'W3SVC' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'W3SVC' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'W3SVC' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'W3SVC' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "NetBIOS",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   NetBIOS   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'NetBT' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'NetBT' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'NetBT' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'NetBT' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'NetBT' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Link-Local Multicast Name Resolution (LLMNR)",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Link-Local Multicast Name Resolution (LLMNR)   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'lltdsvc' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-Service -Name 'lltdsvc' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'lltdsvc' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'lltdsvc' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'lltdsvc' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Services",
        "name": "Server Message Block Version 1 (SMB1)",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Server Message Block Version 1 (SMB1)   |" -ForegroundColor Cyan
                $smb1Enabled = (Get-SmbServerConfiguration | Select-Object -ExpandProperty EnableSMB1Protocol)
                if ($smb1Enabled) {
                    Write-Output "`n      SMB1 is enabled."
                } else {
                    Write-Output "`n      SMB1 is disabled."
                }
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-SmbServerConfiguration -EnableSMB1Protocol $true } catch { Write-Output '      Error: Unable to enable SMB1.' } ''',
            ''' try { Set-SmbServerConfiguration -EnableSMB1Protocol $false } catch { Write-Output '      Error: Unable to disable SMB1.' } ''',
            ''';''',
            ''';''',
        ]
    },
    {
        "group": "Services",
        "name": "Server Message Block Version 2 (SMB2)",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Server Message Block Version 2 (SMB2)   |" -ForegroundColor Cyan
                $smb2Enabled = (Get-SmbServerConfiguration | Select-Object -ExpandProperty EnableSMB2Protocol)
                if ($smb2Enabled) {
                    Write-Output "`n      SMB2 is enabled."
                } else {
                    Write-Output "`n      SMB2 is disabled."
                }
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Set-SmbServerConfiguration -EnableSMB2Protocol $true } catch { Write-Output '      Error: Unable to enable SMB2.' } ''',
            ''' try { Set-SmbServerConfiguration -EnableSMB2Protocol $false } catch { Write-Output '      Error: Unable to disable SMB2.' } ''',
            ''';''',
            ''';''',
        ]
    },
    {
        "group": "Services",
        "name": "Telnet",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Telnet   |" -ForegroundColor Cyan
                $telnetFeature = Get-WindowsOptionalFeature -FeatureName 'TelnetClient' -Online
                if ($telnetFeature) {
                    if ($telnetFeature.State -eq "Enabled") {
                        Write-Output "`n      Telnet Client: Enabled"
                    } elseif ($telnetFeature.State -eq "Disabled") {
                        Write-Output "`n      Telnet Client: Disabled"
                    } else {
                        Write-Output "`n      Telnet Client: State unknown"
                    }
                } else {
                    Write-Output "`n      Telnet Client: Not installed"
                }
            } catch {
                Write-Output "`n      Error: Unable to retrieve service information."
            }
            ''',
            ''' try { Enable-WindowsOptionalFeature -FeatureName 'TelnetClient' -Online } catch { Write-Output '`n      Error: Unable to enable Telnet Client.' } ''',
            ''' try { Disable-WindowsOptionalFeature -FeatureName 'TelnetClient' -Online } catch { Write-Output '`n      Error: Unable to disable Telnet Client.' } ''',
            ''' try { Start-Process -FilePath 'telnet.exe' } catch { Write-Output '`n      Error: Unable to start the service.' } ''',
            ''' try { Stop-Process -Name 'telnet' -Force } catch { Write-Output '`n      Error: Unable to stop the service.' } ''',
        ]
    },
]



################################################# O B J E C T S 2 ###############################################################################



objects2 = [
    {
        "group": "Features/Network",
        "name": "Guest user account",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Guest user account   |" -ForegroundColor Cyan

                $guestAccount = Get-LocalUser -Name 'Guest' -ErrorAction SilentlyContinue
                if ($guestAccount) {
                    Write-Output "`n      Guest user account exists."
                } else {
                    Write-Output "`n      Guest user account does not exist!"
                }
            } catch {
                Write-Output "`n      Error: Unable to retrieve Guest user account status."
            }
            ''',
            "Try {Enable-LocalUser -Name 'Guest'} Catch {Write-Output '`n      Cannot enable Guest user account!'}",
            "Try {Disable-LocalUser -Name 'Guest'} Catch {Write-Output '`n      Cannot disable Guest user account!'}",
            ";",
            ";",
        ]
    },
    {
        "group": "Features/Network",
        "name": "Autorun",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Autorun   |" -ForegroundColor Cyan
                Write-Host " "
                # Check autorun state
                $regKey = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer"
                $regValueName = "NoDriveTypeAutorun"

                if (Test-Path $regKey) {
                    $noDriveTypeAutorun = (Get-ItemProperty -Path $regKey -Name $regValueName -ErrorAction SilentlyContinue).$regValueName
                    if ($noDriveTypeAutorun -eq 255) {
                        Write-Host "      Autorun is disabled."
                    } elseif ($noDriveTypeAutorun -eq 145) {
                        Write-Host "      Autorun is enabled."
                    } else {
                        Write-Host "      Unknown autorun state."
                    }
                } else {
                    Write-Host "      Autorun settings not found."
                }
            } catch {
                Write-Host "      An error occurred: $_"
            }
            ''',
            ''' Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" -Name "NoDriveTypeAutorun" -Value 145 -Type DWord ''',
            ''' Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" -Name "NoDriveTypeAutorun" -Value 255 -Type DWord ''',
            ";",
            ";",
        ]
    },
    {
        "group": "Features/Network",
        "name": "Terminal",
        "tickmark": False,
        "values": [
            '''
            try {
            Write-Output "`n_________________________________________________________________________________________________________"
            Write-Host "|   Terminal   |" -ForegroundColor Cyan
            Write-Host " "
            # Check if Command Prompt is running with administrative privileges
            $isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")

            # Check if Command Prompt execution policy is restricted
            $executionPolicy = Get-ExecutionPolicy

            # Check if Command Prompt usage is restricted via Group Policy
            $regKey = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System"
            $regValueName = "DisableCMD"

            if (Test-Path $regKey) {
                $disableCmd = (Get-ItemProperty -Path $regKey -Name $regValueName -ErrorAction SilentlyContinue).$regValueName
                if ($disableCmd -eq 1) {
                $groupPolicyRestriction = "     Command Prompt usage is restricted via Group Policy"
                } else {
                $groupPolicyRestriction = "      Command Prompt usage is not restricted via Group Policy"
                }
            } else {
                $groupPolicyRestriction = "      No Group Policy restriction found for Command Prompt usage"
            }

            # Output the results
            Write-Host "      Command Prompt Running with Administrative Privileges: $isAdmin"
            Write-Host "      Command Prompt Execution Policy: $executionPolicy"
            Write-Host $groupPolicyRestriction
            }
            catch {
            Write-Host "An error occurred: $_" -ForegroundColor Red
            }
            ''',
            ''' 
            # Remove the item property
            Remove-ItemProperty -Path 'HKCU:\Software\Policies\Microsoft\Windows\System' -Name DisableCMD
            ''',
            ''',
            # Create the registry path if it doesn't exist
            New-Item -Path 'HKCU:\Software\Policies\Microsoft\Windows\System' -Force
            # Disable Command Prompt
            Set-ItemProperty -Path 'HKCU:\Software\Policies\Microsoft\Windows\System' -Name DisableCMD -Value 1
            ''',
            ";",
            ";",
        ]
    },
    {
        "group": "Features/Network",
        "name": "Event Viewer",
        "tickmark": False,
        "values": [
            '''
            try {
            Write-Output "`n_________________________________________________________________________________________________________"
            Write-Host "|   Event Viewer   |" -ForegroundColor Cyan
            try {
                $serviceStatus = Get-Service -Name 'EventLog' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                $formattedName = "`n      Name: " + $_.Name
                $formattedStatus = "      Status: " + $_.Status
                $formattedStartType = "      StartType: " + $_.StartType
                $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            } catch {
            Write-Output "      Error: An error occurred while accessing Event Viewer."
            }
            ''',
            ''' try { Set-Service -Name 'EventLog' -StartupType Automatic } catch { Write-Output '      Error: Unable to set startup type to Automatic.' } ''',
            ''' try { Set-Service -Name 'EventLog' -StartupType Disabled } catch { Write-Output '      Error: Unable to set startup type to Disabled.' } ''',
            ''' try { Start-Service -Name 'EventLog' } catch { Write-Output '      Error: Unable to start the service.' } ''',
            ''' try { Stop-Service -Name 'EventLog' -Force } catch { Write-Output '      Error: Unable to stop the service.' } ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "File Transfer Protocol (FTP)",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   File Transfer Protocol (FTP)   |" -ForegroundColor Cyan
                $serviceStatus = Get-Service -Name 'ftpsvc' | Select-Object -Property Name, Status, StartType
                $formattedStatus = $serviceStatus | ForEach-Object {
                    $formattedName = "`n      Name: " + $_.Name
                    $formattedStatus = "      Status: " + $_.Status
                    $formattedStartType = "      StartType: " + $_.StartType
                    $formattedInfo = $formattedName, $formattedStatus, $formattedStartType -join "`n"
                    $formattedInfo
                }
                Write-Output $formattedStatus.TrimEnd()
            } catch {
                Write-Output "      Error: Unable to retrieve service information."
            }
            ''',
            "try {Set-Service -Name 'ftpsvc' -StartupType Automatic -ErrorAction Stop} catch {Write-Output '`n      Cannot set FTP service to automatic startup!'}",
            "try {Set-Service -Name 'ftpsvc' -StartupType Disabled -ErrorAction Stop} catch {Write-Output '`n      Cannot set FTP service to disabled startup!'}",
            "try {Start-Service -Name 'ftpsvc' -ErrorAction Stop} catch {Write-Output '`n      Cannot start FTP service!'}",
            "try {Stop-Service -Name 'ftpsvc' -Force -ErrorAction Stop} catch {Write-Output '`n      Cannot stop FTP service!'}",
        ]
    },
    {
        "group": "Features/Network",
        "name": "Windows Media Player",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   Windows Media Player   |" -ForegroundColor Cyan

                if (Get-WindowsOptionalFeature -Online -FeatureName 'WindowsMediaPlayer' -ErrorAction SilentlyContinue) {
                    Write-Output "`n      Windows Media Player is installed."
                } else {
                    Write-Output "`n      Windows Media Player is not installed."
                }
            } catch {
                Write-Output "`n      Error: Unable to retrieve Windows Media Player status."
            }
            ''',
            ''' try {Enable-WindowsOptionalFeature -Online -FeatureName 'WindowsMediaPlayer' -NoRestart -ErrorAction Stop} catch {Write-Output '`n      Cannot enable Windows Media Player feature!'} ''',
            ''' try {Disable-WindowsOptionalFeature -Online -FeatureName 'WindowsMediaPlayer' -NoRestart -ErrorAction Stop} catch {Write-Output '`n      Cannot disable Windows Media Player feature!'} ''',
            ''' try {Start-Process -FilePath 'C:\\Program Files\\Windows Media Player\\wmplayer.exe' -ErrorAction Stop} catch {Write-Output '`n      Cannot start Windows Media Player!'} ''',
            ''' try {Stop-Process -Name 'wmplayer' -Force -ErrorAction Stop} catch {Write-Output '`n      Cannot stop Windows Media Player!'} ''',
        ]   
    },
    {
        "group": "Features/Network",
        "name": "USB ports",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   USB ports   |" -ForegroundColor Cyan

                $usbPorts = Get-PnpDevice -Class "USB" | Select-Object -Property DeviceID, Status, Parent
                foreach ($port in $usbPorts) { 
                    $portNumber = $port.DeviceID -replace "\\\\|USBSTOR\\\\DISK&VEN_|&REV.*$"; 
                    $parent = $port.Parent -replace ".*\\\\\\\\(?<parent>.+?)\\\\\\\\.*", '$1'; 
                    $status = if ($port.Status -eq "OK") { "   Enabled" } else { "   Disabled" }; 
                    Write-Output "`n      USB port $portNumber is $status. Parent: $parent" 
                }
            } catch {
                Write-Output "`n      Error: Unable to retrieve USB ports status."
            }
            ''',
            ''' try {Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR' -Name 'Start' -Value 3; Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Power' -Name 'SelectiveSuspendEnabled' -Value 1; Write-Output '      USB ports have been enabled.'} catch {Write-Output '      Cannot enable USB ports!'} ''',
            ''' try {Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR' -Name 'Start' -Value 4; Set-ItemProperty -Path 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Power' -Name 'SelectiveSuspendEnabled' -Value 0; Write-Output '      USB ports have been disabled.'} catch {Write-Output '      Cannot disable USB ports!'} ''',
            '''
            try {
                $usbDevices = Get-PnpDevice -Class "USB"
                foreach ($usbDevice in $usbDevices) { 
                    if ($usbDevice.Status -ne "OK") { 
                        Enable-PnpDevice -InstanceId $usbDevice.InstanceId -Confirm:$false
                        Write-Output "`n      USB port $($usbDevice.DeviceID) has been started." 
                    } else { 
                        Write-Output "`n      USB port $($usbDevice.DeviceID) is already started." 
                    } 
                }
            } catch {
                Write-Output "`n      Error: Unable to start USB ports."
            }
            ''',
            '''
            try {
                $usbDevices = Get-PnpDevice -Class "USB"
                foreach ($usbDevice in $usbDevices) { 
                    if ($usbDevice.Status -eq "OK") { 
                        Disable-PnpDevice -InstanceId $usbDevice.InstanceId -Confirm:$false
                        Write-Output "`n      USB port $($usbDevice.DeviceID) has been stopped." 
                    } else { 
                        Write-Output "`n      USB port $($usbDevice.DeviceID) is already stopped." 
                    } 
                }
            } catch {
                Write-Output "`n      Error: Unable to stop USB ports."
            }
            ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "User Account Control (UAC)",
        "tickmark": False,
        "values": [
            '''
            try {
                $uacPolicy = Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' | Select-Object EnableInstallerDetection, FilterAdministratorToken, PromptOnSecureDesktop, ConsentPromptBehaviorAdmin
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|   UAC Group Policy Settings   |" -ForegroundColor Cyan
                Write-Output "`n      Enable Installer Detection: $(
                    switch ($uacPolicy.EnableInstallerDetection) {
                        0 { 'Disabled' }
                        1 { 'Enabled' }
                        default { 'Unknown' }
                    }
                )"
                Write-Output "      Filter Administrator Token: $(
                    switch ($uacPolicy.FilterAdministratorToken) {
                        0 { 'Disabled' }
                        1 { 'Enabled' }
                        default { 'Unknown' }
                    }
                )"
                Write-Output "      Prompt On Secure Desktop: $(
                    switch ($uacPolicy.PromptOnSecureDesktop) {
                        0 { 'Disabled' }
                        1 { 'Enabled' }
                        default { 'Unknown' }
                    }
                )"
                Write-Output "      Consent Prompt Behavior for Admins: $(
                    switch ($uacPolicy.ConsentPromptBehaviorAdmin) {
                        0 { 'No prompt' }
                        1 { 'Prompt for credentials on the secure desktop' }
                        2 { 'Prompt for consent on the secure desktop' }
                        3 { 'Prompt for consent on the non-secure desktop' }
                        4 { 'Prompt for credentials on the non-secure desktop' }
                        default { 'Unknown' }
                    }
                )"
            } catch {
                Write-Output "`n      Error: Unable to retrieve UAC group policy settings."
            }
            ''',
            ''' 
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name EnableInstallerDetection -Value 0
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name FilterAdministratorToken -Value 0
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name PromptOnSecureDesktop -Value 0
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name ConsentPromptBehaviorAdmin -Value 0
            $uacPolicy = Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' | Select-Object EnableInstallerDetection, FilterAdministratorToken, PromptOnSecureDesktop, ConsentPromptBehaviorAdmin
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name EnableInstallerDetection -Value 1
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name FilterAdministratorToken -Value 1
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name PromptOnSecureDesktop -Value 1
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name ConsentPromptBehaviorAdmin -Value 1
            ''',
            '''
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name EnableInstallerDetection -Value 0
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name FilterAdministratorToken -Value 0
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name PromptOnSecureDesktop -Value 0
            Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name ConsentPromptBehaviorAdmin -Value 0
            ''',
            ''' ''',
            ''' ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "Powershell security checks",
        "tickmark": False,
        "values": [
            '''
            Write-Output "`n_________________________________________________________________________________________________________"
                        Write-Host "|   Powershell security checks   |" -ForegroundColor Cyan
            $alwaysYes = $true  # Set this to $false if you want manual confirmation

            # Script execution with persistent "Yes"
            Write-Host ""
            Write-Host "      ** PowerShell Security Checks **"
            Write-Host ""
            function Check-ExecutionPolicy {
                try {
                    $machinePolicy = Get-ExecutionPolicy -Scope Machine
                    $userPolicy = Get-ExecutionPolicy -Scope CurrentUser
                    $machineStatus = if ($machinePolicy -eq "Restricted") { "Compliant" } else { "Non-Compliant (Recommended: Restricted)" }
                    $userStatus = if ($userPolicy -eq "Restricted") { "Compliant" } else { "Non-Compliant (Recommended: Restricted)" }
                    Write-Host ("      | Machine Policy         | {0,-20} " -f $machinePolicy)
                    Write-Host ("      | Machine Status         | {0,-40} " -f $machineStatus)
                    Write-Host ("      | User Policy            | {0,-20} " -f $userPolicy)
                    Write-Host ("      | User Status            | {0,-40} " -f $userStatus)
                } catch {
                    Write-Host "      Error: Unable to retrieve Execution Policy." -ForegroundColor Red
                }
            }
            # Call the function
            Check-ExecutionPolicy

            # Function to check JEA configuration
            function Check-JeaConfig {
            try {
                $jeaEnabled = Get-Service JeAppHost -ErrorAction Stop | Where-Object {$_.Status -eq "Running"}
                $jeaStatus = if ($jeaEnabled) { "Enabled" } else { "Disabled" }
                Write-Host ("      | JEA Service            | {0,-20} " -f $jeaStatus)
            } catch {
                Write-Host "      Error: Unable to retrieve JEA configuration." -ForegroundColor Red
            }
            }

            # Function to check script signing configuration
            function Check-ScriptSigning {
            try {
                $scriptSigningEnabled = (Get-ExecutionPolicy).PSEnableScriptSigning -eq "RemoteSigned"
                $signingStatus = if ($scriptSigningEnabled) { "Enabled (RemoteSigned)" } else { "Disabled" }
                Write-Host ("      | Script Signing         | {0,-40} " -f $signingStatus)
            } catch {
                Write-Host "      Error: Unable to retrieve Script Signing configuration." -ForegroundColor Red
            }
            }

            # Function to check logging configuration
            function Check-Logging {
            try {
                $winrmLogsEnabled = (Get-WinEvent -ListLog -ErrorAction Stop | Where-Object {$_.LogName -eq "WinRM"}).Enabled
                $logsStatus = if ($winrmLogsEnabled) { "Enabled (WinRM logs)" } else { "Disabled" }
                Write-Host ("      | Logging                | {0,-40} " -f $logsStatus)
            } catch {
                Write-Host "      Error: Unable to retrieve Logging configuration." -ForegroundColor Red
            }
            }

            # Function to check remoting configuration
            function Check-RemotingConfiguration {
            try {
                $remotingEnabled = Get-Service WinRM -ErrorAction Stop | Where-Object {$_.Status -eq "Running"}
                $remotingStatus = if ($remotingEnabled) { "Enabled" } else { "Disabled" }
                Write-Host ("      | Remoting Service       | {0,-20} " -f $remotingStatus)
            } catch {
                Write-Host "      Error: Unable to retrieve Remoting configuration." -ForegroundColor Red
            }
            }

            function Check-BitsadminAvailability {
            if (Get-Command bitsadmin) {
                Write-Host ("      | Bitsadmin Availability | {0,-20} " -f "Available")
            } else {
                Write-Host ("      | Bitsadmin Availability | {0,-20} " -f "Not Available (unlikely scenario)")
            }
            }

            # Check remoting configuration
            Write-Host ""
            Write-Host "      ** Remoting Configuration Check **"
            try {
            Check-RemotingConfiguration
            } catch {
            Write-Host "      Error: Unable to retrieve Remoting configuration." -ForegroundColor Red
            }

            # Additional security checks
            Write-Host ""
            Write-Host "      ** Additional Security Checks **"
            Check-ScriptSigning
            Check-BitsadminAvailability

            Write-Host ""
            ''',
            ''' 
            # RESTORATION
            Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope MachinePolicy -Force
            Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope UserPolicy -Force
            Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process -Force
            Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser -Force
            Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine -Force

            Set-Service WinRM -Status Running
            ''',
            '''
            # Set restricted policy
            Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope MachinePolicy -Force
            Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope UserPolicy -Force
            Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope Process -Force
            Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope CurrentUser -Force
            Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope LocalMachine -Force

            # Set remoting configuration
            Set-Service WinRM -Status Stopped
            ''',
            ''' ''',
            ''' ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "Route: Displays the local routing table on the system.",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|         Route          |" -ForegroundColor Cyan
                route print
            } catch {
                Write-Output "`nError: Unable to retrieve local routing table."
            }
            ''',
            ''' ''',
            ''' ''',
            ''' ''',
            ''' ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "Ping: 20 ICMP echo requests to google.com - bandwidth test.",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|          Ping          |" -ForegroundColor Cyan
                ping -n 20 google.com
            } catch {
                Write-Output "`nError: Unable to perform ping to google.com."
            }
            ''',
            ''' ''',
            ''' ''',
            ''' ''',
            ''' ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "ARP: ARP cache, mapping of IP to MAC addresses on the LAN.",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|          ARP           |" -ForegroundColor Cyan
                arp -a
            } catch {
                Write-Output "`nError: Unable to retrieve ARP cache."
            }
            ''',
            ''' ''',
            ''' ''',
            ''' ''',
            ''' ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "DNS: Retrieves unique DNS server addresses for IPv4/IPv6.",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|          DNS           |" -ForegroundColor Cyan
                # Get unique DNS server addresses for IPv4
                $ipv4Addresses = (Get-DnsClientServerAddress -AddressFamily IPv4).ServerAddresses | Sort-Object -Unique

                # Get unique DNS server addresses for IPv6
                $ipv6Addresses = (Get-DnsClientServerAddress -AddressFamily IPv6).ServerAddresses | Sort-Object -Unique

                # Display IPv4 addresses
                Write-Host "IPv4 DNS Server Addresses:"
                foreach ($ipv4Address in $ipv4Addresses) {
                    Write-Host $ipv4Address
                }

                # Display IPv6 addresses
                Write-Host "IPv6 DNS Server Addresses:"
                foreach ($ipv6Address in $ipv6Addresses) {
                    Write-Host $ipv6Address
                }
            } catch {
                Write-Output "`nError: Unable to retrieve DNS server addresses."
            }
            ''',
            ''' ''',
            ''' ''',
            ''' ''',
            ''' ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "Traceroute: Check the route of packets to the destination (google.com).",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|      Traceroute        |" -ForegroundColor Cyan
                Test-NetConnection -ComputerName google.com -TraceRoute
            } catch {
                Write-Output "`nError: Unable to perform traceroute to google.com."
            }
            ''',
            ''' ''',
            ''' ''',
            ''' ''',
            ''' ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "Routing Table: System's routing table.",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|    Routing Table       |" -ForegroundColor Cyan
                Get-NetRoute
            } catch {
                Write-Output "`nError: Unable to retrieve routing table information."
            }
            ''',
            ''' ''',
            ''' ''',
            ''' ''',
            ''' ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "Ipconfig: Multiple networking specifications",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|        Ipconfig        |" -ForegroundColor Cyan
                ipconfig /all
            } catch {
                Write-Output "`nError: Unable to retrieve Ipconfig information."
            }
            ''',
            ''' ''',
            ''' ''',
            ''' ''',
            ''' ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "Netstat: Active network connections, listening ports, associated processes.",
        "tickmark": False,
        "values": [
            '''
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|        Netstat         |" -ForegroundColor Cyan
                netstat -b
            } catch {
                Write-Output "`nError: Unable to retrieve Netstat information."
            }
            ''',
            ''' ''',
            ''' ''',
            ''' ''',
            ''' ''',
        ]
    },
    {
        "group": "Features/Network",
        "name": "Autonomous System Numbers (ASN): Associated ASN, AS and IP.",
        "tickmark": False,
        "values": [
            '''
            # the ip-api.com service. Displays IP address, ASN, and AS Name if available.
            try {
                Write-Output "`n_________________________________________________________________________________________________________"
                Write-Host "|    ASN Information     |" -ForegroundColor Cyan
                function Get-ASN {
                    param(
                        [string]$IPAddress
                    )

                    $url = "http://ip-api.com/json/$IPAddress"

                    $response = Invoke-RestMethod -Uri $url -Method Get

                    if ($response.status -eq "fail") {
                        Write-Host "Failed to retrieve ASN information for $IPAddress"
                    } else {
                        Write-Host "IP Address: $($response.query)"
                        Write-Host "ASN: $($response.as)"
                        
                        if ($response.asname) {
                            Write-Host "AS Name: $($response.asname)"
                        } else {
                            Write-Host "AS Name: Not available"
                        }
                    }
                }

                # Example usage
                Get-ASN -IPAddress "8.8.8.8"
            } catch {
                Write-Output "`nError: Unable to retrieve ASN information."
            }
            ''',
            ''' ''',
            ''' ''',
            ''' ''',
            ''' ''',
        ]
    },
]



################################################# O B J E C T S 3 ###############################################################################



    # PORTS
objects3 = [
    {
        "group": "Ports", "name": "Port 7 - Echo", "tickmark": False, "values": [
        '''
        Write-Output "`n_________________________________________________________________________________________________________"
        Write-Host "|   Port 7 - Echo   |" -ForegroundColor Cyan
        Write-Output ""
        $portStatusIPv4 = $null
        $portStatusIPv6 = $null
        $firewallRules = $null
        $processInfo = $null
        $processPID = $null

        try {
            $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 7 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
            $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
        } catch {
            Write-Output "      Error occurred while testing port 7: $_"
        }

        try {
            $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 7 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
            $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
        } catch {
            Write-Output "      Error occurred while testing port 7: $_"
        }

        try {
            $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "7") -or ($_.RemotePorts -eq "7") }
        } catch {
            Write-Output "      Error occurred while retrieving firewall rules: $_"
        }

        try {
            $processPID = Get-NetTCPConnection -LocalPort 7 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
        } catch {
            Write-Output "      Error occurred while checking if port 7 is in use: $_"
        }

        if ($processPID) {
            try {
                $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
            } catch {
                Write-Output "      Error occurred while retrieving process details: $_"
            }
        }

        if ($portStatusIPv4 -and $portStatusIPv6) {
            Write-Host '      Port 7 is open.'
        } else {
            Write-Host '      Port 7 is closed or filtered.'
        }

        if ($firewallRules) {
            Write-Host '      Firewall rules for Port 7 exist.'
            $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
        } else {
            Write-Host '      No OSFortify firewall rules found for Port 7.'
        }

        if ($processInfo) {
            Write-Host "      Port 7 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
            Write-Output "      Process Details:"
            Write-Output "         Id: $($processInfo.Id)"
            Write-Output "         Name: $($processInfo.Name)"
            Write-Output "         StartTime: $($processInfo.StartTime)"
            Write-Output "         CPU: $($processInfo.CPU)"
            Write-Output "         Path: $($processInfo.Path)"
        } else {
            Write-Host '      No process is using Port 7.'
        }
        '''
        ]
    },
    {
        "group": "Ports", "name": "Port 20 - File Transfer Protocol (FTP)", "tickmark": False, "values": [
        '''
        Write-Output "`n_________________________________________________________________________________________________________"
        Write-Host "|   Port 20 - File Transfer Protocol (FTP)   |" -ForegroundColor Cyan
        Write-Output ""
        $portStatusIPv4 = $null
        $portStatusIPv6 = $null
        $firewallRules = $null
        $processInfo = $null
        $processPID = $null

        try {
            $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 20 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
            $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
        } catch {
            Write-Output "      Error occurred while testing port 20: $_"
        }

        try {
            $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 20 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
            $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
        } catch {
            Write-Output "      Error occurred while testing port 20: $_"
        }

        try {
            $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "20") -or ($_.RemotePorts -eq "20") }
        } catch {
            Write-Output "      Error occurred while retrieving firewall rules: $_"
        }

        try {
            $processPID = Get-NetTCPConnection -LocalPort 20 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
        } catch {
            Write-Output "      Error occurred while checking if port 20 is in use: $_"
        }

        if ($processPID) {
            try {
                $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
            } catch {
                Write-Output "      Error occurred while retrieving process details: $_"
            }
        }

        if ($portStatusIPv4 -and $portStatusIPv6) {
            Write-Host '      Port 20 is open.'
        } else {
            Write-Host '      Port 20 is closed or filtered.'
        }

        if ($firewallRules) {
            Write-Host '      Firewall rules for Port 20 exist.'
            $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
        } else {
            Write-Host '      No OSFortify firewall rules found for Port 20.'
        }

        if ($processInfo) {
            Write-Host "      Port 20 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
            Write-Output "      Process Details:"
            Write-Output "         Id: $($processInfo.Id)"
            Write-Output "         Name: $($processInfo.Name)"
            Write-Output "         StartTime: $($processInfo.StartTime)"
            Write-Output "         CPU: $($processInfo.CPU)"
            Write-Output "         Path: $($processInfo.Path)"
        } else {
            Write-Host '      No process is using Port 20.'
        }
        '''
        ]
    },
    {
    "group": "Ports", "name": "Port 21 - File Transfer Protocol Control", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 21 - File Transfer Protocol Control   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 21 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 21: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 21 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 21: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "21") -or ($_.RemotePorts -eq "21") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 21 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 21 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 21 is open.'
    } else {
        Write-Host '      Port 21 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 21 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 21.'
    }

    if ($processInfo) {
        Write-Host "      Port 21 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 21.'
    }
    '''
    ]
    },
    {
    "group": "Ports", "name": "Port 22 - Secure Shell (SSH)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 22 - Secure Shell (SSH)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 22 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 22: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 22 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 22: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "22") -or ($_.RemotePorts -eq "22") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 22 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 22 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 22 is open.'
    } else {
        Write-Host '      Port 22 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 22 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 22.'
    }

    if ($processInfo) {
        Write-Host "      Port 22 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 22.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 23 - Telnet", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 23 - Telnet   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 23 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 23: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 23 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 23: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "23") -or ($_.RemotePorts -eq "23") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 23 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 23 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 23 is open.'
    } else {
        Write-Host '      Port 23 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 23 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 23.'
    }

    if ($processInfo) {
        Write-Host "      Port 23 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 23.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 25 - Simple Mail Transfer Protocol (SMTP)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 25 - Simple Mail Transfer Protocol (SMTP)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 25 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 25: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 25 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 25: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "25") -or ($_.RemotePorts -eq "25") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 25 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 25 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 25 is open.'
    } else {
        Write-Host '      Port 25 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 25 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 25.'
    }

    if ($processInfo) {
        Write-Host "      Port 25 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 25.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 37 - Time", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 37 - Time   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 37 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 37: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 37 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 37: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "37") -or ($_.RemotePorts -eq "37") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 37 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 37 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 37 is open.'
    } else {
        Write-Host '      Port 37 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 37 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 37.'
    }

    if ($processInfo) {
        Write-Host "      Port 37 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 37.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 53 - Domain Name System (DNS)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 53 - Domain Name System (DNS)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 53 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 53: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 53 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 53: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "53") -or ($_.RemotePorts -eq "53") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 53 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 53 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 53 is open.'
    } else {
        Write-Host '      Port 53 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 53 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 53.'
    }

    if ($processInfo) {
        Write-Host "      Port 53 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 53.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 69 - Trivial File Transfer Protocol (TFTP)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 69 - Trivial File Transfer Protocol (TFTP)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 69 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 69: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 69 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 69: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "69") -or ($_.RemotePorts -eq "69") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 69 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 69 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 69 is open.'
    } else {
        Write-Host '      Port 69 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 69 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 69.'
    }

    if ($processInfo) {
        Write-Host "      Port 69 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 69.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 80 - Hyper Text Transfer Protocol (HTTP)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 80 - Hyper Text Transfer Protocol (HTTP)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 80 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 80: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 80 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 80: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "80") -or ($_.RemotePorts -eq "80") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 80 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 80 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 80 is open.'
    } else {
        Write-Host '      Port 80 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 80 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 80.'
    }

    if ($processInfo) {
        Write-Host "      Port 80 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 80.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 110 - Post Office Protocol 3 (POP3)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 110 - Post Office Protocol 3 (POP3)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 110 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 110: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 110 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 110: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "110") -or ($_.RemotePorts -eq "110") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 110 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 110 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 110 is open.'
    } else {
        Write-Host '      Port 110 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 110 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 110.'
    }

    if ($processInfo) {
        Write-Host "      Port 110 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 110.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 111 - Remote Procedure Calls (RPC)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 111 - Remote Procedure Calls (RPC)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 111 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 111: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 111 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 111: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "111") -or ($_.RemotePorts -eq "111") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 111 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 111 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 111 is open.'
    } else {
        Write-Host '      Port 111 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 111 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 111.'
    }

    if ($processInfo) {
        Write-Host "      Port 111 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 111.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 123 - Network Time Protocol (NTP)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 123 - Network Time Protocol (NTP)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 123 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 123: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 123 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 123: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "123") -or ($_.RemotePorts -eq "123") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 123 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 123 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 123 is open.'
    } else {
        Write-Host '      Port 123 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 123 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 123.'
    }

    if ($processInfo) {
        Write-Host "      Port 123 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 123.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 135 - Microsoft Remote Procedure Call (MSRPC)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 135 - Microsoft Remote Procedure Call (MSRPC)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 135 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 135: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 135 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 135: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "135") -or ($_.RemotePorts -eq "135") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 135 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 135 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 135 is open.'
    } else {
        Write-Host '      Port 135 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 135 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 135.'
    }

    if ($processInfo) {
        Write-Host "      Port 135 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 135.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 137 - Server Message Block (SMB)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 137 - Server Message Block (SMB)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 137 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 137: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 137 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 137: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "137") -or ($_.RemotePorts -eq "137") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 137 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 137 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 137 is open.'
    } else {
        Write-Host '      Port 137 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 137 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 137.'
    }

    if ($processInfo) {
        Write-Host "      Port 137 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 137.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 139 - Server Message Block/NetBIOS Session Service (SMB/NetBIOS-SSN)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 139 - Server Message Block/NetBIOS Session Service (SMB/NetBIOS-SSN)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 139 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 139: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 139 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 139: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "139") -or ($_.RemotePorts -eq "139") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 139 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 139 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 139 is open.'
    } else {
        Write-Host '      Port 139 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 139 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 139.'
    }

    if ($processInfo) {
        Write-Host "      Port 139 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    def test_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                print(f'      Port {port} is open.')
            else:
                print(f'      Port {port} is closed or filtered.')
            sock.close()
        except Exception as e:
            print(f'      Error occurred while testing port {port}: {e}')

    def get_process_info(pid):
        try:
            process = psutil.Process(pid)
            print(f'      Port {port} is in use by process {process.name()} (PID: {pid}).')
            print("      Process Details:")
            print(f"         Id: {process.pid}")
            print(f"         Name: {process.name()}")
            print(f"         StartTime: {process.create_time()}")
            print(f"         CPU: {process.cpu_percent()}")
            print(f"         Path: {process.exe()}")
        except Exception as e:
            print(f'      Error occurred while retrieving process details: {e}')

    test_port(139)
    test_port(143)
    test_port(161)
    test_port(162)
    test_port(389)
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 389: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "389") -or ($_.RemotePorts -eq "389") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 389 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 389 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 389 is open.'
    } else {
        Write-Host '      Port 389 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 389 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 389.'
    }

    if ($processInfo) {
        Write-Host "      Port 389 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 389.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 443 - HTTP Secure (HTTPS)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 443 - HTTP Secure (HTTPS)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 443 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 443: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 443 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 443: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "443") -or ($_.RemotePorts -eq "443") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 443 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 443 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 443 is open.'
    } else {
        Write-Host '      Port 443 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 443 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 443.'
    }

    if ($processInfo) {
        Write-Host "      Port 443 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 443.'
    }
    '''
    ]
},
{
    "group": "Ports", "name": "Port 445 - Server Message Block over IP (SMB/IP)/MS Active Directory (MS-AD)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 445 - Server Message Block over IP (SMB/IP)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 445 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 445: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 445 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 445: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "445") -or ($_.RemotePorts -eq "445") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 445 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 445 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 445 is open.'
    } else {
        Write-Host '      Port 445 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 445 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 445.'
    }

    if ($processInfo) {
        Write-Host "      Port 445 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 445.'
    }
    '''
    ]
},

]

    # PORTS
objects4 = [
    {
    "group": "Ports 2", "name": "Port 636 - Secure Lightweight Directory Access Protocol (SLDAP)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 636 - Secure Lightweight Directory Access Protocol (SLDAP)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 636 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 636: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 636 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 636: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "636") -or ($_.RemotePorts -eq "636") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 636 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 636 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 636 is open.'
    } else {
        Write-Host '      Port 636 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 636 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 636.'
    }

    if ($processInfo) {
        Write-Host "      Port 636 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 636.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 993 - Internet Message Access Protocol Secure (IMAPS)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 993 - Internet Message Access Protocol Secure (IMAPS)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 993 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 993: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 993 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 993: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "993") -or ($_.RemotePorts -eq "993") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 993 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 993 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 993 is open.'
    } else {
        Write-Host '      Port 993 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 993 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 993.'
    }

    if ($processInfo) {
        Write-Host "      Port 993 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 993.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 995 - Post Office Protocol 3 Secure (POP3S)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 995 - Post Office Protocol 3 Secure (POP3S)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 995 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 995: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 995 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 995: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "995") -or ($_.RemotePorts -eq "995") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 995 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 995 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 995 is open.'
    } else {
        Write-Host '      Port 995 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 995 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 995.'
    }

    if ($processInfo) {
        Write-Host "      Port 995 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 995.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 989 - File Transfer Protocol over TLS/SSL (FTPS data)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 989 - File Transfer Protocol over TLS/SSL (FTPS data)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 989 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 989: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 989 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 989: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "989") -or ($_.RemotePorts -eq "989") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 989 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 989 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 989 is open.'
    } else {
        Write-Host '      Port 989 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 989 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 989.'
    }

    if ($processInfo) {
        Write-Host "      Port 989 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 989.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 990 - File Transfer Protocol over TLS/SSL (FTPS control)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 990 - File Transfer Protocol over TLS/SSL (FTPS control)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 990 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 990: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 990 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 990: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "990") -or ($_.RemotePorts -eq "990") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 990 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 990 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 990 is open.'
    } else {
        Write-Host '      Port 990 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 990 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 990.'
    }

    if ($processInfo) {
        Write-Host "      Port 990 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 990.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 1433 - Microsoft SQL Server", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 1433 - Microsoft SQL Server   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 1433 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 1433: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 1433 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 1433: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "1433") -or ($_.RemotePorts -eq "1433") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 1433 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 1433 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 1433 is open.'
    } else {
        Write-Host '      Port 1433 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 1433 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 1433.'
    }

    if ($processInfo) {
        Write-Host "      Port 1433 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 1433.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 1434 - Microsoft SQL Server Browser Service", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 1434 - Microsoft SQL Server Browser Service   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 1434 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 1434: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 1434 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 1434: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "1434") -or ($_.RemotePorts -eq "1434") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 1434 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 1434 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 1434 is open.'
    } else {
        Write-Host '      Port 1434 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 1434 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 1434.'
    }

    if ($processInfo) {
        Write-Host "      Port 1434 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 1434.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 1723 - Point-to-Point Tunneling Protocol (PPTP)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 1723 - Point-to-Point Tunneling Protocol (PPTP)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 1723 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 1723: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 1723 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 1723: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "1723") -or ($_.RemotePorts -eq "1723") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 1723 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 1723 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 1723 is open.'
    } else {
        Write-Host '      Port 1723 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 1723 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 1723.'
    }

    if ($processInfo) {
        Write-Host "      Port 1723 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 1723.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 1812 - Remote Authentication Dial-In User Service (RADIUS) Authentication", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 1812 - Remote Authentication Dial-In User Service (RADIUS) Authentication   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 1812 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 1812: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 1812 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 1812: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "1812") -or ($_.RemotePorts -eq "1812") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 1812 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 1812 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 1812 is open.'
    } else {
        Write-Host '      Port 1812 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 1812 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 1812.'
    }

    if ($processInfo) {
        Write-Host "      Port 1812 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 1812.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 1813 - Remote Authentication Dial-In User Service (RADIUS) Accounting", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 1813 - Remote Authentication Dial-In User Service (RADIUS) Accounting   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 1813 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 1813: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 1813 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 1813: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "1813") -or ($_.RemotePorts -eq "1813") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 1813 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 1813 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 1813 is open.'
    } else {
        Write-Host '      Port 1813 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 1813 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 1813.'
    }

    if ($processInfo) {
        Write-Host "      Port 1813 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 1813.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 3268 - Global Catalog Service", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 3268 - Global Catalog Service   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 3268 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 3268: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 3268 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 3268: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "3268") -or ($_.RemotePorts -eq "3268") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 3268 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 3268 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 3268 is open.'
    } else {
        Write-Host '      Port 3268 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 3268 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 3268.'
    }

    if ($processInfo) {
        Write-Host "      Port 3268 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 3268.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 3269 - Global Catalog Service over SSL (Secure Global Catalog Service)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 3269 - Global Catalog Service over SSL (Secure Global Catalog Service)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 3269 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 3269: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 3269 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 3269: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "3269") -or ($_.RemotePorts -eq "3269") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 3269 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 3269 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 3269 is open.'
    } else {
        Write-Host '      Port 3269 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 3269 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 3269.'
    }

    if ($processInfo) {
        Write-Host "      Port 3269 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 3269.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 3389 - Remote Desktop Protocol (RDP)/MS-WBT-server", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 3389 - Remote Desktop Protocol (RDP)/MS-WBT-server    |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 3389 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 3389: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 3389 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 3389: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "3389") -or ($_.RemotePorts -eq "3389") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 3389 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 3389 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 3389 is open.'
    } else {
        Write-Host '      Port 3389 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 3389 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 3389.'
    }

    if ($processInfo) {
        Write-Host "      Port 3389 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 3389.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 5060 - Session Initiation Protocol (SIP) (Non-encrypted)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 5060 - Session Initiation Protocol (SIP) (Non-encrypted)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 5060 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5060: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 5060 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5060: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "5060") -or ($_.RemotePorts -eq "5060") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 5060 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 5060 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 5060 is open.'
    } else {
        Write-Host '      Port 5060 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 5060 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 5060.'
    }

    if ($processInfo) {
        Write-Host "      Port 5060 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 5060.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 5061 - Session Initiation Protocol (SIP) over TLS (Encrypted)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 5061 - Session Initiation Protocol (SIP) over TLS (Encrypted)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 5061 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5061: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 5061 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5061: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "5061") -or ($_.RemotePorts -eq "5061") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 5061 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 5061 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 5061 is open.'
    } else {
        Write-Host '      Port 5061 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 5061 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 5061.'
    }

    if ($processInfo) {
        Write-Host "      Port 5061 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 5061.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 5190 - America Online and AOL Instant Messenger (AOL)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 5190 - America Online and AOL Instant Messenger (AOL)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 5190 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5190: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 5190 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5190: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "5190") -or ($_.RemotePorts -eq "5190") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 5190 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 5190 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 5190 is open.'
    } else {
        Write-Host '      Port 5190 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 5190 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 5190.'
    }

    if ($processInfo) {
        Write-Host "      Port 5190 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 5190.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 5631 - Symantec pcAnywhere (data)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 5631 - Symantec pcAnywhere (data)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 5631 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5631: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 5631 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5631: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "5631") -or ($_.RemotePorts -eq "5631") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 5631 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 5631 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 5631 is open.'
    } else {
        Write-Host '      Port 5631 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 5631 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 5631.'
    }

    if ($processInfo) {
        Write-Host "      Port 5631 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 5631.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 5632 - Symantec pcAnywhere (status)", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 5632 - Symantec pcAnywhere (status)   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 5632 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5632: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 5632 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5632: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "5632") -or ($_.RemotePorts -eq "5632") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 5632 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 5632 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 5632 is open.'
    } else {
        Write-Host '      Port 5632 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 5632 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 5632.'
    }

    if ($processInfo) {
        Write-Host "      Port 5632 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 5632.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 5800 - Virtual Network Computing (VNC) over HTTP", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 5800 - Virtual Network Computing (VNC) over HTTP   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 5800 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5800: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 5800 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5800: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "5800") -or ($_.RemotePorts -eq "5800") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 5800 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 5800 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 5800 is open.'
    } else {
        Write-Host '      Port 5800 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 5800 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 5800.'
    }

    if ($processInfo) {
        Write-Host "      Port 5800 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 5800.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 5900 - Virtual Network Computing (VNC) Standalone", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 5900 - Virtual Network Computing (VNC) Standalone   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 5900 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5900: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 5900 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 5900: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "5900") -or ($_.RemotePorts -eq "5900") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 5900 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 5900 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 5900 is open.'
    } else {
        Write-Host '      Port 5900 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 5900 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 5900.'
    }

    if ($processInfo) {
        Write-Host "      Port 5900 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 5900.'
    }
    '''
    ]
},
{
    "group": "Ports 2", "name": "Port 8080 - HTTP Proxy", "tickmark": False, "values": [
    '''
    Write-Output "`n_________________________________________________________________________________________________________"
    Write-Host "|   Port 8080 - HTTP Proxy   |" -ForegroundColor Cyan
    Write-Output ""
    $portStatusIPv4 = $null
    $portStatusIPv6 = $null
    $firewallRules = $null
    $processInfo = $null
    $processPID = $null

    try {
        $resultIPv4 = Test-NetConnection -ComputerName 127.0.0.1 -Port 8080 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv4 = $resultIPv4.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 8080: $_"
    }

    try {
        $resultIPv6 = Test-NetConnection -ComputerName ::1 -Port 8080 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
        $portStatusIPv6 = $resultIPv6.TcpTestSucceeded
    } catch {
        Write-Output "      Error occurred while testing port 8080: $_"
    }

    try {
        $firewallRules = Get-NetFirewallRule | Where-Object { ($_.LocalPorts -eq "8080") -or ($_.RemotePorts -eq "8080") }
    } catch {
        Write-Output "      Error occurred while retrieving firewall rules: $_"
    }

    try {
        $processPID = Get-NetTCPConnection -LocalPort 8080 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess
    } catch {
        Write-Output "      Error occurred while checking if port 8080 is in use: $_"
    }

    if ($processPID) {
        try {
            $processInfo = Get-Process -Id $processPID -ErrorAction SilentlyContinue
        } catch {
            Write-Output "      Error occurred while retrieving process details: $_"
        }
    }

    if ($portStatusIPv4 -and $portStatusIPv6) {
        Write-Host '      Port 8080 is open.'
    } else {
        Write-Host '      Port 8080 is closed or filtered.'
    }

    if ($firewallRules) {
        Write-Host '      Firewall rules for Port 8080 exist.'
        $firewallRules | Select-Object DisplayName, Direction, Action, Profile, Enabled | Format-Table
    } else {
        Write-Host '      No OSFortify firewall rules found for Port 8080.'
    }

    if ($processInfo) {
        Write-Host "      Port 8080 is in use by process $($processInfo.Name) (PID: $($processInfo.Id))."
        Write-Output "      Process Details:"
        Write-Output "         Id: $($processInfo.Id)"
        Write-Output "         Name: $($processInfo.Name)"
        Write-Output "         StartTime: $($processInfo.StartTime)"
        Write-Output "         CPU: $($processInfo.CPU)"
        Write-Output "         Path: $($processInfo.Path)"
    } else {
        Write-Host '      No process is using Port 8080.'
    }
    '''
    ]
},

# C O D E # C O D E # C O D E # C O D E # C O D E # C O D E # C O D E # C O D E # C O D E # C O D E # C O D E # C O D E # C O D E # C O D E # C O D E # C O D E

]
# LIST OF CONFIGURATIONS
configurations = [
    {"name": "Check the current status of the service/feature/port", "values": [0]},
    {"name": "Enable the service/feature/port on boot", "values": [1]},
    {"name": "Disable the service/feature/port on boot", "values": [2]},
    {"name": "Start the service/feature", "values": [3]},
    {"name": "Stop the service/feature", "values": [4]},
]

# INITIALIZATION OF CURSES
stdscr = None
def init_curses():
    global stdscr
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)
    curses.noecho()

def cleanup_curses():
    stdscr.keypad(False)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

# GLOBAL VALUES
index = 0
logical_position = 0
graphic_position = 0
cursor_start = 26
current_objects = objects

KEY_SYSTEM_INFORMATIONS = ord("i")

# GRAPHICAL USER INTERFACE
def display_objects():
    stdscr.clear()

    graphic = r"""
╔═══════════════════════════════════════════════════════════════════════════════════════════════╗

      .oooooo.    .oooooo..o oooooooooooo                        .    o8o   .o88o.             
     d8P'  `Y8b  d8P'    `Y8 `888'     `8                      .o8    `"    888 `"             
    888      888 Y88bo.       888          .ooooo.  oooo d8b .o888oo oooo  o888oo  oooo    ooo 
    888      888  `"Y8888o.   888oooo8    d88' `88b `888""8P   888   `888   888     `88.  .8'  
    888      888      `"Y88b  888    "    888   888  888       888    888   888      `88..8'   
    `88b    d88' oo     .d8P  888         888   888  888       888 .  888   888       `888'    
     `Y8bood8P'  8""88888P'  o888o        `Y8bod8P' d888b      "888" o888o o888o       .8'     
                                                                                   .o..P'      
                                                                                  `Y8P'       
    OSFortify v2.0, by DannnyzZ
╚═══════════════════════════════════════════════════════════════════════════════════════════════╝"""
    stdscr.addstr(graphic)

    # OPTIONS TABLE
    options_table = """
╔══════════« Options »══════════════════════════════════════════════════════════════════════════╗
  Enter: Toggle tickmark       A: Enable all                            U: Unmark all           
  S: Save to file              E: Execute tickmarked options            H: Help                 
  R: Refresh interface         C: Change configuration                  Q: Quit  
  N: Change objects            I: System informations
  P: Security policies         V: Event Viewer
╚═══════════════════════════════════════════════════════════════════════════════════════════════╝"""
    stdscr.addstr(options_table)

    # SELECTED CONFIGURATION TABLE
    selected_config_table = f"""
╔══════════« Selected Configuration »═══════════════════════════════════════════════════════════╗
  {configurations[index]['name']:<48s}                                          
╚═══════════════════════════════════════════════════════════════════════════════════════════════╝"""
    stdscr.addstr(selected_config_table)

    objects_table = """
╔══════════« List of objects »══════════════════════════════════════════════════════════════════╗
"""

    groups = {}
    for obj in current_objects:
        group = obj["group"]
        if group not in groups:
            groups[group] = []
        groups[group].append(obj)

    for group, group_objects in groups.items():
        objects_table += f"║ {group.upper():^86s}        ║\n"
        for i, obj in enumerate(group_objects):
            tickmark = "[X]" if obj["tickmark"] else "[ ]"
            obj_name = f"{i + 1}. {obj['name']}"
            objects_table += f"║ {tickmark} {obj_name:<82s}        ║\n"

    objects_table += "╚═══════════════════════════════════════════════════════════════════════════════════════════════╝"

    try:
        stdscr.addstr(objects_table)
    except curses.error:
        pass

    # CURSOR SETTINGS - FORMATTING
    cursor_position = cursor_start + graphic_position

    visible_lines = curses.LINES - cursor_start - 2  # FOOTER SETTINGS
    if cursor_position >= cursor_start and cursor_position < cursor_start + visible_lines:
        stdscr.move(cursor_position, 3)

# FUNCTION - DISPLAY HELP - MANUAL
def display_help():
    stdscr.refresh()
    cmd = (
        'echo   && '
        'mode 116,30 && echo   =============================================================================================================== && '
        'echo                                                   * INTRODUCTION *                                                 && '
        'echo   ===============================================================================================================  && '
        'echo      This program is a terminal-based interface designed to manage system services, features, network, and ports.  && '
        'echo   ===============================================================================================================  && '
        'echo                                              * HOW TO USE THE PROGRAM *                                            && '
        'echo   ===============================================================================================================  && '
        'echo     1. Use arrows to navigate through the list of services/features/network/ports.                                 && '
        'echo     2. Toggle tickmark with Enter.                                                                                 && '
        'echo     3. Choose the type of function with \'C\'.                                                                     && '
        'echo     4. Execute the desired configuration with \'E\', and save the configuration with \'S\'.                        && '
        'echo   ===============================================================================================================  && '
        'echo                                                    * FUNCTIONS *                                                   && '
        'echo   ===============================================================================================================  && '
        'echo     1.  Navigation:               Use the UP and DOWN arrow keys to navigate.                                      && '
        'echo     2.  Toggle:                   Press ENTER to select or deselect the current option.                            && '
        'echo     3.  Change Configuration:     Press \'C\' to modify configurations for the selected option.                    && '
        'echo     4.  Execution:                Press \'E\' to implement the tickmarked selections.                              && '
        'echo     5.  Save:                     Press \'S\' to preserve your current configuration to a file.                    && '
        'echo     6.  Refresh:                  Press \'R\' to clear the interface and refresh all information.                  && '
        'echo     7.  Help:                     Press \'H\' to open a separate window displaying instructions for program use.   && '
        'echo     8.  System Information:       Press \'I\' to display key system information in a new terminal window.          && '
        'echo     9.  Security policies:        Press \'P\' to use security policies module (GPO).                               && '
        'echo     10. Event Viewer:             Press \'V\' to use Event Viewer module                                           && '
        'echo     11. Quit:                     Press \'Q\' to close the application.                                            && '
        'echo. && pause'
    )
    os.system('start cmd /k "' + cmd + '"')
    stdscr.refresh()


def event_viewer():
    script_path = r'C:\Users\OSFortify\Event_Viewer_Module.ps1'
    subprocess.Popen(['powershell.exe', '-File', script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)


def security_policies():
    script_path = r'C:\Users\OSFortify\OSFortify_security_policies_module.ps1'
    subprocess.Popen(['powershell.exe', '-File', script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    
# FUNCTION - GENERATE SYSTEM INFO
def execute_system_informations():
    script = r'''
# Accounts information

$users = Get-WmiObject -Class Win32_UserAccount

Write-Output "------|User Accounts|----------------------------------------------------"
Write-Output "   "
foreach ($user in $users) {
    $currentUser = Get-WmiObject -Class Win32_ComputerSystem | Select-Object -ExpandProperty UserName
    $name = $user.Name
    $fullName = $user.FullName
    $accountType = $user.AccountType
    $sid = $user.SID
    
    Write-Output "    Currently logged-in Microsoft Account: $currentUser"
    Write-Output "    Username: $name$(if ($fullName) { " ($fullName)" })"
    Write-Output "        Account Type: $accountType"
    Write-Output "        SID: $sid"

    $isAdmin = $false

    # Check if the user is a member of the Administrators group
    $group = [ADSI]"WinNT://./Administrators"
    $members = $group.Invoke("Members") | ForEach-Object { $_.GetType().InvokeMember("Name", 'GetProperty', $null, $_, $null) }

    if ($members -contains $name) {
        $isAdmin = $true
    }

    if ($isAdmin) {
        Write-Output "        Privileges: Administrator"
    } else {
        Write-Output "        Privileges: Standard User"
    }

    $accountDisabled = $user.Disabled

    if ($accountDisabled) {
        Write-Output "        Account State: Disabled"
    } else {
        Write-Output "        Account State: Enabled"
    }
}
Write-Output "   "
# Windows specification
$os = Get-CimInstance Win32_OperatingSystem
$osCaption = $os.Caption
$osVersion = $os.Version
$osArchitecture = $os.OSArchitecture
$productKey = (Get-WmiObject -Query "SELECT * FROM SoftwareLicensingService").OA3xOriginalProductKey


Write-Output "------|Windows specification|--------------------------------------------"
Write-Output "   "
Write-Output "    Current Windows version: $osVersion"
Write-Output "    Windows architecture: $osArchitecture"
Write-Output "    Windows product key: $productKey"
Write-Output "   "
Write-Output "------|Hardware|---------------------------------------------------------"
# Processor
Write-Output "   "
$processor = Get-CimInstance Win32_Processor
$processorName = $processor.Name
$processorCores = $processor.NumberOfCores
$processorThreads = $processor.NumberOfLogicalProcessors

Write-Output "    Processor:"
Write-Output "        Name: $processorName"
Write-Output "        Number of Cores: $processorCores"
Write-Output "        Number of Threads: $processorThreads"

# Memory
$memory = (Get-CimInstance -Class Win32_PhysicalMemory).Capacity | Measure-Object -Sum
$memoryCapacity = $memory.Sum / 1GB

Write-Output "    RAM:"
Write-Output "        Total RAM Capacity: $memoryCapacity GB"

# Graphic Card
$graphicCard = Get-CimInstance Win32_VideoController
$graphicCardName = $graphicCard.Name

Write-Output "    Graphic Card:"
Write-Output "        Name: $graphicCardName"

# Discs
$disks = Get-CimInstance Win32_LogicalDisk | Where-Object {$_.DriveType -eq 3}
Write-Output "    Disks:"
foreach ($disk in $disks) {
    $diskID = $disk.DeviceID
    $diskCaption = $disk.Caption
    $diskSize = $disk.Size / 1GB
    $diskFreeSpace = $disk.FreeSpace / 1GB

    Write-Output "        Disk ID: $diskID"
    Write-Output "            Caption: $diskCaption"
    Write-Output "            Size: $diskSize GB"
    Write-Output "            Free Space: $diskFreeSpace GB"
}

# Network adapter
$networkAdapters = Get-CimInstance Win32_NetworkAdapter | Where-Object {$_.NetConnectionStatus -eq 2}
Write-Output "    Network Adapters:"
foreach ($adapter in $networkAdapters) {
    $adapterName = $adapter.Name
    $adapterConnectionID = $adapter.NetConnectionID
    $adapterMACAddress = $adapter.MACAddress

    Write-Output "        Adapter Name: $adapterName"
    Write-Output "            Connection ID: $adapterConnectionID"
    Write-Output "            MAC Address: $adapterMACAddress"
}
Write-Output "   "
#Security Features
Write-Output "------|Security Features|------------------------------------------------"
# Bitlocker
Write-Output "   "
$bitLockerVolumes = Get-BitLockerVolume
Write-Output "    BitLocker Status:"
foreach ($volume in $bitLockerVolumes) {
    $volumeMountPoint = $volume.MountPoint
    $volumeProtectionStatus = $volume.ProtectionStatus

    Write-Output "        Volume: $volumeMountPoint"
    Write-Output "            Protection Status: $volumeProtectionStatus"
}

# TPM module
# Check TPM status
$tpmStatus = Get-WmiObject -Namespace "Root\CIMv2\Security\MicrosoftTpm" -Class Win32_Tpm | Select-Object -ExpandProperty SpecVersion

if ($tpmStatus) {
    Write-Output "    TPM Status: Enabled (Version: $tpmStatus)"
} else {
    Write-Output "    TPM Status: Disabled"
}

# Check security processor status
$securityProcessorStatus = Get-CimInstance -Namespace "root\SecurityCenter2" -ClassName "AntivirusProduct" | Select-Object -ExpandProperty displayName

if ($securityProcessorStatus) {
    Write-Output "    Security Processor Status: Enabled (Antivirus: $securityProcessorStatus)"
} else {
    Write-Output "    Security Processor Status: Disabled"
}
Write-Output "   "
#Software Inventory
Write-Output "------|Software Inventory|----------------------------------------------"
Write-Output "   "
# Get list of installed software on the system
$SoftwareInventory = Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate

# Display the software inventory
Write-Output "    Software Inventory:"
$SoftwareInventory | Format-Table -AutoSize

# Retrieve package upgrade information
$upgradeInfo = winget upgrade

# Format the output into a table
$table = $upgradeInfo | Format-Table -AutoSize -Property PackageId, CurrentVersion, AvailableVersion, Source

# Output the formatted table
$table

# Export software inventory to a CSV file
$SoftwareInventory | Export-Csv -Path "C:\Users\OSFortify\Software_Inventory.csv" -NoTypeInformation

# Optional: Log the software inventory details to a text file
$SoftwareInventory | Out-File -FilePath "C:\Users\OSFortify\Software_Inventory.txt" -Append

'''
    script_path = "system_informations.ps1"
    with open(script_path, "w") as file:
        file.write(script)

    # Open a new PowerShell window and execute the script
    subprocess.Popen(["start", "powershell", "-ExecutionPolicy", "Bypass", "-NoExit", "-File", script_path], shell=True)

# FUNCTION - SAVE PROGRESS
def save_progress():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(r"Start-Transcript -Path 'C:\Users\OSFortify_Audit_Report.txt' -Append")
            file.write("\n")
            combined_objects = objects + objects2 + objects3
            for obj in combined_objects:
                if obj["tickmark"]:
                    value = obj["values"][configurations[index]['values'][0]]
                    file.write(f"{value}\n")
            file.write(r"Stop-Transcript")
            file.write("\n")
            file.write(r"Pause")



# FUNCTION - CHANGE CURRENT CONFIGURATION
def change_configuration():
    global index
    index = (index + 1) % len(configurations)
    display_objects()

# FUNCTION - TOGGLE TICKMARS
def toggle_tickmark(i):
    if i >= 0 and i < len(current_objects):
        current_objects[i]["tickmark"] = not current_objects[i]["tickmark"]
        display_objects()
    else:
        messagebox.showinfo("Information", "Tickmark position is out of index. Please move it to correct position.")
        pass

# FUNCTION - ENABLE ALL TICKMARKS
def enable_all_tickmarks():
    for obj_list in [objects, objects2, objects3, objects4]:
        for obj in obj_list:
            obj["tickmark"] = True
    display_objects()

# FUNCTION - DISABLE ALL TICKMARKS
def unmark_all_tickmarks():
    for obj_list in [objects, objects2, objects3, objects4]:
        for obj in obj_list:
            obj["tickmark"] = False
    display_objects()

# FUNCTION - REFRESH INTERFACE
def refresh_interface():
    try:
        # Refresh the display
        display_objects()
    except curses.error:
        pass

# FUNCTION - ASK FOR EXECUTION WINDOW
def confirm_execution():
    result = messagebox.askyesno("Confirmation", "Do you want to execute the code?")
    return result

# FUNCTION - EXECUTE CONFIGURATION
def execute_tickmarked_options():
    tickmarked_options = [obj for obj in objects if obj["tickmark"]]
    tickmarked_options2 = [obj for obj in objects2 if obj["tickmark"]]
    tickmarked_options3 = [obj for obj in objects3 if obj["tickmark"]]
    tickmarked_options4 = [obj for obj in objects4 if obj["tickmark"]]

    if tickmarked_options or tickmarked_options2 or tickmarked_options3 or tickmarked_options4:
        # Generate PowerShell commands
        commands = []
        total_commands = len(tickmarked_options) + len(tickmarked_options2) + len(tickmarked_options3) + len(tickmarked_options4)

        for obj in tickmarked_options:
            value = obj["values"][configurations[index]['values'][0]]
            if isinstance(value, str):
                commands.append(value)
                commands.append(f"Write-Progress -Activity 'Executing Commands' -Status 'Progress:' -PercentComplete (($i / {total_commands}) * 100); $i++")

        for obj in tickmarked_options2:
            value = obj["values"][configurations[index]['values'][0]]
            if isinstance(value, str):
                commands.append(value)
                commands.append(f"Write-Progress -Activity 'Executing Commands' -Status 'Progress:' -PercentComplete (($i / {total_commands}) * 100); $i++")

        for obj in tickmarked_options3:
            value = obj["values"][configurations[index]['values'][0]]
            if isinstance(value, str):
                commands.append(value)
                commands.append(f"Write-Progress -Activity 'Executing Commands' -Status 'Progress:' -PercentComplete (($i / {total_commands}) * 100); $i++")

        for obj in tickmarked_options4:
            value = obj["values"][configurations[index]['values'][0]]
            if isinstance(value, str):
                commands.append(value)
                commands.append(f"Write-Progress -Activity 'Executing Commands' -Status 'Progress:' -PercentComplete (($i / {total_commands}) * 100); $i++")        

        # Add the start and stop transcript commands
        commands.insert(0, "Start-Transcript -Path 'C:\\Users\\%USERPROFILE%\\Desktop\\transcript.txt' -Append")
        commands.append("Write-Output ''")
        commands.append("Write-Host '      Scripts have been executed successfully.' -ForegroundColor Green")
        commands.append("Write-Output ''")
        commands.append("Stop-Transcript")

        # Initialize progress counter
        commands.insert(0, "$i = 0")

        # Prompt for confirmation
        if confirm_execution():
            # Save the commands to a temporary script file
            script_file = "script.ps1"
            with open(script_file, "w") as file:
                file.write("\n".join(commands))

        # Execute the PowerShell script in a new PowerShell window
        try:
            os.system(f"start powershell -ExecutionPolicy Bypass -NoExit -File \"{script_file}\"")
        except Exception as e:
            print(f"An error occurred while executing the PowerShell script: {e}")

# FUNCTION - CHANGE CURRENT LIST OF OBJECTS
def next_objects_list():
    # GLOBAL VALUES
    global current_objects, graphic_position, cursor_position, position
    # RESET POSITIONS OF CURSOR
    position = 0  
    cursor_position = 0
    graphic_position = 0
    position = 0
    if current_objects is objects:
        current_objects = objects2
    elif current_objects is objects2:
        current_objects = objects3
    elif current_objects is objects3:
        current_objects = objects4
    else:
        current_objects = objects
    refresh_interface()

# MAIN PROGRAM LOOP
def main():
    global logical_position
    global graphic_position

    logical_position = 0
    graphic_position = 0

    init_curses()
    refresh_interface()
    global position
    position = 0

    while True:
        try:
            key = stdscr.getch()

            if key == curses.KEY_RESIZE:
                stdscr.erase()
                # Get the new screen size
                size = os.get_terminal_size()
                try:
                    curses.resizeterm(size.lines, size.columns)
                except AttributeError:
                    pass
                refresh_interface()
            elif key == curses.KEY_UP:
                if position > 0:
                    position -= 1
                    logical_position = max(logical_position - 1, 0)
                    graphic_position = max(graphic_position - 1, 0)
                    refresh_interface()
            elif key == curses.KEY_DOWN:
                if position < len(objects) - 1:
                    position += 1
                    logical_position = min(logical_position + 1, len(objects) - 1)
                    graphic_position = min(graphic_position + 1, len(objects) - 1)
                    refresh_interface()
            elif key == ord("\n"):
                toggle_tickmark(position)
                refresh_interface()
            elif key == ord("a") or key == ord("A"):
                enable_all_tickmarks()
            elif key == ord("u") or key == ord("U"):
                unmark_all_tickmarks()
            elif key == ord("s") or key == ord("S"):
                save_progress()
            elif key == ord("c") or key == ord("C"):
                change_configuration()
            elif key == ord("h") or key == ord("H"):
                display_help()
            elif key == ord("r") or key == ord("R"):
                refresh_interface()
            elif key == ord("e") or key == ord("E"):
                execute_tickmarked_options()
            elif key == ord("q") or key == ord("Q"):
                break
            elif key == ord("n") or key == ord("N"):
                next_objects_list()
            elif key == ord("p") or key == ord("P"):
                security_policies()
            elif key == ord("v") or key == ord("V"):
                event_viewer()
            if key == KEY_SYSTEM_INFORMATIONS:
                execute_system_informations()

            refresh_interface()

        except Exception as e:
            print(f"An error occurred in the main loop: {e}")

    cleanup_curses()

sys.stdin = open("nul", "r")

if __name__ == "__main__":
    main()
