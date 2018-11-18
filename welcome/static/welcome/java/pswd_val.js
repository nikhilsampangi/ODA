function checkForm(form)
  {
      if (form.password.value != form.con_password.value) {
          alert("Error: password didn't match!");
          form.password.focus();
          return false;
      }

      else if(form.password.value != "" && form.password.value == form.con_password.value) {
        if(form.password.value.length < 6) {
        alert("Error: Password must contain at least six characters!");
        form.password.focus();
        return false;
        }

        re = /[0-9]/;
      if(!re.test(form.password.value)) {
        alert("Error: password must contain at least one number (0-9)!");
        form.password.focus();
        return false;
      }
      re = /[a-z]/;
      if(!re.test(form.password.value)) {
        alert("Error: password must contain at least one lowercase letter (a-z)!");
        form.password.focus();
        return false;
      }

    } else {
      alert("Error: Please check that you've entered and confirmed your password!");
      form.password.focus();
      return false;
    }

    alert("You entered a valid password: " + form.password.value);
    return true;
  }
document.getElementsByName(email).readonly=true;