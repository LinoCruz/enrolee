//=======ALERTS========
var formLogin = document.getElementById("formLogin");
formLogin.onsubmit = function (e) {
  // e is the variable that we are listening
  e.preventDefault();
  // get the information from the form
  var data = new FormData(formLogin);
  fetch("http://127.0.0.1:5000/login", { method: "POST", body: data })
    .then((response) => response.json())
    .then((data) => {
      if (data.message == "Welcomeback") {
        window.location.href = "/dashboard";
      } else {
        console.log(data);
        var alertMessage = document.getElementsByClassName("alertMessage");
        alertMessage.innerhtml = data.message;
      }
    });
};
