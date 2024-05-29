@echo off
netsh wlan show interfaces | findstr /C:"SSID"