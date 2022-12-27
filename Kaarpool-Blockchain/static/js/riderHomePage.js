var userData;
function init() {
    // initialisation stuff here
    userData= JSON.parse(sessionStorage.getItem("userData"));
    console.log("userData: - ",userData);
    document.getElementById("userNameDiv").innerHTML = "Hi "+userData.name;

  }
  
init();
$( function() {
  $("#selUser").select2();
  $("#selUserSource").select2();
  $('.openmodale').click(function (e) {
    e.preventDefault();
    $('.modale').addClass('opened');
});
$('.closemodale').click(function (e) {
    e.preventDefault();
    $('.modale').removeClass('opened');
});


} );
var responseSearchData ;
function searchFunction(){
  // let 
  console.log("search");
  var time = document.getElementById("appt").value;
  var sourceLoacation = document.getElementById("selUserSource").value;
  var destinationLoacation = document.getElementById("selUser").value;
  if (time == "" || sourceLoacation == 0 || destinationLoacation == 0) {
    alert("please fill all fields");
  }
  else {
    let payload = {
      'name': userData.name,
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
          // launch_toast("toast", res.message);
          // sessionStorage.setItem("userData", this.responseText);
          // window.location.href = "/driverHomePage";
          document.getElementById("tableDiv").style.display = "block";
          let tdData ='';
          responseSearchData = res.data;
      if(res.data?.length == 0){
        document.getElementById('td1').innerHTML = '<tr style="text-align:center">No Data avaliable</tr>';
      }
      else{
        res.data.forEach((element,inx) => {
          // let timeData = element.starttime.split("_");
          tdData +=  '<tr class="openmodale" onClick="clickTableRow('+inx+')" ><td class="openmodale">'+element.name+'</td><td class="openmodale">'+element.source+'</td><td class="openmodale">'+element.destination+'</td><td class="openmodale">'+element.starttime+'</td></tr>';
        });
        document.getElementById('td1').innerHTML = tdData
      }
          // init();

        }
        else {
          launch_toast("toast1", res.message);

        }
      }
    };
    xhttp.open("POST", "/getDriverRouteDataWithSrcAndDes", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(payloadString);
    console.log("Rider Register Event fired");
}
}
function launch_toast(tosterName, msg) {
  var x = document.getElementById(tosterName);
  x.className = "show";
  document.getElementById("desc").innerHTML = msg;
  setTimeout(function () { x.className = x.className.replace("show", ""); }, 5000);
}
var selectedData;
function clickTableRow(rowData){
  console.log("rowData: - ",rowData);
  console.log('responseSearchData: - ',responseSearchData[rowData]);
  selectedData = responseSearchData[rowData]
  $('.modale').addClass('opened');
}
function cancelFunction(){
  // $('.modale').addClass('opened');
  $('.modale').removeClass('opened');
}
function successFunction(){
  console.log("selectedData: - ",selectedData);
  console.log("userData.name: - ",userData.name);
  let payload = {
    'driveName': selectedData.name,
    'source':selectedData.source,
    'destination': selectedData.destination,
    'riderName': userData.name,
    'time': selectedData.starttime
  }
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
          // launch_toast("toast", res.message);
          // sessionStorage.setItem("userData", this.responseText);
          // window.location.href = "/driverHomePage";
          console.log("In side sucess");
          launch_toast("toast", "Ride booked successfully.");
          // init();
          $('.modale').removeClass('opened');

        }
        else {
          launch_toast("toast1", "Error on ride booking.");

        }
      }
      // else{
      //   launch_toast("toast1", "Error on ride booking.");
      // }
    };
    xhttp.open("POST", "/updateDriveRouteDataWithRiderName", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(payloadString);
    console.log("Rider Register Event fired");
}
