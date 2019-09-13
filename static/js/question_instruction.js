var xhttp = new XMLHttpRequest();
xhttp.open("GET","",true);
xhttp.setRequestHeader("Content-Type","application/json");
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var inst = JSON.parse(this.responseText);
        document.getElementById("").innerHTML = inst.instructions;
    }
  };
  
  xhttp1.send();

  var send = new XMLHttpRequest();
  var obj = {
      key : document.getElementsByClassName[0].value
  }
  var sendkey = JSON.stringify(obj);
  send.open("POST","",true);
  send.setRequestHeader("Content-Type","application/json");
  send.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var flag1 = JSON.parse(this.responseText);
        if(flag1 == 1) {
            window.location.href = "http://localhost:8000/treasure/question-1.html";
          } else {
            alert("Wrong Key");
          }
    }
  };
  
  send.send(sendkey);