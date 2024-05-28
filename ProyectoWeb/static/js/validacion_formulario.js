document.addEventListener("DOMContentLoaded", function() {

            const form = document.getElementById("support-form");
            const mensajeError = document.getElementById("mensaje-error");
            const mensajeResaltado = document.getElementById("mensaje-resaltado");
            const palabrasProhibidas = ["palabra1", "palabra2", "palabra3"];
            //Event listener para el envio del formulario
            form.addEventListener("submit", function(event) {
                const mensajeInput = document.querySelector("textarea[name='mensaje']");
                const textoMensaje = mensajeInput.value;
                let tienePalabrasProhibidas = false;
                let palabrasEncontradas = [];

                // Recorre la lista de palabras prohibidas y comprobar si estan en el mensaje
                palabrasProhibidas.forEach(palabra => {
                    const regex = new RegExp(`\\b(${palabra})\\b`, 'gi');
                    if (regex.test(textoMensaje)) {
                        tienePalabrasProhibidas = true;
                        palabrasEncontradas.push(`<span class="highlight">${palabra}</span>`);
                    }
                });
                // Si hay palabras prohibidas previene el envio del formulario y se muestra un mensaje de error
                if (tienePalabrasProhibidas) {
                    event.preventDefault();
                    mensajeError.style.display = "block";
                    mensajeResaltado.style.display = "block";
                    mensajeResaltado.innerHTML = palabrasEncontradas.join(', ');
                } else {
                    mensajeError.style.display = "none";
                    mensajeResaltado.style.display = "none";
                }
            });
        });