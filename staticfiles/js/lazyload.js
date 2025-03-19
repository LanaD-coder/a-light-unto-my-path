document.addEventListener("DOMContentLoaded", function () {
    const hero = document.querySelector(".hero");

    if (!hero) {
        console.error("Hero section not found!");
        return;
    }

    console.log("Hero section found:", hero);
    console.log("Data-bg attribute:", hero.getAttribute("data-bg"));

    if ("IntersectionObserver" in window) {
        let observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    let imgUrl = hero.getAttribute("data-bg");
                    console.log("Loading background image:", imgUrl);
                    hero.style.backgroundImage = `url('${imgUrl}')`;
                    hero.classList.add("loaded");
                    observer.unobserve(hero);
                }
            });
        });

        observer.observe(hero);
    } else {
        console.warn("IntersectionObserver not supported, loading image immediately.");
        let imgUrl = hero.getAttribute("data-bg");
        hero.style.backgroundImage = `url('${imgUrl}')`;
        hero.classList.add("loaded");
    }
});