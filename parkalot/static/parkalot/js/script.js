
// Mozilla get location

$(document).ready(function() { 
  // Don't submit form right away, get user location first and callback submit
  $('#startParkForm').submit( function(event) {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(function(position) {
        submitIfHaveCoordinates(position.coords.latitude, position.coords.longitude);
      });
    }
    else {
      return null
    }
    event.preventDefault();
  });

  setInterval(() => {
    getCurrentTime($("#current-time"))
  }, 1000)
});

function getCurrentTime(element) {
  let time = new Date()
  let timeValue = "";

  if (time.getHours() < 10)
      timeValue += "0"
  timeValue += time.getHours() + ":"
  if (time.getMinutes() < 10)
      timeValue += "0"
  timeValue += time.getMinutes() + ":"
  if (time.getSeconds() < 10)
      timeValue += "0"
  timeValue += time.getSeconds()

  element.text(timeValue)
}

// callback to submit form if we got the coordinates
function submitIfHaveCoordinates(lat,long) {
  if(lat != null && long != null) {
    $('input[name="coordinates"]').val(lat+":"+long);
    let formEl = $("#startParkForm")

    $.ajax({
      url:formEl.attr('action'),
      type: 'post',
      data: formEl.serialize(),
      succsess: () => {
          console.log("successfully sent data to server")
      }
  })

  //get current time and set the second clock for 3 hours later
    // document.getElementById("startParkForm").submit();
  }
}