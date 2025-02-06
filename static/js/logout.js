document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("confirmLogout").addEventListener("click", function () {
        fetch("/account/logout/", {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"), // CSRF token for security
                "Content-Type": "application/json",
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                window.location.href = "/";
            }
        })
        .catch(error => console.error("Error logging out:", error));
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
