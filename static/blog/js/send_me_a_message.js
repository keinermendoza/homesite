document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('send_me_a_message_btn').onclick = function() {
        const seccionDestino = document.getElementById('contact');
        let posicion = seccionDestino.offsetTop;
    
        document.body.scrollTop = posicion;
        document.getElementById('request_name').focus();
    }
})
