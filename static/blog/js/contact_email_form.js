document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('contact_email_form').onsubmit = function(e) {
        e.preventDefault()
        
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
    }
})