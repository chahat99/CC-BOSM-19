function team() {
    var xhttp1 = new XMLHttpRequest();
    var obj={
      team:document.getElementsByClassName("input3")[0].value,
      id : localStorage.getItem("id")
    };
var team_name=JSON.stringify(obj);
xhttp1.open("POST", "/treasure/create_team/", true);
xhttp1.setRequestHeader("Content-Type", "application/json");
xhttp1.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var json = JSON.parse(this.responseText);
      console.log(json);
      var pin = json.pin;
      document.getElementById("pincode").innerHTML = pin;
  }
};

xhttp1.send(team_name);
}