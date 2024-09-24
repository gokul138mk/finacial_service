document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordField = document.querySelector('#show_hide_password input');
    const icon = this.querySelector('i');
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    icon.classList.toggle('fa-eye');
    icon.classList.toggle('fa-eye-slash');
});