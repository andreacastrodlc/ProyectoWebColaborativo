function validateForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var error = document.getElementById("error");
    error.innerHTML = "";
}

 //<script> PRUEBA PARA CAMBIAR SOLICITUD

    const palabrasProhibidas = ["palabra1", "palabra2", "palabra3"];


    function validarMensaje(event) {
    const mensaje = event.target.value;
    let mensajeModificado = mensaje;

    palabrasProhibidas.forEach(palabra => {
    const regex = new RegExp(`\\b(${palabra})\\b`, 'gi');
    mensajeModificado = mensajeModificado.replace(regex, '<span class="highlight">$1</span>');
});


    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = mensajeModificado;

    const textoPlano = tempDiv.textContent || tempDiv.innerText || "";


    event.target.value = textoPlano;


    document.getElementById('mensaje-preview').innerHTML = mensajeModificado;
}


    document.addEventListener('DOMContentLoaded', () => {
    const textarea = document.querySelector('textarea[name="mensaje"]');
    textarea.addEventListener('input', validarMensaje);
    })//;
</script>
