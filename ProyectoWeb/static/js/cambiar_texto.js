        document.addEventListener("DOMContentLoaded", function() {
            const botonAumentar = document.getElementById("btn-aumentar");
            const botonDisminuir = document.getElementById("btn-disminuir");

            botonAumentar.addEventListener("click", function() {
                const elements = document.querySelectorAll("h1, h2, p");

                elements.forEach(element => {
                    const currentFontSize = window.getComputedStyle(element).fontSize;
                    element.style.fontSize = parseFloat(currentFontSize) * 1.2 + "px";
                });
            });

            botonDisminuir.addEventListener("click", function() {
                const elements = document.querySelectorAll("h1, h2, p");

                elements.forEach(element => {
                    const currentFontSize = window.getComputedStyle(element).fontSize;
                    element.style.fontSize = parseFloat(currentFontSize) / 1.2 + "px";
                });
            });
        });