#import modules that make this program work
import os
import subprocess
print (" _    ___  __      ___                                               _             ")
print ("(_)  /___\/ _\    /   \ ___ __      __ _ __    __ _  _ __  __ _   __| |  ___  _ __ ")
print ("| | //  //\ \    / /\ // _ \\ \ /\ / /| '_ \  / _` || '__|/ _` | / _` | / _ \| '__|")
print ("| |/ \_// _\ \  / /_//| (_) |\ V  V / | | | || (_| || |  | (_| || (_| ||  __/| |   ")
print ("|_|\___/  \__/ /___,'  \___/  \_/\_/  |_| |_| \__, ||_|   \__,_| \__,_| \___||_|   ")
print ("                                              |___/                                ")
print ("[Info] This program only works on the following 32bit iOS devices")
print ("[Info] iPhone 4, 4S, 5, 5C, iPod Touch 4G, 5G, iPad 2, 3, 4, Mini 1st Gen")
print ("[Info] The device needs to be in kDFU")

#ask user for the path to the futurerestore executable (helps with multi platform support)
executable_path = input("[User input] Path to futurerestore executable (eg. futurerestore_macos): ")

#ask the user for their blob and ipsw
blob = input("[User input] Path to SHSH blob: ")
ipsw = input("[User input] Path to ipsw: ")

#start a loop to stop user from accidentally flashing without baseband
while True:
	bb = input("[User input] Flash baseband? (Select n for Wi-Fi-only devices)[y/n]:")
	if bb != "y" or "n":
		print("Please enter a valid option!")
		continue


#start the restore
print("[Info] Starting the restore... If your device doesn't do anything then you probably typed something in wrong.")
if bb == 'y':	
	subprocess.call([executable_path, '--latest-baseband', '--use-pwndfu', '-t', blob, ipsw])
else:
	subprocess.call([executable_path, '--no-baseband', '--use-pwndfu', '-t', blob, ipsw])
	
