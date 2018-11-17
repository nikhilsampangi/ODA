function onSuccess(googleUser) {
              console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
              let profile = googleUser.getBasicProfile();
                console.log(profile.getName())
                  document.getElementById("full_name").value=profile.getName();
                  document.getElementById("image").value=profile.getImageUrl();
                  document.getElementById("email").value=profile.getEmail();
                  document.myform.submit();
                  // setTimeout('', 500);
            }


function onFailure(error) {
              console.log(error);
            }
function renderButton() {
    gapi.signin2.render('my-signin2', {
        'scope': 'profile email',
        'width': 240,
        'height': 50,
        'longtitle': true,
        'theme': 'dark',
        'onsuccess': onSuccess,
        'onfailure': onFailure
    });
}

function signOut() {
      var auth2 = gapi.auth2.getAuthInstance();
      auth2.signOut().then(function () {
        console.log('User signed out.');
      });
    }
function onLoad() {
    gapi.load('auth2', function () {
        gapi.auth2.init();
    });
}



