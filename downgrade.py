#import modules that make this program work
import subprocess
print (" _    ___  __      ___                                               _             ")
print ("(_)  /___\/ _\    /   \ ___ __      __ _ __    __ _  _ __  __ _   __| |  ___  _ __ ")
print ("| | //  //\ \    / /\ // _ \\ \ /\ / /| '_ \  / _` || '__|/ _` | / _` | / _ \| '__|")
print ("| |/ \_// _\ \  / /_//| (_) |\ V  V / | | | || (_| || |  | (_| || (_| ||  __/| |   ")
print ("|_|\___/  \__/ /___,'  \___/  \_/\_/  |_| |_| \__, ||_|   \__,_| \__,_| \___||_|   ")
print ("                                              |___/                                ")
print ("This program only works on the following 32bit iOS devices")
print ("iPhone 4, 4S, 5, 5C, iPod Touch 4G, 5G, iPad 2, 3, 4, Mini 1st Gen")
print ("The device needs to be in kDFU")

#ask the user for their blob and ipsw
blob = input("Path to SHSH blob: ")
ipsw = input("Path to ipsw: ")
bb = input("Flash baseband? (Select n for Wi-Fi-only devices)[y/n]:")


#start the restore
if bb == 'y':	
	subprocess.call(['./futurerestore_macos', '--latest-baseband', '--use-pwndfu', '-t', blob, ipsw])
else:
	subprocess.call(['./futurerestore_macos', '--no-baseband', '--use-pwndfu', '-t', blob, ipsw])
