import os


print("Your PC will restart in less than 2 seconds.")
def restart_pc():
    if os.name == 'nt': #Check if the os is windows
        os.system('shutdown /r /t 1') #Restart the Pc with a delay of 1 second
    elif os.name == 'posix': #Check if the OS POSIX(Linux, Unix, macOS)
        os.system('sudo reboot') #Execute command to reboot the system
    else:
        print("Restart functionality not supported on this operating system.")

if __name__ == "__main__":
    restart_pc()