function verificarNumeroOS() {
    const valor = document.getElementById('os-number').value;
    if (valor != ''){
    fetch(`/verify_os/?os_number=${valor}`)
        .then(response => response.json())
        .then(data => {
            const span = document.getElementById('os-error');
            const confirm = document.getElementById('confirm');
            if (data.existe) {
                span.style.display = 'block';
                confirm.disabled = true;
            } else {
                span.style.display = 'none';
                confirm.disabled = false;
            }
        });
    }
}