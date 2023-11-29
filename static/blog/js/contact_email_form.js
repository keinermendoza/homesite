document.addEventListener('DOMContentLoaded', () => {
    // wait animation    
    const elemsToAnimate = Array.from(document.getElementsByClassName("email-animation-switch"))

    // form
    document.getElementById('contact_email_form').onsubmit = function(e) {
        e.preventDefault()

        // activate animations
        elemsToAnimate.forEach(animate => { animate.classList.add("active")})
        
        const data = new FormData(this)
        fetch(this.action, {
            method:'post',
            body: data,
        })
        .then(async (response) => {
             

            if (!response.ok) { 
                const data = await response.json() 
                throw new Error(data.error) // trowing a new error with the json message
            } else {
                const data = await response.json()
                document.body.appendChild(Toast(data.message)) // appending toast succefully message
                this.reset() // cleaning the fields
            }
        })
        .catch(err => document.body.appendChild(Toast(err.message, true))) // appending toast error message
        .finally(() => {
            // desactivate animation
            elemsToAnimate.forEach(desanimate => { desanimate.classList.remove("active")})
        })
    }
})