document.getElementById("theButton").addEventListener("click", function (e) {
    console.log("Event: " + e.type + ", target text: " + e.target.textContent);
});


// Show information on a keyboard event
function keyboardInfo (e) {
    console.log("Keyboard event: " + e.type + ", key: " + e.keyCode);
}

document.addEventListener("keydown", keyboardInfo);
document.addEventListener("keyup", keyboardInfo);


// Show information on a mouse event
function getMouseButton (code) {
    var button = "unknown";
    switch (code) {
        case 0:
            button = "left";
            break;
        case 1:
            button = "middle";
            break;
        case 2:
            button = "right";
            break;
    }
    return button;
}

function mouseInfo (e) {
    console.log("Mouse event: " + e.type
                + ", button " + getMouseButton(e.button)
                + ", X: " + e.clientX
                + ", Y: " + e.clientY);
}

document.addEventListener("click", mouseInfo);


// Web page loading event
window.addEventListener("load", function () {
    console.log("The page has been loaded!");
})


// Click handler
document.addEventListener("click", function () {
    console.log("Document handler");
});
document.getElementById("para").addEventListener("click", function () {
    console.log("Paragraph handler");
});
document.getElementById("propa").addEventListener("click", function (e) {
    console.log("Button handler");
    e.stopPropagation();
})