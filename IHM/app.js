
document.getElementById('syracuseForm').addEventListener('submit', async function (event) {
    event.preventDefault();
    const number = document.getElementById('numberInput').value;

    try {
        const response = await fetch('http://localhost:5000/syracuse', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ number: parseInt(number) })
        });
        const data = await response.json();
        document.getElementById('results').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    } catch (error) {
        console.error("Erreur lors de l'appel au service Syracuse", error);
    }
});
