/* Project Detail Page slider */
// document.addEventListener("DOMContentLoaded", (event) => {
//     let next = document.querySelector(".next");
//     let prev = document.querySelector(".prev");
//     let slider = document.querySelector(".slider");
  
//     if (next && prev && slider) {
//       next.addEventListener("click", function () {
//         let slides = document.querySelectorAll(".slides");
//         if (slides.length > 0) {
//           slider.appendChild(slides[0]);
//         }
//       });
  
//       prev.addEventListener("click", function () {
//         let slides = document.querySelectorAll(".slides");
//         if (slides.length > 0) {
//           slider.prepend(slides[slides.length - 1]);
//         }
//       });
//     }
//   });


/* Project Detail Page slider 2 */
document.addEventListener('DOMContentLoaded', () => {
    let nextButton = document.getElementById('next');
    let prevButton = document.getElementById('prev');
    let carousel = document.querySelector('.carousel');
    let listHTML = document.querySelector('.carousel .list');
    let backButton = document.getElementById('back'); 

    nextButton.onclick = function(){
        showSlider('next');
    }
    prevButton.onclick = function(){
        showSlider('prev');
    }
    let unAcceppClick;
    const showSlider = (type) => {
        nextButton.style.pointerEvents = 'none';
        prevButton.style.pointerEvents = 'none';

        carousel.classList.remove('next', 'prev');
        let items = document.querySelectorAll('.carousel .list .item');
        if(type === 'next'){
            listHTML.appendChild(items[0]);
            carousel.classList.add('next');
        }else{
            listHTML.prepend(items[items.length - 1]);
            carousel.classList.add('prev');
        }
        clearTimeout(unAcceppClick);
        unAcceppClick = setTimeout(()=>{
            nextButton.style.pointerEvents = 'auto';
            prevButton.style.pointerEvents = 'auto';
        }, 1000)
    }

    backButton.onclick = () => {
        const url = backButton.getAttribute('data-url');
        if (url) {
            window.location.href = url;
        };
    };
});

