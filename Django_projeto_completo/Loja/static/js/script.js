


function toggleTheme() {

    const html = document.documentElement;

    const icon = document.getElementById("themeIcon");

    const temaAtual = html.getAttribute("data-bs-theme");


    if (temaAtual === "dark") {


        html.setAttribute("data-bs-theme", "light");

        icon.classList.remove("fa-moon");

        icon.classList.add("fa-sun");

        localStorage.setItem("theme", "light");

    } else {


        html.setAttribute("data-bs-theme", "dark");

        icon.classList.remove("fa-sun");

        icon.classList.add("fa-moon");

        localStorage.setItem("theme", "dark");

    }

}




document.addEventListener("DOMContentLoaded", function () {

    const html = document.documentElement;

    const icon = document.getElementById("themeIcon");

    const temaSalvo = localStorage.getItem("theme");


    if (temaSalvo) {

        html.setAttribute(
            "data-bs-theme",
            temaSalvo
        );


        if (temaSalvo === "dark") {

            icon.classList.remove("fa-sun");

            icon.classList.add("fa-moon");

        } else {

            icon.classList.remove("fa-moon");

            icon.classList.add("fa-sun");

        }

    }

});

