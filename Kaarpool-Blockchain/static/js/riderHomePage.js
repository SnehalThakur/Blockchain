var userData;
function init() {
    // initialisation stuff here
    userData= JSON.parse(sessionStorage.getItem("userData"));
    console.log("userData: - ",userData);
    document.getElementById("userNameDiv").innerHTML = "Hi "+userData.name;

  }
  
init();