// Obtener el botón y el formulario
var btnConsulta = document.getElementById("btnConsulta");
var formulario = document.getElementById("formularioConsulta");
var btnConsultar = document.getElementById("btnConsultar");
var btnSalir = document.getElementById("btnSalir");
var saldoActual = null;
var formularioMostrado = false;

// Agregar el evento de clic al botón
btnConsulta.addEventListener("click", function() {
    // Mostrar el formulario como una pestaña emergente solo si no se ha mostrado antes
    if (!formularioMostrado) {
        formulario.style.display = "block";
        formularioMostrado = true;
    }
});

// Agregar el evento de clic al botón de salir
btnSalir.addEventListener("click", function() {
    formulario.style.display = "none";
    formularioMostrado = false;
    document.getElementById("tarjetaId").value = "";
    document.getElementById("saldo").textContent = "";
});

// Agregar el evento de clic al botón de consultar saldo
btnConsultar.addEventListener("click", function() {
    const tarjetaId = document.getElementById("tarjetaId").value;
    fetch(`https://api.xor.cl/red/balance/${tarjetaId}`)
        .then(response => response.json())
        .then(data => {
            // Verificar si el saldo actual es diferente al saldo anterior
            if (data.balance !== saldoActual) {
                saldoActual = data.balance;
                document.getElementById("saldo").textContent = `El saldo de su Tarjeta Bip es de $${data.balance}`;
            }
        })
        .catch(error => {
            document.getElementById("saldo").textContent = "No se pudo consultar el saldo de su Tarjeta Bip en este momento. Inténtelo de nuevo más tarde.";
        });
});