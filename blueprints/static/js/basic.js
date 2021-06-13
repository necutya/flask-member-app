document.addEventListener("DOMContentLoaded", (event) => {
    const messageCloseIcons = document.querySelectorAll('.icon-cross');
    messageCloseIcons.forEach((icon) => {
        icon.addEventListener('click', (event) => {
           event.target.parentElement.parentElement.remove();
        });
    });
});