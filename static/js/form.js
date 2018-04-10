function register_suc() {
    var registerers = document.getElementById("register");
    var email = document.getElementById("inputEmail");
    var pwd1 = document.getElementById("inputPassword");
    var pwd2 = document.getElementById("confirmPassword");

    if (registerers[0].checked == true) {
        if (email == true && pwd1 ==true && true == pwd2) {
            window.location.assign("/customer/");
        }
    }
}
