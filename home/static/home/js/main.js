$(document).ready(function () {
var button = $('#sidebar-btn');
var sidebarDiv = $('#collapseExample');
var sidebar = $('#sidebar');
var content = $('#content');
var currentWidth = $(window).width();
button.on('click',function(){
if(sidebarDiv.hasClass('show') && sidebar.display == 'none'){
//sidebarDiv.removeClass('show');
sidebar.css('display','block');
sidebar.css('width','18%');
content.css('width','82%');
console.log('second');


}
else if(sidebarDiv.hasClass('show') && sidebar.display != 'none'){
sidebarDiv.removeClass('show');
sidebar.css('display','none');
content.css('width','100%');

}
else{

sidebarDiv.addClass('show');
sidebar.css('display','inline-block');
sidebar.css('width','40%');
content.css('width','60%');
console.log('first');
}



});


});