import os

HiddenSrvPath = "/var/lib/tor/Hidden_Service/"
torrcPath = "/etc/tor/torrc"

def installTor():
    print("[i] installing...")
    cmd = os.popen("apt install tor -y")
    print(cmd.read())
    print("Done!")
    menu()

def hidSrv():
    #step 1: install web engine
    print("Step 1: install web engine. (not responsible for any error)")
    ask1 = input("Have you installed any web engine on this system? (Y/N): ")
    if ask1 == "Y":
        print("[i] Skipped web engine installation...")
    elif ask1 == "N":
        ask2 = input("Input web engine name to install, i.e. apt install ->: ")
        cmd = os.popen(f"apt install {ask2} -y")
        print(cmd.read())

    #Step 2: configure hidden service
    print("\nStep 2: configure hidden service")
    print("[i] Installing tor...")
    cmd = os.popen("apt install tor -y")
    print(cmd.read())

    print("[i] Adding something important to torrc file...")
    torrc = None
    if not os.path.exists(torrcPath):
        print("[w] Config file doesn't exist... creating one...")
        open(torrcPath,'w').write('')
    
    torrc = open(torrcPath, 'a')

    ask3 = input("Input port no. of your localhost (usually 80/8080): ")
    ask4 = input("Input port no. of your hidden service: ")

    try:
        print(f"[i] Configured port no. of your localhost to {int(ask3)}")
    except:
        ask3 = 80
        print("[e] You entered something invalid, so configured port no. of your localhost to 80")

    try:
        print(f"[i] Configured port no. of your hidden service to {int(ask4)}")
    except:
        ask4 = 80
        print("[e] You entered something invalid, so configured port no. of your hidden service to 80")

    
    print(f"[i] The path of the hidden service is configured to '{HiddenSrvPath}'")
    
    torrc.write(f"\nHiddenServiceDir {HiddenSrvPath}\nHiddenServicePort {ask4} 127.0.0.1:{ask3}")

    print(f"[i] Torrc config ok! (You may find and modify torrc file (path: '{torrcPath}')")
    print("[i] What to do next: issue command 'tor' to start the hidden service, and make sure web engine's service is also enabled.")
    

def removeTor():
    print("Removing tor...")
    cmd = os.popen("apt remove tor -y")
    print(cmd.read())
    print("cleaning up...")
    os.popen("rm -r /var/lib/tor/")
    os.popen("rm -r /etc/tor/")

    print("Done!")
    menu()

def checkHiddenSrv():
    try:
        print(f"[i] Your hidden service link is: {open(f'{HiddenSrvPath}hostname').read()}")
    except:
        print("[e] Unable to fetch hidden service link... (probably the hidden service is not installed in the default path)")

    menu()

def menu():
    option = int(input("\nSelect:\n (1) Simply install Tor, (2) Install Tor with hidden service configured, (3) Check hidden service link, (4) Clean remove Tor, (5) Exit\nYour option: "))

    if option == 1:
        installTor()
    elif option == 2:
        hidSrv()
    elif option == 3:
        checkHiddenSrv()
    elif option == 4:
        removeTor()
    elif option == 5:
        exit()


print("Note: You must run this script in Root level.")
print("Note: You may customize the paths (hidden service/ torrc file) by editing this script.")



menu()