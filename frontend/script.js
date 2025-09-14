document.getElementById('certificateForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        last_name: document.getElementById('last_name').value,
        cedula: document.getElementById('cedula').value,
        expedida_en: document.getElementById('expedida_en').value,
        mes: document.getElementById('mes').value
    };

    const response = await fetch('/certificate/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
    });

    if (response.ok) {
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'certificado.pdf';
        a.click();
    } else {
        alert('Error al generar el certificado');
    }
});