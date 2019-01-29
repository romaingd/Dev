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


function ADD() {
    var title = document.getElementById("title").value;
    var url = document.getElementById("url").value;
    var author = document.getElementById("author").value;

    var newLink = {
        title : title,
        url : url,
        author : author,
    }

    var regex = /http:\/\//;

    if (regex.test(newLink.url) === false) {
        newLink.url = "http://" + newLink.url;
    }

    linkList.push(newLink);

    var linktitle = document.createElement("a");
    linktitle.href = newLink.url;
    linktitle.style.color = "#428bca";
    linktitle.style.textDecoration = "none";
    linktitle.style.marginRight = "5px";
    linktitle.appendChild(document.createTextNode(newLink.title));

    var linkUrl = document.createElement("span");
    linkUrl.appendChild(document.createTextNode(newLink.url));

    var titleLine = document.createElement("h4");
    titleLine.style.margin = "0px";
    titleLine.appendChild(linktitle);
    titleLine.appendChild(linkUrl);

    var detailsLine = document.createElement("span");
    detailsLine.appendChild(document.createTextNode("Added by " + newLink.author));

    var linkDiv = document.createElement("div");
    linkDiv.classList.add("link");
    linkDiv.appendChild(titleLine);
    linkDiv.appendChild(detailsLine);

    document.getElementById("content2").appendChild(linkDiv);

    var elems = document.getElementsByClassName('form');
    for (var i=0;i<elems.length;i+=1){
        elems[i].style.display = 'none';
    }

    var elems2 = document.getElementsByClassName('addlink');
    for (var i=0;i<elems2.length;i+=1){
        elems2[i].style.display = 'inline';
    }
    document.getElementById("title").value = "";
    document.getElementById("url").value = "";
    document.getElementById("author").value = "";

    var msg = "Your link has been successfully added"

    setTimeout(function () {
    document.getElementById("confirm").innerHTML = msg;
    }, );


    setTimeout(function () {
    document.getElementById("confirm").innerHTML = "";
    }, 2000);
}


function showForm() {
    var elems = document.getElementsByClassName('form');
    for (var i=0;i<elems.length;i+=1){
        elems[i].style.display = 'inline';
    }

    var elems2 = document.getElementsByClassName('addlink');
    for (var i=0;i<elems2.length;i+=1){
        elems2[i].style.display = 'none';
    }
}
