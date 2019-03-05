$('#ball').hide().fadeIn('slow');

console.log('OK');
function roll() {
  $('#ball').animate({left: '+=150'}, 'slow')
            .animate({left: '-=150'}, 'fast');
};
setInterval(roll, 600);

// $('#move-me').animate({
//   left : "+=150"
// }, 1000);