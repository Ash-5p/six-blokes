document.addEventListener("DOMContentLoaded", function () {
    const logoutButton = document.getElementById("confirmLogout");
    const logoutForm = document.getElementById("logoutForm");

    if (logoutButton && logoutForm) {
        logoutButton.addEventListener("click", function () {
            logoutForm.submit();
        });
    }
});