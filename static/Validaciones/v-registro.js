document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username');
    const pnombre = document.getElementById('pnombre');
    const snombre = document.getElementById('snombre');
    const papellido = document.getElementById('papellido');
    const sapellido = document.getElementById('sapellido');
    const fecha_nacimiento = document.getElementById('fecha_nacimiento');
    const correo = document.getElementById('correo');
    const password = document.getElementById('password');
    const errorBox = document.getElementById('error-box');

    const errorUsername = document.getElementById('error-username');
    const errorPnombre = document.getElementById('error-pnombre');
    const errorSnombre = document.getElementById('error-snombre');
    const errorPapellido = document.getElementById('error-papellido');
    const errorSapellido = document.getElementById('error-sapellido');
    const errorFechaNacimiento = document.getElementById('error-fecha_nacimiento');
    const errorCorreo = document.getElementById('error-correo');
    const errorPassword = document.getElementById('error-password');

    let valid = true;

    function validateName(field, errorField, errorMessage) {
      const nameRegex = /^[a-zA-Z]+$/;
      if (field.value.trim() === '') {
        field.classList.add('error-field');
        errorField.textContent = errorMessage + ' es obligatorio.';
        errorField.style.display = 'block';
        valid = false;
      } else if (!nameRegex.test(field.value)) {
        field.classList.add('error-field');
        errorField.textContent = errorMessage + ' solo debe contener letras.';
        errorField.style.display = 'block';
        valid = false;
      } else {
        field.classList.remove('error-field');
        errorField.style.display = 'none';
      }
    }

    function validateEmail(field, errorField, errorMessage) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (field.value.trim() === '') {
        field.classList.add('error-field');
        errorField.textContent = errorMessage + ' es obligatorio.';
        errorField.style.display = 'block';
        valid = false;
      } else if (!emailRegex.test(field.value)) {
        field.classList.add('error-field');
        errorField.textContent = 'El ' + errorMessage + ' no es válido.';
        errorField.style.display = 'block';
        valid = false;
      } else {
        field.classList.remove('error-field');
        errorField.style.display = 'none';
      }
    }

    function validatePassword(field, errorField, errorMessage) {
      const passwordRegex = /^(?=.*[A-Z])(?=.*\d{3,})(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/;
      if (field.value.trim() === '') {
        field.classList.add('error-field');
        errorField.textContent = errorMessage + ' es obligatoria.';
        errorField.style.display = 'block';
        valid = false;
      } else if (!passwordRegex.test(field.value)) {
        field.classList.add('error-field');
        errorField.textContent = 'La ' + errorMessage + ' debe tener al menos 8 caracteres, incluir una letra mayúscula, tres dígitos y un carácter especial.';
        errorField.style.display = 'block';
        valid = false;
      } else {
        field.classList.remove('error-field');
        errorField.style.display = 'none';
      }
    }

    validateName(username, errorUsername, 'Nombre de usuario');
    validateName(pnombre, errorPnombre, 'Primer nombre');
    validateName(snombre, errorSnombre, 'Segundo nombre');
    validateName(papellido, errorPapellido, 'Primer apellido');
    validateName(sapellido, errorSapellido, 'Segundo apellido');

    if (fecha_nacimiento.value.trim() === '') {
      fecha_nacimiento.classList.add('error-field');
      errorFechaNacimiento.textContent = 'La fecha de nacimiento es obligatoria.';
      errorFechaNacimiento.style.display = 'block';
      valid = false;
    } else {
      fecha_nacimiento.classList.remove('error-field');
      errorFechaNacimiento.style.display = 'none';
    }

    validateEmail(correo, errorCorreo, 'correo electrónico');
    validatePassword(password, errorPassword, 'contraseña');

    if (!valid) {
      errorBox.textContent = 'Por favor, corrige los errores en el formulario.';
      errorBox.style.display = 'block';
    } else {
      errorBox.style.display = 'none';
      this.submit();
    }
  });
});
