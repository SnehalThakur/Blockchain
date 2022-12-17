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
    var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                alert(this.responseText);
            }
        };
        xhttp.open("POST", "/riderLogin", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(payload);
    }
}