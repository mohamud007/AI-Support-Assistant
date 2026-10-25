
const chatForm = document.getElementById("chatForm");
const questionInput = document.getElementById("questionInput");
const chatMessages = document.getElementById("chatMessages");

function addMessage(message, className) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", className);
    messageElement.textContent = message;

    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    return messageElement;
}

chatForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const question = questionInput.value.trim();

    if (!question) {
        return;
    }

    addMessage(question, "user-message");
    questionInput.value = "";
    questionInput.disabled = true;

    const sendButton = chatForm.querySelector("button");
    sendButton.disabled = true;
    sendButton.textContent = "Sending...";

    const loadingMessage = addMessage(
        "Thinking...",
        "bot-message"
    );

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Request failed.");
        }

        loadingMessage.textContent =
            data.answer || "Sorry, I couldn't find an answer.";

    } catch (error) {
        loadingMessage.textContent =
            "Sorry, something went wrong. Please try again.";

        console.error("Chat error:", error);

    } finally {
        questionInput.disabled = false;
        sendButton.disabled = false;
        sendButton.textContent = "Send";
        questionInput.focus();
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
