var i = 0;
function spam(){
  setInterval(function(){
	document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = 'hi';
	$('.im_submit').trigger('mousedown');	
	i++;
	console.log(i + ' MESSAGES SENT');
  } , 1000 ) ;
}
spam()
