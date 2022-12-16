function signupFunction(){
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
        const userAction = async () => {
            const response = await fetch('http://example.com/movies.json', {
              method: 'POST',
              body: payload, // string or object
              headers: {
                'Content-Type': 'application/json'
              }
            });
            const myJson = await response.json(); //extract JSON from the http response
            // do something with myJson
            if(myJson.status){
                window.location.href = "./page1.html";
              }
              else{
                  alert("Your password or username is wrong");
              }
          }
    }
}