function set_body_height() { // set body height = window height
    $('body').height($(window).height());
  }
  $(document).ready(function() {
      $(window).bind('resize', set_body_height);
      set_body_height();
});


function reset_animation() {
  var el = document.getElementById('map');
  el.style.animation = 'none';
  el.offsetHeight; /* trigger reflow */
  el.style.animation = null;
}



$(function(){
  $('#map-button').on('click',function(){
    $('#map').addClass('map-animation-2');
    $('#map').removeClass('map-animation')
  });
});


$(function(){
  $('#map-close').on('click',function(){
    $('#map').addClass('map-animation');
    $('#map').removeClass('map-animation-2');
  });
});


var state;
function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     var json=JSON.parse(this.responseText);
     state=json.questionstate;
    }
  };
  xhttp.open("GET", "", true);
  xhttp.send();
}

window.onload=function(){
  if(state==1){
    $("#map").attr('src', '{% static 'assets/images/Map 1.svg' %}');
    }
  if(state==2){
    $("#map").attr('src', '{% static 'assets/images/Map 2.svg' %}');
  }
  if(state==3){
    $("#map").attr('src', '{% static 'assets/images/Map 3.svg' %}');
  }
  if(state==4){
    $("#map").attr('src', '{% static 'assets/images/Map 4.svg' %}');
  }
}