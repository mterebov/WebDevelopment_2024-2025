import socket

HOST = '127.0.0.1'
PORT = 12346

a = float(input("Введите основание a: "))
b = float(input("Введите основание b: "))
h = float(input("Введите высоту h: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(f"{a},{b},{h}".encode())
    result = s.recv(1024).decode()
    print("Ответ от сервера:", result)
