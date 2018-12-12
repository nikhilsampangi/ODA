$(function () {
        $("#submit_user_reg").click(function () {
            var phone_num=$("#phn").val();
            var emerg_phone_num=$("#em_phn").val();
            var age = $("#age").val();
            var pass_error;
            var err_val=0;



            // -------------PHONE_NUMBER_VALIDATION-----------------


            if (phone_num.length != 10) {

                $('#phn_err').html('Phone Number invalid Structure').show().fadeOut(3000);
                err_val=1;
            }

            if (emerg_phone_num.length != 10) {

                $('#emg_phn_err').html('Phone Number invalid Structure').show().fadeOut(3000);
                err_val=1;
            }

            if (age == "") {

                $('#age_err').html('Age Invalid').show().fadeOut(3000);
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

        $("#phn_err").html("Invalid Number").show().fadeOut(3000);
               return false;
    }

   });

   $("#em_phn").keypress(function (num) {

      if (num.which != 8 && num.which != 0 && (num.which < 48 || num.which > 57)) {

         $("#emg_phn_err").html("Invalid Number").show().fadeOut(3000);
                return false;
     }

    });

  $("#age").keypress(function (num) {

     if (num.which != 8 && num.which != 0 && (num.which < 48 || num.which > 57)) {

        $("#age_err").html("Age Invalid").show().fadeOut(3000);
               return false;
    }

   });

});
