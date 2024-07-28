/* NavBar */
let menu = document.querySelector("#menu-icon");
let navlist = document.querySelector(".navlist");

menu.onclick = () => {
  menu.classList.toggle("bx-x");
  navlist.classList.toggle("open");
};

window.onscroll = () => {
  menu.classList.remove("bx-x");
  navlist.classList.remove("open");
};

// Contact Page message 

document.addEventListener('DOMContentLoaded', function () {
  var popup = document.getElementById('popup-message');
  if (popup) {
      popup.style.display = 'block';
      setTimeout(function () {
          popup.style.display = 'none';
      }, 2000);  // Adjust the timeout duration as needed
  }
});