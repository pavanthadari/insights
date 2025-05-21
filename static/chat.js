function sendChat() {
    const input = document.getElementById('chat-input');
    const msg = input.value;
    fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: msg})
    })
    .then(res => res.json())
    .then(data => {
        const history = document.getElementById('chat-history');
        history.innerHTML += `<div><b>You:</b> ${msg}</div><div><b>Bot:</b> ${data.response}</div>`;
        input.value = '';
    });
}