document.addEventListener('DOMContentLoaded', () => {
    // creating the observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            console.log(entry)
            if (entry.isIntersecting) {
                entry.target.classList.add('show')
            }
        })
    })

    const targetEls = document.querySelectorAll('.show-on-scroll')
    targetEls.forEach((el) => observer.observe(el))
})