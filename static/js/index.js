var login_button = document.getElementById("login_button");
if (login_button) {
    login_button.addEventListener("click", function () {
        window.location.href = "/login/"
    });
}


var register_button = document.getElementById("register_button");
if (register_button) {
    register_button.addEventListener("click", function () {
        window.location.href = "/register/"
    });
}
