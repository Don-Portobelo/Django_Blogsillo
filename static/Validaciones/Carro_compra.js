
// Esperamos que todos los elementos de la página carguen para ejecutar el script
document.addEventListener('DOMContentLoaded', ready);

function ready() {
    // Agregamos funcionalidad al botón Agregar al carrito
    var botonesAgregarAlCarrito = document.getElementsByClassName('boton-item');
    for (var i = 0; i < botonesAgregarAlCarrito.length; i++) {
        var button = botonesAgregarAlCarrito[i];
        button.addEventListener('click', agregarAlCarritoClicked);
    }
}

function agregarAlCarritoClicked(event) {
    var button = event.target;
    var item = button.parentElement; // Accedemos al contenedor del elemento que queremos agregar
    var titulo = item.querySelector('.titulo-item').innerText; // Usamos querySelector para obtener el título
    var precio = item.querySelector('.precio-item').innerText; // Usamos querySelector para obtener el precio
    var imagenSrc = item.querySelector('.img-item').src; // Usamos querySelector para obtener la fuente de la imagen

    agregarAlCarrito(titulo, precio, imagenSrc); // Llamamos a la función para agregar al carrito
}

// Por ejemplo, de manera estática si la URL no cambia
const urlAgregarAlCarrito = 'tienda/fantasia/agregar_al_carrito/';

function agregarAlCarrito(libroId, nombreLibro, precioLibro) {
    // Verifica si precioLibro es null o undefined
    if (precioLibro === null || precioLibro === undefined) {
        console.error('El precio del libro no está definido correctamente.');
        return;
    }

    fetch('/tienda/agregar_al_carrito/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            'libro_id': 123,  // Aquí debes proporcionar el ID del libro correcto
            'nombre_libro': 'Nombre del Libro',  // Aquí debes proporcionar el nombre del libro correcto
            'precio_libro': 29.99  // Aquí debes proporcionar el precio del libro correcto
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error al agregar al carrito');
        }
        return response.json();
    })
    .then(data => {
        console.log('Respuesta del servidor:', data);
    })
    .catch(error => {
        console.error('Error en la solicitud:', error);
    });
}

function actualizarVistaCarrito(data) {
    var itemsCarrito = document.getElementsByClassName('carrito-items')[0];
    
    var item = document.createElement('div');
    item.classList.add('carrito-item');
    
    var itemCarritoContenido = `
        <img src="${data.imagen_src}" width="80px" alt="">
        <div class="carrito-item-detalles">
            <span class="carrito-item-titulo">${data.nombre_libro}</span>
            <div class="selector-cantidad">
                <i class="fa-solid fa-minus restar-cantidad"></i>
                <input type="text" value="1" class="carrito-item-cantidad" disabled>
                <i class="fa-solid fa-plus sumar-cantidad"></i>
            </div>
            <span class="carrito-item-precio">${data.precio_libro}</span>
        </div>
        <button class="btn-eliminar">
            <i class="fa-solid fa-trash"></i>
        </button>
    `;
    
    item.innerHTML = itemCarritoContenido;
    itemsCarrito.appendChild(item);

    // Agregamos la funcionalidad eliminar al nuevo item
    item.querySelector('.btn-eliminar').addEventListener('click', eliminarItemCarrito);

    // Agregamos la funcionalidad restar cantidad del nuevo item
    item.querySelector('.restar-cantidad').addEventListener('click', restarCantidad);

    // Agregamos la funcionalidad sumar cantidad del nuevo item
    item.querySelector('.sumar-cantidad').addEventListener('click', sumarCantidad);

    // Actualizamos total
    actualizarTotalCarrito();
}

function hacerVisibleCarrito() {
    var carrito = document.getElementsByClassName('carrito')[0];
    carrito.style.marginRight = '0';
    carrito.style.opacity = '1';

    var items = document.getElementsByClassName('contenedor-items')[0];
    items.style.width = '60%';
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Otras funciones relacionadas con el carrito de compras (eliminar, restar cantidad, sumar cantidad, etc.)
// Función para restar la cantidad de un artículo en el carrito
function restarCantidad(event) {
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    var cantidadActual = parseInt(selector.querySelector('.carrito-item-cantidad').value);
    cantidadActual--;
    if (cantidadActual >= 1) {
        selector.querySelector('.carrito-item-cantidad').value = cantidadActual;
        actualizarTotalCarrito();
    }
}

// Función para sumar la cantidad de un artículo en el carrito
function sumarCantidad(event) {
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    var cantidadActual = parseInt(selector.querySelector('.carrito-item-cantidad').value);
    cantidadActual++;
    selector.querySelector('.carrito-item-cantidad').value = cantidadActual;
    actualizarTotalCarrito();
}

// Función para eliminar un artículo del carrito
function eliminarItemCarrito(event) {
    var buttonClicked = event.target;
    var item = buttonClicked.parentElement.parentElement;
    var titulo = item.querySelector('.carrito-item-titulo').innerText;
    eliminarDelCarrito(titulo); // Llama a la función para eliminar del carrito (se pasa el título como identificador)
    item.remove(); // Elimina visualmente el elemento del DOM
    actualizarTotalCarrito(); // Actualiza el total del carrito
}

// Función para eliminar un artículo del carrito en el backend
function eliminarDelCarrito(nombreLibro) {
    fetch("{% url 'eliminar_del_carrito' %}", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            'nombre_libro': nombreLibro
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(`Eliminando ${nombreLibro} del carrito`);
        // Aquí podrías actualizar la vista del carrito si es necesario
        if (data.carrito_vacio) {
            ocultarCarrito(); // Si el carrito queda vacío después de eliminar, ocultamos el carrito
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Función para actualizar el total del carrito
function actualizarTotalCarrito() {
    var carritoItems = document.getElementsByClassName('carrito-items')[0];
    var total = 0;

    // Recorremos cada elemento del carrito para actualizar el total
    var carritoItemsList = carritoItems.getElementsByClassName('carrito-item');
    for (var i = 0; i < carritoItemsList.length; i++) {
        var item = carritoItemsList[i];
        var precioElemento = item.querySelector('.carrito-item-precio');
        var precio = parseFloat(precioElemento.innerText.replace('$', '').replace('.', ''));
        var cantidadItem = parseInt(item.querySelector('.carrito-item-cantidad').value);
        total += precio * cantidadItem;
    }
    total = Math.round(total * 100) / 100;

    // Actualizamos el elemento en la página que muestra el total
    document.getElementsByClassName('carrito-precio-total')[0].innerText = '$' + total.toLocaleString("es");

    // Si el total es 0, ocultamos el carrito
    if (total === 0) {
        ocultarCarrito();
    }
}

// Función que controla si hay elementos en el carrito. Si no hay, ocultamos el carrito.
function ocultarCarrito() {
    var carrito = document.getElementsByClassName('carrito')[0];
    carrito.style.marginRight = '-100%';
    carrito.style.opacity = '0';

    var items = document.getElementsByClassName('contenedor-items')[0];
    items.style.width = '100%';

    carritoVisible = false; // Actualizamos el estado del carrito a no visible
}
