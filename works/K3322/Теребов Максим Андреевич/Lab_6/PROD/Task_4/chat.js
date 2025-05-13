const ws = new WebSocket("ws://localhost:8765");
const chat = document.getElementById("chat");
const msgInput = document.getElementById("msg");

let nickname = ""; // Инициализируем переменную
let nicknameSet = false;

ws.onmessage = (event) => {
    const msg = event.data;
    
    if (!nicknameSet && msg === "Введите никнейм:") {
        const inputNickname = prompt("Введите ваш никнейм:");
        if (inputNickname) {
            nickname = inputNickname; // Сохраняем введенный ник
            ws.send(nickname);
            nicknameSet = true;
        }
        return;
    }
    
    if (msg.includes("Никнейм уже занят")) {
        alert(msg);
        ws.close();
        return;
    }
    
    const messageElement = document.createElement("div");
    messageElement.textContent = msg;
    
    // Определяем тип сообщения
    if (msg.includes("присоединился") || msg.includes("покинул")) {
        messageElement.className = "system-message";
    } else if (nickname && msg.startsWith(`${nickname}:`)) {
        messageElement.className = "user-message";
    } else {
        messageElement.className = "other-message";
    }
    
    chat.appendChild(messageElement);
    chat.scrollTop = chat.scrollHeight;
};

function sendMessage() {
    const text = msgInput.value.trim();
    if (text && nicknameSet) {
        ws.send(text);
        msgInput.value = "";
    }
}

msgInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") sendMessage();
});

ws.onclose = () => {
    const messageElement = document.createElement("div");
    messageElement.className = "system-message";
    messageElement.textContent = "Соединение закрыто";
    chat.appendChild(messageElement);
};