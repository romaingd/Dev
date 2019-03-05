

$(document).ready(function(){	
	//Load Html file via AJAX (file hosted in CodePen)
	$("#coreStore").load("https://codepen.io/Okozuki/pen/BvvMJJ.html");
    //Show Product List
	$("#thebutton").click(function(){
		$("#coreStore").slideDown(2000);
    });
	$("#home").click(function(){
		$("#coreStore").slideUp(2000);
	});	
});











