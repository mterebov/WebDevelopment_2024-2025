import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"HTTP-сервер запущен на http://{HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024)
            print(f"Запрос от {addr}:\n{request.decode()}")

            with open("PROD\Task_3\index.html", "r", encoding="utf-8") as file:
                html_content = file.read()

            response = (
                "HTTP/1.1 200 OK\n"
                "Content-Type: text/html\n"
                f"Content-Length: {len(html_content.encode())}\n\n"
                f"{html_content}"
            )
            conn.sendall(response.encode())
