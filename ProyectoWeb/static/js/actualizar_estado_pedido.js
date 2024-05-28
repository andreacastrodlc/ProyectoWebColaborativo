document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("form-estado");
    const btnActualizar = document.getElementById("btn-actualizar");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
    });

    btnActualizar.addEventListener("click", function (event) {
        event.preventDefault();
        const estado = document.getElementById("estado").value;
        const url = form.action;

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'estado': estado
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const estadoSpan = document.getElementById("estado-pedido");
                    estadoSpan.textContent = data.estado;
                    const pedidoItem = document.querySelector('.pedido-item');
                    pedidoItem.className = 'pedido-item pedido-' + estado.replace(" ", "_").toLowerCase();
                } else {
                    alert('Error: ' + data.error);
                }
            })
            .catch(error => console.error('Error:', error));
    });
});