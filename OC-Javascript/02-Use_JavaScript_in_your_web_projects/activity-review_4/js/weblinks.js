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

function showForm() {
	// hide the "Add Link" button and show the form
	document.getElementById("addLink").style.display = "none";
	document.getElementById("formProper").style.display = "block";
}

function submitForm() {
	
	var title = document.getElementById("linkTitle").value;
    var url = document.getElementById("linkURL").value;
    var author = document.getElementById("username").value;

	// validate link URL
	var linkPattern = /http[s]?:\/\/.+/;
	if(!linkPattern.test(url)) {
		url = "http://" + url;
		document.getElementById("linkURL").value = url;
	}

	// create link object
	var newLink =     {
        title: title,
        url: url,
        author: author
    };
	
	// reset the form
	document.getElementById("formProper").reset();
	
	// create the link element and add it to the page
	var linkElement = createLinkElement(newLink);
	document.getElementById("content").prepend(linkElement);
	
	// hide the form and show the "Add Link" button
	document.getElementById("addLink").style.display = "block";
	document.getElementById("formProper").style.display = "none";
	
	// show the confirmation message for 2 seconds	
	document.getElementById("confirmation").innerHTML = "The link for \"" + title + "\" was successfully added";
	document.getElementById("confirmation").style.display = "block";
	setTimeout(function () {
            document.getElementById("confirmation").style.display = "none";
        }, 2000);
	
	// return false so the form does not get sent to the server
	return false;
}