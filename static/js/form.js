function register_suc() {
    var customer_reg = document.getElementById("registerer1");
    var emails = document.getElementById("inputEmail");
    var pwd1 = document.getElementById("inputPassword");
    var pwd2 = document.getElementById("confirmPassword");

    if (customer_reg.checked == true) {
        if ((emails.value + 1) != 1) {
            window.location.reload();
            if ((pwd1.value + 1) != 1) {
                window.location.reload();
                if ((pwd2.value + 1) != 1) {
                    document.write('');
                    window.location.assign("/customer/");
                }
            }
        }
    }
}
