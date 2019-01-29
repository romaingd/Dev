var titleElements = document.getElementsByTagName("h1");
console.log(titleElements[0]);

var wondersElements = document.getElementsByClassName("wonders");
for (var i = 0; i < wondersElements.length; i++) {
    console.log(wondersElements[i]);
};

console.log(document.getElementById("new"));

console.log(document.querySelectorAll("#ancient > .exists").length);

console.log(document.querySelector("p").innerHTML);
console.log(document.querySelector("p").textContent);

console.log(document.querySelectorAll("ul")[1].hasAttribute("id"));
console.log(document.getElementById("ancient").classList.contains("wonders"));
