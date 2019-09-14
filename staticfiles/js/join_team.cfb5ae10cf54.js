function joinTeam(){
  var xhttp = new XMLHttpRequest();
  var obj = {
    pin:document.getElementsByClassName("input2")[0].value,
    id : localStorage.getItem("id")
  }
  var pincode=JSON.stringify(obj)
  xhttp.open("POST", "jointeam/", true);
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var resp=JSON.parse(this.responseText);
      console.log(resp);
      if(resp.status == 1) {
        window.location.href = "/treasure/teams-page.html";
    }
    else {
        alert(resp.message);
    }
    }
  };

  xhttp.send(pincode);
}
