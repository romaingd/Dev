// Get started with the DOM
var h = document.head;
console.log(h);

var b = document.body;
console.log(b);

if (document.body.nodeType === document.ELEMENT_NODE) {
    console.log("Body is an element node!");
} else {
    console.log("Body is a textual node!");
};

console.log(document.body.childNodes[1]);

document.body.childNodes.forEach(function (child) {
    console.log(child);
    console.log(child.nextSibling);
});