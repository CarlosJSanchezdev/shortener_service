document.getElementById('shorten-form').addEventListener('submit', async (e) => {
    e.preventDefault(); // Evita que el formulario se envíe de forma tradicional

    const urlInput = document.getElementById('url-input');
    const shortUrlElement = document.getElementById('short-url');

    // Limpia el resultado anterior
    shortUrlElement.textContent = '';
    shortUrlElement.href = '';

    try {
        // Envía la URL al backend
        const response = await fetch('/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: urlInput.value }),
        });

        if (!response.ok) {
            throw new Error('Error al acortar la URL');
        }

        const data = await response.json();

        // Muestra la URL acortada
        shortUrlElement.textContent = data.short_url;
        shortUrlElement.href = data.short_url;
    } catch (error) {
        console.error('Error:', error);
        alert('Ocurrió un error al acortar la URL. Inténtalo de nuevo.');
    }
});