// Ensure script works correctly once page finishes loading
document.addEventListener('DOMContentLoaded', () => {
    console.log("Arqade homepage scripts loaded successfully.");

    const mainTitle = document.getElementById('main-title');

    if (mainTitle) {
        // Visual text pulse trigger when user moves cursor onto logo
        mainTitle.addEventListener('mouseenter', () => {
            mainTitle.classList.add('pulse');
        });

        // Return title to normal size on cursor exit
        mainTitle.addEventListener('mouseleave', () => {
            mainTitle.classList.remove('pulse');
        });
    }
});
