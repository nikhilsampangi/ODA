$(function () {
        $("#submit_log").click(function () {
            var password = $("#pass").val();
            var err_val=0;
            if (password == "") {

                $('#pass1_err').html('Invalid password').show().fadeOut(2000);
                return false;
            }

            return true;
        });
    });


$(function () {
        $("#submit_reg").click(function () {
            var fname=$("#fname").val();
            var password = $("#pass2").val();
            var confirmPassword = $("#pass3").val();
            var phone_num=$("#phn").val();
            var pass_error;
            var err_val=0;

            jQuery('#phn').keyup(function () {
                this.value = this.value.replace(/[^0-9\.]/g,'');
            });


            if (password == password.match(/^-?\d*$/)) {

                pass_error = $('#pass_err').html('Passwords should contain atleast one alphabet');
                err_val=1;
            }

            if (password != confirmPassword) {

                pass_error = $('#pass_err').html('Passwords do not match.');
                err_val=1;
            }

            if(password.length <= 8){

                pass_error = $('#pass_err').html('Passwords should contain atleast 8 chracters.');
                err_val=1;
            }

            // -------------PHONE_NUMBER_VALIDATION-----------------


            if (phone_num.length < 10) {

                $('#phn_err1').html('Phone Number invalid Structure').show().fadeOut(3000);
                err_val=1;
            }

            // -------------Checking for ERRORS-----------------

            if (err_val == 1) {
                err_val = 0;
                return false;
            }


            return true;
        });
    });

$(document).ready(function () {

  $("#phn").keypress(function (num) {

     if (num.which != 8 && num.which != 0 && (num.which < 48 || num.which > 57)) {

        $("#phn_err2").html("Invalid Number").show().fadeOut(3000);
               return false;
    }

   });
});
