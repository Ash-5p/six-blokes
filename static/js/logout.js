/* jshint esversion: 11 */

document.addEventListener("DOMContentLoaded", function () {
    const logoutButton = document.getElementById("confirmLogout");
    const logoutForm = document.getElementById("logoutForm");

    if (logoutButton && logoutForm) {
        logoutButton.addEventListener("click", function () {
            logoutForm.submit();
        });
    }
    window.addEventListener("pageshow", function (event) {
        if (event.persisted) {
            window.location.reload();
        }
    });
});