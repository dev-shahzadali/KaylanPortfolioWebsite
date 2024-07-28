/* Project Card */
document.addEventListener("DOMContentLoaded", function () {
  const cardWraps = document.querySelectorAll(".card-wrap");

  cardWraps.forEach((cardWrap) => {
    const card = cardWrap.querySelector(".card");
    const cardBg = cardWrap.querySelector(".card-bg");
    const cardInfo = cardWrap.querySelector(".card-info");

    let width = cardWrap.offsetWidth;
    let height = cardWrap.offsetHeight;
    let mouseX = 0;
    let mouseY = 0;
    let mouseLeaveDelay;

    cardWrap.addEventListener("mousemove", (e) => {
      mouseX = e.pageX - cardWrap.offsetLeft - width / 2;
      mouseY = e.pageY - cardWrap.offsetTop - height / 2;
      updateStyles();
    });

    cardWrap.addEventListener("mouseenter", () => {
      clearTimeout(mouseLeaveDelay);
    });

    cardWrap.addEventListener("mouseleave", () => {
      mouseLeaveDelay = setTimeout(() => {
        mouseX = 0;
        mouseY = 0;
        updateStyles();
      }, 1000);
    });

    function updateStyles() {
      const mousePX = mouseX / width;
      const mousePY = mouseY / height;
      const rX = mousePX * 30;
      const rY = mousePY * -30;
      const tX = mousePX * -40;
      const tY = mousePY * -40;

      card.style.transform = `rotateY(${rX}deg) rotateX(${rY}deg)`;
      cardBg.style.transform = `translateX(${tX}px) translateY(${tY}px)`;
    }
  });
});

/* Details Page URL */
document.addEventListener("DOMContentLoaded", () => {
  const cardContainer = document.getElementById("card-container");

  cardContainer.addEventListener("click", (event) => {
    const card = event.target.closest(".card-wrap");
    if (card) {
      const url = card.getAttribute("data-url");
      if (url) {
        window.location.href = url;
      }
    }
  });
});
