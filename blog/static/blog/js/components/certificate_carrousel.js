document.addEventListener('DOMContentLoaded', () => {
    const progressCircle = document.querySelector(".autoplay-progress svg");
    const progressContent = document.querySelector(".autoplay-progress span");

    // var swiper = new Swiper(".mySwiper", {
    //   spaceBetween: 30,
    //   centeredSlides: true,
    //   autoplay: {
    //     delay: 99000,
    //     disableOnInteraction: false
    //   },
    //   pagination: {
    //     el: ".swiper-pagination",
    //     clickable: true
    //   },
    //   navigation: {
    //     nextEl: ".swiper-button-next",
    //     prevEl: ".swiper-button-prev"
    //   },
    //   on: {
    //     autoplayTimeLeft(s, time, progress) {
    //       progressCircle.style.setProperty("--progress", 1 - progress);
    //       progressContent.textContent = `${Math.ceil(time / 1000)}s`;
    //     }
    //   }
    // });


    const swiper = new Swiper('.swiper', {


      // Default parameters
      speed: 800,
      slidesPerView: 1,
      spaceBetween: 10,
      
      // Responsive breakpoints
      breakpoints: {
          // when window width is >= 600px
          785: {
          slidesPerView: 2,
          spaceBetween: 40
          },
          // when window width is >= 1040px
        
        
      },
         
      
      // Optional parameters
      direction: 'horizontal',
      loop: true,
      autoplay: {
          delay: 6000,
          disableOnInteraction: false,
      },



      // If we need pagination
      pagination: {
          el: '.swiper-pagination',
          type: 'bullets',
          clickable: true,
      },
      grabCursor:true,
      // Navigation arrows
      navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
      },


  });




})