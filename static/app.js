document.getElementById('calculateBtn').addEventListener('click', () => {
    const numberInput = document.getElementById('numberInput').value;
    const resultElement = document.getElementById('result');

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ number: numberInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultElement.textContent = `Error: ${data.error}`;
        } else {
            resultElement.textContent = `Result: ${data.result}`;
        }
    })
    .catch(error => {
        resultElement.textContent = 'Error: Could not connect to server.';
        console.error('Error:', error);
    });
});