import tkinter as tk
from tkinter import font
import os
import ctypes

HEIGHT = 800
WIDTH = 600

def first_part_response(hex_result, hex_string, x):
    try:
        final_str = 'UNICODE: %s \nUTF-8: %s \nCHAR: %c' % (hex_string, hex_result, x)
    except:
        final_str = "Kodavimas šio skaičiaus negali apdoroti"
    return final_str

def first_part(x):
    try:
        x = int(x)
        hex_string = hex(x)
        hex_string = hex_string.split('x', 2)[1]
        zero_count = 4 - len(hex_string)
        hex_string = ("U+" + ('0' * zero_count) + hex_string).upper()

        bin_string = bin(x)
        bin_string = bin_string.split('b', 2)[1]

        if x >= 0 and x <= 127:
            if len(bin_string) < 7:
                zero_count = 7 - len(bin_string)
            bin_string = ('0' * zero_count) + bin_string
            bin_result = "0" + bin_string
            hex_result = (hex(int(bin_result, 2)).split('x', 2)[1]).upper()
        elif x >= 128 and x <= 2047:
            if len(bin_string) < 11:
                zero_count = 11 - len(bin_string)
            bin_string = ('0' * zero_count) + bin_string
            bin_result1 = "110" + bin_string[0:5]
            bin_result2 = "10" + bin_string[5:11]
            hex_result = (hex(int(bin_result1, 2)).split('x', 2)[1] + " " + hex(int(bin_result2, 2)).split('x', 2)[
                1]).upper()

        elif x >= 2048 and x <= 65535:
            if len(bin_string) < 16:
                zero_count = 16 - len(bin_string)
            bin_string = ('0' * zero_count) + bin_string
            bin_result1 = "1110" + bin_string[0:4]
            bin_result2 = "10" + bin_string[4:10]
            bin_result3 = "10" + bin_string[10:16]
            hex_result = (hex(int(bin_result1, 2)).split('x', 2)[1] + " " + hex(int(bin_result2, 2)).split('x', 2)[
                1] + " " + hex(int(bin_result3, 2)).split('x', 2)[1]).upper()
        elif x >= 65536:
            if len(bin_string) < 21:
                zero_count = 21 - len(bin_string)
            bin_string = ('0' * zero_count) + bin_string
            bin_result1 = "11110" + bin_string[0:3]
            bin_result2 = "10" + bin_string[3:9]
            bin_result3 = "10" + bin_string[9:15]
            bin_result4 = "10" + bin_string[15:21]
            hex_result = (hex(int(bin_result1, 2)).split('x', 2)[1] + " " + hex(int(bin_result2, 2)).split('x', 2)[
                1] + " " + hex(int(bin_result3, 2)).split('x', 2)[1] + " " + hex(int(bin_result4, 2)).split('x', 2)[
                              1]).upper()
    except:
        final_str = "Kodavimas šio skaičiaus negali apdoroti"

    label['text'] = first_part_response(hex_result, hex_string, x)


def second_part():
    codepage437 = {}
    with open('CP437.txt', 'r') as f:
        for line in f:
            (key, val) = line.split()
            codepage437[int(key)] = val
    results_file = open("output.txt", "w+", encoding='utf-8')
    with open("386intel.txt") as fileobj:
        for line in fileobj:
            for ch in line:
                if ord(ch) > 127 and ord(ch) < 256:
                    cp437 = codepage437[ord(ch)]
                    cp437 = int(cp437, 16)
                    #print(chr(cp437))
                    results_file.write(chr(cp437))
                else:
                    results_file.write(ch)
    encode_done = ctypes.windll.user32.MessageBoxW
    encode_done(None, '\"386intel\" sėkmingai atkoduotas', 'Operacija atlikta', 0)


def view_file():
    if os.path.isfile("output.txt"):
        os.system("start " + "output.txt")
    else:
        no_file = ctypes.windll.user32.MessageBoxW
        no_file(None, 'Rezultatų failas neegzistuoja. Pabandykite dar kartą', 'Failas nerastas', 0)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Lucida Sans Unicode', 15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="GO!", font=('Lucida Sans Unicode', 15), command=lambda: first_part(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.4, anchor='n')

label = tk.Label(lower_frame, font=('Lucida Sans Unicode', 15))
label.place(relwidth=1, relheight=1)

second_frame = tk.Frame(root, bg='#80c1ff', bd=5)
second_frame.place(relx=0.5, rely=0.7, relwidth=0.75, relheight=0.1, anchor='n')

encode_button = tk.Button(second_frame, text="Atkoduoti \"386intel\" failą", font=('Lucida Sans Unicode', 10), command=lambda: second_part())
encode_button.place(relwidth=0.45, relheight=1)

output_button = tk.Button(second_frame, text="Peržvelgti rezultatų failą", font=('Lucida Sans Unicode', 10), command=lambda: view_file())
output_button.place(relx=0.55, relwidth=0.45, relheight=1)

root.mainloop()