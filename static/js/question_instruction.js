window.onload = load();
function load() {
var xhttp = new XMLHttpRequest();
xhttp.open("GET","/treasure/get/question_details",true);
xhttp.setRequestHeader("Content-Type","application/json");
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var inst = JSON.parse(this.responseText);
        console.log(inst)
        document.getElementById("show-text").innerHTML = inst.Question;
    }
  };
  
  xhttp.send();
}
function submitCode() {
  var send = new XMLHttpRequest();
  var obj = {
      ans : document.getElementById('code-to').value
  }
  var sendkey = JSON.stringify(obj);
  send.open("POST","/treasure/check_question_answer/",true);
  send.setRequestHeader("Content-Type","application/json");
  send.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var flag1 = JSON.parse(this.responseText);
        console.log(flag1)
        if(flag1.status == 1) {
            window.location.href = "/treasure/question-1.html";
          } else {
            alert("Wrong Key");
          }
    }
  };
  
  send.send(sendkey);
}
