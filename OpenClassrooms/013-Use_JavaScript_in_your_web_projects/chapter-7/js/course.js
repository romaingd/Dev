/* Bring pages to life */

// Decrease a counter until the explosion
var counterElement = document.getElementById("counter");

function decreaseCounter () {
    var counter = Number(counterElement.textContent);
    if (counter > 1) {
        counterElement.textContent = counter - 1;
    } else {
        clearInterval(intervalId);
        var title = document.getElementById("title");
        title.textContent = "BOOM!!";
        setTimeout(function () {
            title.textContent = "R.I.P."
        }, 2000);
    }
}

var intervalId = setInterval(decreaseCounter, 1000);