function ToggleNav() {
    const navbar = document.getElementById("side-nav");

    if (navbar.style.width === "0%") {
        navbar.style.width = "100%";
    } else {
        navbar.style.width = "0%";
    }
}
