const chatContainer = document.getElementById("chat-container");
const chatInput = document.getElementById("chat-input");
const sendBtn = document.getElementById("send-btn");

function appendMessage(text, isUser = false) {
  const el = document.createElement("div");
  el.className = isUser ? "text-right text-blue-600" : "text-left text-gray-700";
  el.innerText = text;
  chatContainer.appendChild(el);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

sendBtn.addEventListener("click", async () => {
  const message = chatInput.value.trim();
  if (!message) return;

  appendMessage("You: " + message, true);
  chatInput.value = "";

  try {
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    appendMessage("Bot: " + data.reply);
  } catch (err) {
    appendMessage("⚠️ Error connecting to backend");
  }
});
