
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
});

// callback to submit form if we got the coordinates
function submitIfHaveCoordinates(lat,long) {
  if(lat != null && long != null) {
    $('input[name="coordinates"]').val(lat+":"+long);
    document.getElementById("startParkForm").submit();
  }
}