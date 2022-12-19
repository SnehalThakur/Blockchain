function driverSignupFunction(){
    var name = document.getElementById("name").value;
    var contactNo = document.getElementById("contactNo").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var licenseNumber = document.getElementById("licenseNumber").value;
    var licenseValidity = document.getElementById("licenseValidity").value;
    var e = document.getElementById("gender");
    var value = e.value;
    var v = document.getElementById("vehicle");
    var vehicleValue = v.value;
    var gender = e.options[e.selectedIndex].text;
    var vehicle = v.options[e.selectedIndex].text;
    console.log("name: -",name)
    if(name == "" ||contactNo == "" || password == "" || value == 0 || email =="" || vehicleValue == 0 || licenseNumber=="" || licenseValidity==""){
        alert("please fill all fields")
    }
    else{
        let payload = {
           "name":name,
           "contactNo":contactNo,
           "password":password,
           "gender":gender,
           "vehicle":vehicle,
           "email": email,
           "licenseNumber": licenseNumber,
           "licenseValidity": licenseValidity
        }
        console.log("payload: - ",payload);
        console.log("JSON.stringify(payload): - ",JSON.stringify(payload));
        var payloadString = JSON.stringify(payload);
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                alert(this.responseText);
            }
        };
        xhttp.open("POST", "/driverRegister", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(payloadString);
        console.log("Driver Register Event fired");
    }
}