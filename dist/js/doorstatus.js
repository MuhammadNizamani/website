var openString = "<h2> Døra er åpen. Velkommen inn! :) </h2>"
var closedString = "<h2> Døra er desverre lukket. Sjekk igjen senere </h2>"

var jqxhr = $.getJSON("api/door", function() {
  console.log("door fetch success");
})
  .done(function() {
    console.log("door fetch second success");
  })
  .fail(function() {
    console.log("door fetch error");
  })
  .always(function() {
    console.log("door fetch complete");
  });


jqxhr.complete(function() {
  console.log( "door fetch second complete" );
  var doorstatusDiv = document.getElementById('door-status');
  if(jqxhr.responseJSON[0].isOpen){
    doorstatusDiv.innerHTML = openString;
  }
  else{
    doorstatusDiv.innerHTML = closedString;
  }

});
