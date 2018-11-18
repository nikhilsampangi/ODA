document.getElementById('email_1').readOnly=true;

var myLink = document.getElementById('pat');

myLink.onclick = function(){

    var script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "https://apis.google.com/js/platform.js?onload=renderButton";
    document.getElementsByTagName("head")[0].appendChild(script);
    return false;

}