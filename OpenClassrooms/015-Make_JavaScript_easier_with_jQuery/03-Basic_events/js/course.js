$(function() {
  // Window dimensions
  var width = ($(window).width()) - 440;
  var height = ($(window).height()) - 360;

  // Show the image at location 100, 100
  var p = $('#target').offset();
  p.top = 100;
  p.left = 100;
  $('#target').offset(p);

  // Click handler and image movement
  $('#target').on('mouseenter', function() {
    x = Math.floor(Math.random() * width);
    y = Math.floor(Math.random() * height);
    var p = $('#target').offset();
    p.top = x;
    p.left = y;
    $('#target').offset(p);
  });
});
