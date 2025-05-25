const inputFotos = document.getElementById('pictures');
const container = document.getElementById('pictures-container');

inputFotos.addEventListener('change', () => {
    container.innerHTML = '';

    const files = inputFotos.files;

    if(files.length === 0) {
        return;
    }
    container.style.display = 'flex'

    for(let i = 0; i < files.length; i++) {
        const file = files[i];

        if(!file.type.startsWith('image/')) continue;

        const img = document.createElement('img');
        img.style.maxWidth = '100px';
        img.style.height = 'auto';
        img.style.marginRight = '10px';
        img.style.marginBottom = '10px';
        img.style.borderRadius = '8px';

        img.src = URL.createObjectURL(file);

        container.appendChild(img);
    }
});
