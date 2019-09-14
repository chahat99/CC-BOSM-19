window.onload = function team() {
    var xhttp1 = new XMLHttpRequest();
    console.log(localStorage.getItem("id"));
    var obj={
      teamname :document.getElementsByClassName("input3")[0].value,
    };
var team_name=JSON.stringify(obj);
console.log(obj)
xhttp1.open("POST", "/treasure/create_team/", true);
xhttp1.setRequestHeader("Content-Type", "application/json");
xhttp1.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {

    var json = JSON.parse(this.responseText);
      console.log(json);
      var pin = json.team_code;
      console.log(pin);
      var pobj = {
        id : pin
      }
      var pinid = JSON.stringify(pobj);
      localStorage.setItem("pin",pinid)
      // document.getElementById("pincode").innerHTML = pin;
  }
};

xhttp1.send(team_name);
}
