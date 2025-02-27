/* jshint esversion: 11 */

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".menu-collapse").forEach(button => {
        let menuCaret = button.querySelector("i.fa-solid");

        if (!menuCaret) {
            console.warn("Caret icon not found inside:", button);
            return;
        }

        // Bootstrap collapse event listener
        let targetID = button.getAttribute("data-bs-target");
        let collapseElement = document.querySelector(targetID);

        if (collapseElement) {
            collapseElement.addEventListener("show.bs.collapse", function () {
                menuCaret.classList.remove("fa-caret-down");
                menuCaret.classList.add("fa-caret-up");
            });

            collapseElement.addEventListener("hide.bs.collapse", function () {
                menuCaret.classList.remove("fa-caret-up");
                menuCaret.classList.add("fa-caret-down");
            });
        } else {
            console.warn("Collapse target not found for:", button);
        }
    });
});

