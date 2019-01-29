var frame = document.getElementById("frame");
var block = document.getElementById("block");

var blockWidth = parseFloat(getComputedStyle(block).width);
var movement = 7;

function moveBlock() {
    var xBlock = parseFloat(getComputedStyle(block).left);
    var xMax = parseFloat(getComputedStyle(frame).width);
    if (xBlock + blockWidth <= xMax) {
        block.style.left = (xBlock + movement) + "px";
        animationId = requestAnimationFrame(moveBlock);
    } else {
        cancelAnimationFrame(animationId);
    }
}

animationId = requestAnimationFrame(moveBlock);