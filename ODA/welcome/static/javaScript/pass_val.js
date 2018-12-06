$(function () {
        $("#submit").click(function () {
            var fname=$("#fname").val();
            var password = $("#pass2").val();
            var confirmPassword = $("#pass3").val();
            if (password != confirmPassword) {
                alert("Passwords do not match.");
                return false;
            }
            return true;
        });
    });