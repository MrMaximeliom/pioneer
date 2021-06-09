
let button = document.getElementById('liveToastBtn');
let buttonC = document.getElementsByClassName('toast');
 button.addEventListener("click",()=>{
$('#liveToast').toast('show');
 });