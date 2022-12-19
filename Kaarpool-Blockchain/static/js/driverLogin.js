
function driverLoginFunction(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if(username =="" || password ==""){
        alert("please enter username or password");
    }
    else{
    console.log("username: - ",username," password: - ",password);
    let payload={
        'username':username,
        'password': password
    }
    console.log("payload: - ",payload);
    console.log("JSON.stringify(payload): - ",JSON.stringify(payload));
    var payloadString = JSON.stringify(payload);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
            if(this.responseText.status){
              
            }
        }
    };
    xhttp.open("POST", "/driverLogin", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(payloadString);
    console.log("Rider Register Event fired");
    }
}