document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".like-button").forEach(button => {
        button.addEventListener("click", function () {
            let postId = this.getAttribute("data-post-id");
            let csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

            fetch(`/like/${postId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken,
                    "Content-Type": "application/json"
                },
                credentials: "same-origin"
            })
            .then(response => response.json())
            .then(data => {
                document.querySelector(`#like-count-${postId}`).textContent = data.total_likes;
                this.textContent = data.liked ? "Unlike" : "Like";
            })
            .catch(error => console.error("Error:", error));
        });
    });
});