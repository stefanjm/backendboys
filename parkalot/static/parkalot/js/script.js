
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
    getCurrentTime($("#current-time>span"))
  }, 1000)
});

// This function just gets the current time, formats it and puts the formatted text into element
function getCurrentTime(element) {
  if (element.attr("class") == "not-used")
    element.removeClass("not-used")
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

    // Make an ajax requests, so that we keep the same page and show the digital clock
    $.ajax({
      url:formEl.attr('action'),
      type: 'post',
      dataType: "json",
      data: formEl.serialize(), 
      success: function(databack) {
          // if successful, display the address
          $("#customer-parking-address").append("<P>"+databack.address);
      }
  })

  // This puts the timer on, showing the customer when his free time on this parking zone is over
  calculateParkEndTime($("#park-end-time>span"))

  //get current time and set the second clock for 3 hours later
  // document.getElementById("startParkForm").submit();
  }
}

function calculateParkEndTime(element) {
  if (element.attr("class") == "not-used")
    element.removeClass("not-used")
  let time = new Date()
  let parkEndTime = ""

  if (time.getHours() + 3 < 10)
    parkEndTime += "0"
  parkEndTime += (time.getHours() + 3) + ":"
  if (time.getMinutes() + 1 < 10)
    parkEndTime += "0"
  parkEndTime += (time.getMinutes() + 1)

  element.text(parkEndTime)
}