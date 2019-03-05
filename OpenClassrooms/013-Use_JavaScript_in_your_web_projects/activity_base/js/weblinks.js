// List of links to show. Each link has:
// - a title
// - a URL
// - an author (the person who added it)

var linkList = [
    {
        title: "Kottke",
        url: "http://kottke.org",
        author: "brett.suggs"
    },
    {
        title: "National Geographic",
        url: "http://www.nationalgeographic.com",
        author: "jessica"
    },
    {
        title: "American Museum of Natural History",
        url: "http://www.amnh.org",
        author: "aurora.nicole"
    }
];

function createLinkElement(link) {
    var linktitle = document.createElement("a");
    linktitle.href = link.url;
    linktitle.style.color = "#428bca";
    linktitle.style.textDecoration = "none";
    linktitle.style.marginRight = "5px";
    linktitle.appendChild(document.createTextNode(link.title));

    var linkUrl = document.createElement("span");
    linkUrl.appendChild(document.createTextNode(link.url));

    var titleLine = document.createElement("h4");
    titleLine.style.margin = "0px";
    titleLine.appendChild(linktitle);
    titleLine.appendChild(linkUrl);

    var detailsLine = document.createElement("span");
    detailsLine.appendChild(document.createTextNode("Added by " + link.author));

    var linkDiv = document.createElement("div");
    linkDiv.classList.add("link");
    linkDiv.appendChild(titleLine);
    linkDiv.appendChild(detailsLine);

    return linkDiv;
}

var content = document.getElementById("content");
linkList.forEach(function (link) {
    var linkElement = createLinkElement(link);
    content.appendChild(linkElement);
});


// Retrieve various DOM elements:
//  - "Add link" button
//  - Form and form div
//  - Blue banner that will hold the "successfully added" message
var addLinkButtonElement = document.getElementById("add-link-button");
var formElement = document.getElementById('addLinkForm');
var formDivElement = document.getElementById('form-div');
var bannerElement = document.getElementById('banner');

// We chose to implement all elements in HTML from the beginning,
// and hide/show the various elements at various steps.
// The banner is initially not displayed.
bannerElement.style.display = 'none';

// displayAddingForm and hideAddingForm are inverse functions, hiding or
// showing various elements depending on the button clicked.
displayAddingForm = function (){
    addLinkButtonElement.style.display = 'none';
    formDivElement.style.display = '';
};
hideAddingForm = function (){
    addLinkButtonElement.style.display = '';
    formDivElement.style.display = 'none';
};

// Override the form submission
handleSubmit = function () {
    if (!formElement.checkValidity()) {
        return false;
    }
    var linkToAdd = {       // Retrieve form information
        title: formElement.title.value,
        url: formElement.url.value,
        author: formElement.author.value
    };
    var linkElement = createLinkElement(linkToAdd);
    content.insertBefore(linkElement, content.firstChild);
    displayBanner(linkToAdd.title);     // Display the banner, with a timeout
    hideAddingForm();                   // Hide the form
    return true;
};

displayBanner = function(title) {
    var bannerMessageText = 'The link to "' + title + '" was successfully added';
    bannerMessageElement = document.createTextNode(bannerMessageText);
    bannerElement.appendChild(bannerMessageElement);
    bannerElement.style.display = "";
    setTimeout(function () {
        bannerElement.style.display = 'none';
        bannerElement.removeChild(bannerElement.firstChild);    // Remove the old message
    }, 2000)
};

// The default behavior is to hide the form and show the "Add link" button
hideAddingForm();


// Make sure URL starts with "http://" or "https://"
var urlElement = document.getElementById("url");
urlElement.addEventListener("blur", function (e) {
    console.log(urlElement.value);
    var httpRegex = /^https?:\/\//;
    if (!httpRegex.test(urlElement.value)) {
        urlElement.value = "http://" + urlElement.value;
    }
})