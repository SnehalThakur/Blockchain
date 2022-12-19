function riderSignupFunction(){
    var name = document.getElementById("name").value;
    var contactNo = document.getElementById("contactNo").value;
    var password = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    var e = document.getElementById("gender");
    var value = e.value;
    var gender = e.options[e.selectedIndex].text;
    console.log("name: -",name)
    if(name == "" ||contactNo == "" || password == "" || value == 0 || email == ""){
        alert("please fill all fields");
    }
    else{
        let payload = {
           "name":name,
           "contactNo":contactNo,
           "password":password,
           "gender":gender,
           "email":email
        }
        console.log("payload: - ",payload);
        console.log("JSON.stringify(payload): - ",JSON.stringify(payload));
        var payloadString = JSON.stringify(payload);
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                console.log(this.responseText);
                console.log(this.responseText);
                let res = JSON.parse(this.responseText)
                console.log(typeof this.responseText);
                console.log(typeof res);
                if(res.status){
                  launch_toast("toast",res.message);
                  window.location.href = "/driverHomePage";
                }
                else{
                  launch_toast("toast1",res.message);

                }
            }
        };
        xhttp.open("POST", "/riderRegister", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(payloadString);
        console.log("Rider Register Event fired");
    }
}
function launch_toast(tosterName,msg) {
  var x = document.getElementById(tosterName);
  x.className = "show";
  document.getElementById("desc").innerHTML = msg;
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
}