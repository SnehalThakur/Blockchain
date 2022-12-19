function riderLoginFunction(){
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
    xhttp.open("POST", "/riderLogin", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(payloadString);
    console.log("Rider Login Event fired");
    }
}
function launch_toast(tosterName,msg) {
    var x = document.getElementById(tosterName);
    x.className = "show";
    document.getElementById("desc").innerHTML = msg;
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 5000);
  }