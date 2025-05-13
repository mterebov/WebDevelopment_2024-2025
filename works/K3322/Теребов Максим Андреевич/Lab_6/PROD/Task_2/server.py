import socket

HOST = '127.0.0.1'
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Математический сервер запущен на {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Клиент подключился: {addr}")
            data = conn.recv(1024).decode()
            print("Полученные данные:", data)
            a, b, h = map(float, data.split(','))
            s_trap = ((a + b) / 2) * h
            conn.send(f"Площадь трапеции: {s_trap}".encode())
