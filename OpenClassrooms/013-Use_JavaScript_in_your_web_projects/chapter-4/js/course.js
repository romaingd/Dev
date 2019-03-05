var pElement = document.querySelector("p");
pElement.style.color = "red";
pElement.style.margin = "50px";

pElement.style.fontFamily = "Arial";
pElement.style.backgroundColor = "black";

var paragraphStyle = getComputedStyle(document.getElementById("para"));
console.log(paragraphStyle.fontStyle);