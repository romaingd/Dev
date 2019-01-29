$(function(){
});

/* Add content */
$('h2').append('***');
$('#three').after('<hr>');


/* Add elements */
// $('h2').replaceWith('<h3>')      // Wrong, deletes content
$('h2').each(function() {
  var elemH2 = $(this);
  elemH2.replaceWith('<h3>' + elemH2.text() + '</h3>')
});

$('<li>Second and a half element</li>').prependTo($('li:nth-child(2)'));
$('<li>Second and a half element fixed</li>').insertBefore($('li:nth-child(2)'));

$('li').wrap('<i></i>');
$('p').css('background-color', 'yellow');