// 1. Create a new XMLHttpRequest object -- an object like any other
var myRequest = new XMLHttpRequest();

// 2. Open the request and pass the HTTP method name and the resource as parameters
myRequest.open('GET', 'suprise.html');

// 3. Write a function that runs anytime the state of the AJAX request changes
myRequest.onreadystatechange = function () {
    // 4. Check if the request has a readyState of 4, which indicates the
    //    server has responded (complete)
    if (myRequest.readyState === 4) {
        // 5. Insert the text sent by the server into the HTML of the 'ajax-content'
        document.getElementById('ajax-content').innerHTML = myRequest.responseText;
    }
};

function sendTheAJAX () {
    myRequest.send();
    document.getElementById('reveal').style.display = 'none';
}


/* Candy shop */
var req = XMLHttpRequest();
req.open('GET', '/candies.json');
req.onreadystatechange = function () {
    if (req.readyState === 4 && req.status === 200) {
        var candies = JSON.parse(req.responseText);
        var candyList = '<ul class="candies">';
        for (var i=0; i<candies.length; i++) {
            if (candies[i].quantity > 0) {
                candyList += '<li class="item available">';
            } else {
                candyList += '<li class="item sold-out">';
            };
            candyList += candies[i].name + '<br>' + "Brand: " + candies[i].brand;
            candyList += '<button>Buy</button>';
            candyList += '</li>';
        }
    }
    candyList += '</ul>';
    document.getElementById("candyListing").innerHTML = candyList;
};
req.send();
