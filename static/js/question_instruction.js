var xhttp = new XMLHttpRequest();
xhttp.open("GET","",true);
xhttp.setRequestHeader("Content-Type","application/json");
xhttp1.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var inst = JSON.parse(this.responseText);
        document.getElementById("").innerHTML = inst.instructions;
    }
  };
  
  xhttp1.send();