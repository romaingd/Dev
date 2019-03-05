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
    detailsLine.classList.add("info");
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


/***************
 * Start My Code
 *************** 
 */

// Add EventListener to Show Form Button
let showForm = document.getElementById('show-form');
showForm.addEventListener('click', function () {
    this.style.display = 'none';
    document.querySelector('form').style.display = 'block';
});

// Create saveData Function
function savaData() {
    let authorValue = document.getElementById('author').value;
    let titleValue = document.getElementById('title').value;
    let urlValue = document.getElementById('url').value;

   
    if(!urlValue.includes('http')){
        urlValue = "http://" + urlValue;
        console.log(urlValue);
        
    }
            
    var linkTitle = document.createElement("a");
    linkTitle.href = urlValue;
    linkTitle.style.color = "#00ADB5";
    linkTitle.style.textDecoration = "none";
    linkTitle.style.marginRight = "5px";
    linkTitle.appendChild(document.createTextNode(titleValue));

    var linkURL = document.createElement("span");
    linkURL.appendChild(document.createTextNode(urlValue));

    var TitleLine = document.createElement("h4");
    TitleLine.style.margin = "0px";
    TitleLine.appendChild(linkTitle);
    TitleLine.appendChild(linkURL);

    var infoLine = document.createElement("span");
    infoLine.appendChild(document.createTextNode("Added by " + authorValue));

    var linDiv = document.createElement("div");
    linDiv.classList.add("link");
    linDiv.appendChild(TitleLine);
    linDiv.appendChild(infoLine);

    return linDiv;
}

let addBtn = document.getElementById('add');
var box = document.getElementById("content");
var f = document.getElementsByTagName('form');
    addBtn.addEventListener("click", function () {
    document.querySelector('form').style.display = 'none';
    setTimeout( function(){
        document.getElementById('message').textContent = 'Item Added Properly';
        document.getElementById('message').style.display='block';
    } , 2000);
    var linkElem = savaData();
        box.insertBefore(linkElem, box.children[2]);
});
