
var xhttp = new XMLHttpRequest();
var question;
var team_name;

var pid = {
  id1 : localStorage.getItem("id")
}
var participation_id = JSON.stringify(pid);
xhttp.open("POST", "url/", true);
xhttp.setRequestHeader("Content-Type", "application/json");
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {

    var json = JSON.parse(this.responseText);
    console.log(json);
      question = json.question;
      team_name = json.team_name;
      document.getElementById("q-text").innerHTML = question;
      console.log(question,team_name);
  }
};
xhttp.send(participation_id);

function sendres() {
    var obj = {
      ans : document.getElementsByClassName("input2").value,
      id : localStorage.getItem("id")
    }
    console.log(obj);
    var sendans = JSON.stringify(obj);
    var res = new XMLHttpRequest();
    res.open("POST","url/",true);
    res.setRequestHeader("Content-Type", "application/json");
    res.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var flag = JSON.parse(this.responseText).flag;
            console.log(flag)
            if(flag == 1) {
              window.location.href = "http://localhost:8000/treasure/question-main.html";
            } 
            else {
              $(function(){
                  $('#submit-btn').on('click', function(){
                    $('submit-btn').attr("href", "#myModal");
                  });
              });            
            }
        }
    };
    res.send(sendans);
}
