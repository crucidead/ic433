import os
import time

from colorama import Fore, Back

from config import RECEIVER_PIN, TRANSMITTER_PIN, DEFAULT_LENGTH
from lib.receiver import Receiver
from lib.transmitter import Transmitter


def print_menu():
    print(f'''{Fore.CYAN} 
        ,--.        ,---.,----. ,----.  
        `--' ,---. /    |'.-.  |'.-.  | 
        ,--.| .--'/  '  |  .' <   .' <  
        |  |\ `--.'--|  |/'-'  |/'-'  | 
        `--' `---'   `--'`----' `----'  
        {Back.YELLOW}{Fore.RESET}do not harm{Back.RESET}
        {Fore.GREEN}:: version: 0.1 ::
        
        {Fore.CYAN} - 1 - {Fore.RESET}RECEIVE
        {Fore.CYAN} - 2 - {Fore.RESET}SEND
        {Fore.CYAN} - Q - {Fore.RESET}QUIT
            ''')


def menu():
    action = ""
    while action.lower() != "q":
        os.system("clear")
        print_menu()

        action = input("> ")

        if action == "1":
            receiver = Receiver(RECEIVER_PIN)
            receiver.start()
        elif action == "2":
            code = int(input("Code: "))
            plength = int(input("Pulse length: "))
            proto = int(input("Protocol: "))
            repeat = int(input("Repeat: ")) or 1

            if repeat < 1:
                repeat = 1

            sender = Transmitter(TRANSMITTER_PIN, code, plength, proto, DEFAULT_LENGTH, repeat)
            sender.start()
        elif action.lower() != "q":
            print(Fore.RED + "Wrong action")
            time.sleep(1)


if __name__ == "__main__":
    menu()
