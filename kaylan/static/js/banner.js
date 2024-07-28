/* Banner */
window.addEventListener("load", () => {
  // Check if the current path is the homepage (assuming the homepage path is '/')
  if (window.location.pathname === "/") {
    const nameElement = document.getElementById("name");
    setTimeout(() => {
      nameElement.style.opacity = 1;
    }, 100);
  }
});

/* rotating words in banner */
document.addEventListener("DOMContentLoaded", function () {
  const words = ["Graphic", "UI/UX", "Web", "App"];
  let currentIndex = 0;
  const rotatingElement = document.getElementById("rotating-words");

  setInterval(() => {
    currentIndex = (currentIndex + 1) % words.length;
    rotatingElement.textContent = words[currentIndex];
  }, 1500); // Change every 2 seconds
});
