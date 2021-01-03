import os

from config import RECIEVER_PIN, TRANSMITTER_PIN, DEFAULT_LENGTH
from lib.reciever import Reciever
from lib.transmitter import Transmitter


def menu():
    action = ""
    while action.lower() != "q":
        os.system("clear")
        print('''
    ,--.        ,---.,----. ,----.  
    `--' ,---. /    |'.-.  |'.-.  | 
    ,--.| .--'/  '  |  .' <   .' <  
    |  |\ `--.'--|  |/'-'  |/'-'  | 
    `--' `---'   `--'`----' `----'  

    [1] RECIEVE
    [2] SEND
    [Q] QUIT
        ''')

        answer = input("> ")

        if action == "1":
            reciever = Reciever(RECIEVER_PIN)
            reciever.start()
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
            print("Wrong action")
            time.sleep(1)



if __name__ == "__main__":
    menu()
