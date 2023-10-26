function autoDelete(button) { //remove animation when click button
    button.parentElement.remove()
}

function Toast(message, error=false) {
    let basicClass = 'alert toast-message'
    let successClass = 'alert-primary '
    let errorClass = 'alert-danger'

    const toast = document.createElement('div')
    toast.className = `${basicClass} ${error ? errorClass : successClass}`
    toast.role = 'alert'
    toast.innerHTML =  `${message}
        <button onclick="autoDelete(this)" type="button" class="btn-close ms-3" data-bs-dismiss="alert" aria-label="Close"></button>`
    
    toast.onanimationend = () => toast.remove() // remove animation when ends
    return toast
}

