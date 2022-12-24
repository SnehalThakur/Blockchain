var userData;
function init() {
    // initialisation stuff here
    userData= JSON.parse(sessionStorage.getItem("userData"));
    console.log("userData: - ",userData);
    document.getElementById("userNameDiv").innerHTML = "Hi "+userData.name;

  }
  
init();
$( function() {
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
    var availableTags = [
          'Bajrang nagar, Manewada road, Nagpur',
          'Omkar nagar, Manewada road, Nagpur',
          'Rameshwari, Nagpur',
          'Chhatrapati Sqr, Nagapur',
           'Jaitala, Nagapur',
           'Trimurti nagar, Nagapur',
          'T-point, Nagpur',
          'Hingna road, Nagpur',
          'Mahindra sqr, Nagpur',
           'IC sqr, Nagpur',
           'YCC colleage, Hingna, Nagpur',
          'Bajaj nagar, Nagpur',
        ]
    $( "#tags" ).autocomplete({
      source: availableTags,
      select: function (event, ui) {
        // $("#tags_code").val(ui.item.locationCode);  
        console.log("ui.item.locationCode: - ",ui.item.locationCode)
        }
    });
    $( "#tags1" ).autocomplete({
      source: availableTags,
      select: function (event, ui) {
        // $("#tags_code").val(ui.item.locationCode);  
        console.log("ui.item.locationCode: - ",ui.item.locationCode)
        }
    });
  } );
  function confirmFunction(){
    var time = document.getElementById("appt").value;
    var sourceLoacation = document.getElementById("selUserSource").value;
    var destinationLoacation = document.getElementById("selUser").value;
    var value = document.getElementById("vehicle").value;
    
    console.log("value: -",value);
    console.log("time: -",time);
    console.log("sourceLoacation: -",sourceLoacation);
    console.log("destinationLoacation: -",destinationLoacation);
  }
  $(document).ready(function(){
 
    // Initialize select2
    $("#selUser").select2();
    $("#selUserSource").select2();

    // Read selected option
    $('#but_read').click(function(){
        var username = $('#selUser option:selected').text();
        var userid = $('#selUser').val();

        $('#result').html("id : " + userid + ", name : " + username);

    });
});