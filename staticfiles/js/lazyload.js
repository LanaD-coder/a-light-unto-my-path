document.addEventListener("DOMContentLoaded", function () {
    const hero = document.querySelector(".hero");

    if (!hero) {
        console.error("Hero section not found!");
        return;
    }

    let imgUrl = hero.getAttribute("data-bg");

    if (!imgUrl) {
        console.error("No data-bg attribute found!");
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