const text =
  "<button id='btn_less'>See less<i class='uil uil-angle-up'></i></button>";

function show() {
  events_here_id.classList.remove("events_here");
  events_here_id.classList.add("events_here2");
}

function change() {
  btn = document.getElementById("btn_more");
  btn.innerHTML = text;
}

button1 = document.getElementById("btn_with_functions");

button1.addEventListener("click", show);
button1.addEventListener("click", change);

const text2 =
  "<button id='btn_with_functions' type='button'>More Events<i class='uil uil-plus'></i></button>";
function changeAgain() {
  btn = document.getElementById("btn_more");
  btn.innerHTML = text2;
}
button2 = document.getElementById("btn_less");
button2.addEventListener("click", changeAgain);
