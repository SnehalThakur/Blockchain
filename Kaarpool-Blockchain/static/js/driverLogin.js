
function loginFunction(){
    var uername = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if(username =="" || password ==""){
        alert("please enter username or password");
    }
    else{
    console.log("username: - ",uername," password: - ",password);
    let payload={
        'username':username,
        'password': password
    }
    const userAction = async () => {
        const response = await fetch('http://example.com/movies.json', {
          method: 'POST',
          body: payload
          , // string or object
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