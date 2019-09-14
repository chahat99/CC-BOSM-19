
var xhttp = new XMLHttpRequest();
var question;
var team_name;
window.onload = load();
function load() {
  console.log(1);
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET","/treasure/get/question_details",true);
  xhttp.setRequestHeader("Content-Type","application/json");
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          var inst = JSON.parse(this.responseText);
          console.log(inst)
          document.getElementById("q-text").innerHTML = inst.Question;
      }
    };

    xhttp.send();
  }
// var pid = {
//   id1 : localStorage.getItem("id")
// }
// var participation_id = JSON.stringify(pid);
// xhttp.open("POST", "/treasure/get/question_details", true);
// xhttp.setRequestHeader("Content-Type", "application/json");
// xhttp.onreadystatechange = function() {
//   if (this.readyState == 4 && this.status == 200) {

//     var json = JSON.parse(this.responseText);
//     console.log(json);
//       question = json.question;
//       team_name = json.team_name;
//       document.getElementById("q-text").innerHTML = question;
//       console.log(question,team_name);
//   }
// };
// xhttp.send(participation_id);

function sendres() {
    var obj = {
      ans: document.getElementsByClassName("input2")[0].value,
      // id : localStorage.getItem("id")
    }
    console.log(obj);
    var sendans = JSON.stringify(obj);
    var res = new XMLHttpRequest();
    res.open("POST","/treasure/check_question_answer/",true);
    res.setRequestHeader("Content-Type", "application/json");
    res.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var flag = JSON.parse(this.responseText);
            console.log(flag)
            if(flag.status == 1) {
              window.location.href = "/treasure/question-main.html";
            }
            else {
              console.log(2);
              $(function(){
                  alert("Wrong answer!")
              });
            }
        }
    };
    res.send(sendans);
}
