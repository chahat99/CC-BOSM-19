
var refbut=document.getElementById("refbut");
var teamname=document.getElementById("teamname");
console.log('hello')

// function teamname() {
//     var xhr=new XMLHttpRequest();
//     xhttp.open("GET", "linkhere", true);
//     xhr.setRequestHeader("Content-Type",'application/json');
//     xhr.onreadystatechange=function() {
//         if (this.readyState==4 && this.status==200)
//         var json1 = JSON.parse(this.responseText);
//         document.getElementById("teamname").innerHTML = json.team_name;
//     }
//     xhr.send();
// }

var players= new Array(15);
var i=0;

refbut.addEventListener("click", addteam);


function addteam(){
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/treasure/team_list/", true);


    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           var json2 = JSON.parse(this.responseText);
           console.log(json2)
           document.getElementById("teamname").innerHTML = json2.teamname;
            for(i=0; i<json2.length; i++)
            {
                j=i+1;
                var player=document.getElementById("player"+j);
                players[i]=json2.teamlist[i];
                player.innerHTML=players[i];
            }
    }
};
    xhttp.send();
}
window.onload = addteam();
function redirect() {
    window.location.href = "/treasure/question-main.html"
}