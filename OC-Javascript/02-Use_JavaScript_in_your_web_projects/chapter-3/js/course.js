document.getElementById("languages").innerHTML += '<li id="c">C</li>';
// document.getElementById("languages").innerHTML = "";

var titleElement = document.querySelector("h1");
titleElement.classList.remove("beginning");
titleElement.classList.add("title");
console.log(titleElement);

var pythonElement = document.createElement("li");
pythonElement.id = "python";
pythonElement.textContent = "Python";
document.getElementById("languages").appendChild(pythonElement);

document.getElementById("languages").insertAdjacentHTML("afterbegin", '<li id="javascript">JavaScript</li>');


var bashElement = document.createElement("li");
bashElement.id = "bash";
bashElement.textContent = "Bash";
document.getElementById("languages").replaceChild(bashElement, document.getElementById("java"));