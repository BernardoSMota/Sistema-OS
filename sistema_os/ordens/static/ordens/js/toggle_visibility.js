const button = document.getElementById('edit-os')
button.addEventListener("click", function () {
    const form = document.getElementById('form-os-number');
    if (form.style.opacity == "1") {
        form.style.opacity = '0';
    } else {
        form.style.opacity = '1';
    }
});
