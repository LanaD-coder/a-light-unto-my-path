document.addEventListener("DOMContentLoaded", function () {
    const heroes = document.querySelectorAll("[data-bg]");  // Select all elements with a data-bg attribute

    if (heroes.length === 0) {
        console.error("No hero sections found!");
        return;
    }

    heroes.forEach(hero => {
        let imgUrl = hero.getAttribute("data-bg");

        if (!imgUrl) {
            console.error("No data-bg attribute found for hero section!");
            return;
        }

        const loadImage = () => {
            console.log("Loading background image:", imgUrl);
            hero.style.backgroundImage = `url('${imgUrl}')`;
            hero.classList.add("loaded");
        };

        if ("IntersectionObserver" in window) {
            let observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        loadImage();
                        observer.unobserve(hero);
                    }
                });
            });

            observer.observe(hero);
        } else {
            console.warn("IntersectionObserver not supported, loading image immediately.");
            loadImage();
        }
    });
});