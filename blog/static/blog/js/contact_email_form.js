document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('contact_email_form').onsubmit = function(e) {
        
        e.preventDefault()
        
        const data = new FormData(this)

        fetch(this.action, {
            method:'post',
            body: data,
        })
        .then(response => {
            if (!response.ok) {
                const err = response.json()
                throw new Error(err.error)
            }
        })
        .catch(err => console.log(err))     
    }
})