$('#show-albums').on('click', function(){
  $('#albums-ajax-content').load('./albums.html');
  $('#main-content').hide();
})