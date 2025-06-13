document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".like-button").forEach(button => {
        button.addEventListener("click", function () {
            let postId = this.getAttribute("data-post-id");
            let icon = this.querySelector("i");
            let likeCount = document.querySelector(`#like-count-${postId}`);
            let csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

            fetch(`/blog/like/${postId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken,
                    "Content-Type": "application/json"
                },
                credentials: "same-origin"
            })
            .then(response => response.json())
            .then(data => {
                if (data.liked) {
                    icon.classList.replace("fa-regular", "fa-solid");
                } else {
                    icon.classList.replace("fa-solid", "fa-regular");
                }
                likeCount.textContent = data.total_likes;
            })
            .catch(error => console.error("Error:", error));
        });
    });
});