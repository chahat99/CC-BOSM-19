var xhttp1 = new XMLHttpRequest();
xhttp1.open("GET", "/treasure/get_pin/", true);
xhttp1.setRequestHeader("Content-Type", "application/json");
xhttp1.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    
    var json = JSON.parse(this.responseText);
      console.log(json);
      var pin = json.pincode;
      console.log(pin);
      document.getElementById("pincode").innerHTML = pin;
      
  }
};
xhttp1.send();