$(document).ready(function() {
    $('form').submit(function(event) {
      event.preventDefault(); // Evitar que el formulario se envíe automáticamente
  
      // Validación de campos
var username = $('#username').val();
var firstName = $('#first-name').val();
var lastName = $('#last-name').val();
var birthdate = $('#birthdate').val();
var email = $('#email').val();
var phone = $('#phone').val();
var password = $('#password').val();
var securityQuestion = $('#security-question').val();
var securityAnswer = $('#security-answer').val();

var error = false;

if (!/^[a-zA-Z0-9\-]+$/.test(username)) {
  if(!$('#username').next().hasClass('error')) {
    $('#username').after('<span class="error">Solo se permiten letras, guiones medios y números.</span>');
  }
  error = true;
}

if (!/^[a-zA-Z]+$/.test(firstName)) {
  if(!$('#first-name').next().hasClass('error')) {
    $('#first-name').after('<span class="error">Solo se permiten letras.</span>');
  }
  error = true;
}

if (!/^[a-zA-Z]+$/.test(lastName)) {
  if(!$('#last-name').next().hasClass('error')) {
    $('#last-name').after('<span class="error">Solo se permiten letras.</span>');
  }
  error = true;
}

if (!/^\d{4}-\d{2}-\d{2}$/.test(birthdate)) {
  if(!$('#birthdate').next().hasClass('error')) {
    $('#birthdate').after('<span class="error">El formato de la fecha debe ser AAAA-MM-DD.</span>');
  }
  error = true;
}

if (!/\S+@\S+\.\S+/.test(email)) {
  if(!$('#email').next().hasClass('error')) {
    $('#email').after('<span class="error">Ingrese un correo electrónico válido.</span>');
  }
  error = true;
}

if (!/^\+56\d{9}$/.test(phone)) {
  if(!$('#phone').next().hasClass('error')) {
    $('#phone').after('<span class="error">El formato del número debe ser +56XXXXXXXXX.</span>');
  }
  error = true;
}

if (!/^[\w\d\p{P}]+$/.test(password)) {
  if(!$('#password').next().hasClass('error')) {
    $('#password').after('<span class="error">Solo se permiten letras, números y signos de puntuación.</span>');
  }
  error = true;
}

if (!/^.+$/.test(securityQuestion)) {
  if(!$('#security-question').next().hasClass('error')) {
    $('#security-question').after('<span class="error">Ingrese una pregunta de seguridad válida.</span>');
  }
  error = true;
}

if (!/^[a-zA-Z0-9]+$/.test(securityAnswer)) {
  if(!$('#security-answer').next().hasClass('error')) {
    $('#security-answer').after('<span class="error">Solo se permiten letras y números.</span>');
  }
  error = true;
}


      // Si hay algún error, no se envía el formulario y se muestra un mensaje
      if (error) {
        alert('Ha ocurrido un error al cambiar los ajuste de cuenta. Por favor, revise los campos.');
        return;
      }
  
      // Si todo está bien, se muestra un mensaje de éxito y se redirige a la siguiente página
      alert('¡Se han aplicado los cambios exitosamente!');
      window.location.href = '../El-Blogsillo/Usuario.html';
    });
  
    // Quitar mensaje de error al escribir en un campo
    $('input').keyup(function() {
      $(this).siblings('.error').remove();
    });
  });
  