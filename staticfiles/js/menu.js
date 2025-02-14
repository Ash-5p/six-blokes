const menuDropdown = document.getElementsByClassName('menu-collapse');

for (let button of menuDropdown) {
    if (button.children.length >= 2) {
      if(button.children[1].children.length >= 1){
        let menuCaret = button.children[1].children[0];
        
        if (menuCaret) {
            menuCaret.addEventListener("click", (e) => {
                if (menuCaret.classList.contains("fa-caret-down")) {
                    menuCaret.classList.remove("fa-caret-down");
                    menuCaret.classList.add("fa-caret-up");
                } else {
                    menuCaret.classList.remove("fa-caret-up");
                    menuCaret.classList.add("fa-caret-down");
                }
            });
        }
      } else {
          console.warn('menu-collapse element does not have expected structure (second child doesn\'t have children):', button);
      }
    } else {
        console.warn('menu-collapse element does not have expected structure (less than 2 children):', button);
    }
}