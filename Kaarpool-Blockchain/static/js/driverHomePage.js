var userData;
function init() {
  // initialisation stuff here
  userData = JSON.parse(sessionStorage.getItem("userData"));
  console.log("userData: - ", userData);
  document.getElementById("userNameDiv").innerHTML = "Hi " + userData.name;
  let payload = {
    'name': userData.name,
  }
  console.log("payload: - ", payload);
  console.log("JSON.stringify(payload): - ", JSON.stringify(payload));
  var payloadString = JSON.stringify(payload);
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText);
      let res = JSON.parse(this.responseText)
      console.log(typeof this.responseText);
      console.log(res.data);
      let tdData =''
      if(res.data?.length == 0){
        document.getElementById('td1').innerHTML = '<tr>No Data avaliable</tr>';
      }
      else{
        res.data.forEach(element => {
          let timeData = element.starttime.split("_");
          tdData +=  '<tr><td>'+element.source+'</td><td>'+element.destination+'</td><td>'+timeData[0]+'</td><td>'+timeData[1]
          +'</td><td>'+element.rider1+'</td></tr>';
          // '</td><td>'+element.rider2+'</td><td>'+element.rider3+
        });

        document.getElementById('td1').innerHTML = tdData
      }
     
    }
    else{
      document.getElementById('td1').innerHTML = '<tr>No Data avaliable</tr>';

    }
  };
  xhttp.open("POST", "/getDriverRouteData", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(payloadString);
  
}

init();
$(function () {
  // var availableTags = [
  //   {'locationTitle': 'Bajrang nagar, Manewada road, Nagpur','locationCode':'001'},
  //   {'locationTitle': 'Omkar nagar, Manewada road, Nagpur','locationCode':'002'},
  //   {'locationTitle': 'Rameshwari, Nagpur','locationCode':'003'},
  //   {'locationTitle': 'Chhatrapati Sqr, Nagapur','locationCode':'004'},
  //   {'locationTitle': 'Jaitala, Nagapur','locationCode':'005'},
  //   {'locationTitle': 'Trimurti nagar, Nagapur','locationCode':'006'},
  //   {'locationTitle': 'T-point, Nagpur','locationCode':'007'},
  //   {'locationTitle': 'Hingna road, Nagpur','locationCode':'008'},
  //   {'locationTitle': 'Mahindra sqr, Nagpur','locationCode':'009'},
  //   {'locationTitle': 'IC sqr, Nagpur','locationCode':'010'},
  //   {'locationTitle': 'YCC colleage, Hingna, Nagpur','locationCode':'011'},
  //   {'locationTitle': 'Bajaj nagar, Nagpur','locationCode':'012'},
  // ];
  // var availableTags = [
  //   'Bajrang nagar, Manewada road, Nagpur',
  //   'Omkar nagar, Manewada road, Nagpur',
  //   'Rameshwari, Nagpur',
  //   'Chhatrapati Sqr, Nagapur',
  //   'Jaitala, Nagapur',
  //   'Trimurti nagar, Nagapur',
  //   'T-point, Nagpur',
  //   'Hingna road, Nagpur',
  //   'Mahindra sqr, Nagpur',
  //   'IC sqr, Nagpur',
  //   'YCC colleage, Hingna, Nagpur',
  //   'Bajaj nagar, Nagpur',
  // ]
  // $("#tags").autocomplete({
  //   source: availableTags,
  //   select: function (event, ui) {
  //     // $("#tags_code").val(ui.item.locationCode);  
  //     console.log("ui.item.locationCode: - ", ui.item.locationCode)
  //   }
  // });
  // $("#tags1").autocomplete({
  //   source: availableTags,
  //   select: function (event, ui) {
  //     // $("#tags_code").val(ui.item.locationCode);  
  //     console.log("ui.item.locationCode: - ", ui.item.locationCode)
  //   }
  // });
});
function confirmFunction() {
  var time = document.getElementById("appt").value;
  var sourceLoacation = document.getElementById("selUserSource").value;
  var destinationLoacation = document.getElementById("selUser").value;
  var vehicleSites = document.getElementById("vehicle").value;

  if (vehicleSites == 0 || time == "" || sourceLoacation == 0 || destinationLoacation == 0) {
    alert("please fill all fields");
  }
  else {
    let payload = {
      'name': userData.name,
      'availableSeats': vehicleSites,
      'starttime': time,
      'source': sourceLoacation,
      'destination': destinationLoacation
    }
    console.log("payload: - ", payload);
    console.log("JSON.stringify(payload): - ", JSON.stringify(payload));
    var payloadString = JSON.stringify(payload);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText);
        let res = JSON.parse(this.responseText)
        console.log(typeof this.responseText);
        console.log(typeof res);
        if (res.status) {
          launch_toast("toast", res.message);
          // sessionStorage.setItem("userData", this.responseText);
          // window.location.href = "/driverHomePage";
          init();
        }
        else {
          launch_toast("toast1", res.message);

        }
      }
    };
    xhttp.open("POST", "/driverRoute", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(payloadString);
    console.log("Rider Register Event fired");
  }
  // console.log("value: -",value);
  // console.log("time: -",time);
  // console.log("sourceLoacation: -",sourceLoacation);
  // console.log("destinationLoacation: -",destinationLoacation);

}
function launch_toast(tosterName, msg) {
  var x = document.getElementById(tosterName);
  x.className = "show";
  document.getElementById("desc").innerHTML = msg;
  setTimeout(function () { x.className = x.className.replace("show", ""); }, 5000);
}
$(document).ready(function () {

  // Initialize select2
  $("#selUser").select2();
  $("#selUserSource").select2();

  // Read selected option
  $('#but_read').click(function () {
    var username = $('#selUser option:selected').text();
    var userid = $('#selUser').val();

    $('#result').html("id : " + userid + ", name : " + username);

  });
});