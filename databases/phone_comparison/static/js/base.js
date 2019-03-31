const form_phone = document.getElementsByClassName('form_phone');

function spam() {
    alert('11111111111');
}

for (const phone of form_phone) {
    phone.addEventListener('onchange', spam);
}
