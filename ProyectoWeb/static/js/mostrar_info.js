document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("btn-toggle");
    const infoBlock = document.getElementById("info");

    toggleButton.addEventListener("click", function () {
        if (infoBlock.style.display === "none" || infoBlock.style.display === "") {
            infoBlock.style.display = "block";
            toggleButton.textContent = "Ocultar Información";
        } else {
            infoBlock.style.display = "none";
            toggleButton.textContent = "Expandir Información";
        }
    });
});