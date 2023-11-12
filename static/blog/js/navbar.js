document.addEventListener('DOMContentLoaded', () => {
    const mobileMenu = document.getElementById('mobile-menu') // mobile wrapper menu
    const barsContainer = document.getElementById('bars') // bars svg
    const xContainer = document.getElementById('x') // x svg

    // close the mobile wrapper menu and shows the bars icon
    function closeNavbar () {
        mobileMenu.classList.remove('active');
        xContainer.style.display = 'none'
        barsContainer.style.display = 'inline-block'
    }
    
    // open the mobile wrapper menu and shows the x icon
    function openNavbar () {
        mobileMenu.classList.add('active');
        barsContainer.style.display = 'none';
        xContainer.style.display = "inline-block"; 
    }
    
    // toggle between open and close functions
    function handleNavbarOpen() {
        if (mobileMenu.classList.contains('active')) {
            closeNavbar()
        } else {
            openNavbar()
        }
    }

    // when press any nav-item  
    const navItems = document.querySelectorAll('.nav-item')
    navItems.forEach(link => link.onclick = function() {
        // the mobile wrapper menu close
        closeNavbar() 

        // removes the active class from all items
        navItems.forEach(item => item.classList.remove('active')) 
        
        // add active class to the clicked item
        link.classList.add('active')
    })

    // add toggle function to navbar-btn
    document.getElementById('navbar-btn').onclick = () => handleNavbarOpen()
    
    // when resize the screen close the navbar
    window.addEventListener('resize', closeNavbar)
})


