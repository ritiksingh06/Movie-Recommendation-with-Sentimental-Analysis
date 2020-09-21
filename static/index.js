function move_to_top(){
    var searchbox=document.getElementsByClassName("wrapper")[0];
    searchbox.classList.add("trans");
    var moviename = document.getElementById("movie").value;
    setTimeout(display_table, 2000);
}

function display_table()
{
  var table=document.getElementsByClassName("tables")[0];
  table.style.display="block";
  table.classList.add("effect")
}