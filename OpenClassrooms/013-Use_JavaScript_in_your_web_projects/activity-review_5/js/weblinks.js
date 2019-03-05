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
	linktitle.target = "_blank";
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

// Show Form
function showForm() {
  document.getElementById("form1").innerHTML = "";
  //document.getElementById("form1").appendChild(createForm());
  createForm();
}

  //Create form
  function createForm() {
	
	var yourName = document.createElement("input");
	var linkTitle = document.createElement("input");
	var linkURL = document.createElement("input");
	var addButton = document.createElement("button");
	yourName.type = "text";
	yourName.placeholder = "Your Name";
	yourName.id = "yourName";
	yourName.required = true;
	document.getElementById("form1").appendChild(yourName);
	
	linkTitle.type = "text";
	linkTitle.placeholder = "Link Title";
	linkTitle.id = "linkTitle";
	linkTitle.required = true;
	linkTitle.style.marginLeft = "15px";
	document.getElementById("form1").appendChild(linkTitle);
	
	linkURL.type = "url";
	linkURL.placeholder = "Link URL";
	linkURL.id = "linkURL";
	linkURL.required = true;
	linkURL.style.marginLeft = "15px";
	document.getElementById("form1").appendChild(linkURL);
	  
	var t = document.createTextNode("Add");
	addButton.id = "Add";
	addButton.style.marginLeft = "15px";
	addButton.appendChild(t);
	document.getElementById("form1").appendChild(addButton);
  
    
	// Validate the inputted URL
	document.getElementById("linkURL").addEventListener("blur", function (e) {
		// matches an http/https:// format
		var urlRegex = /http\:\/\/.+/;
		var urlRegex1 = /https\:\/\/.+/;
		var urlValid = "";
		if ((urlRegex.test(e.target.value)) || (urlRegex1.test(e.target.value))) {
			urlValid = e.target.value;
		}
		else {
			urlValid = "http://" + e.target.value;
		}
		document.getElementById("linkURL").value = urlValid;
    });

	//Form Validation
    function validateForm() {
      var x = yourName.value;
      var y = linkTitle.value;
      var z = linkURL.value;
	  //Verify Imput fields (required)
      if ((x == "") || (y == "") || (z == "")) {
      alert("Hello My Friend!\n\nEntering Title, Author and URL link is mandatory!\n\n Please Take Your Time To Fill All the Fields :)\n\nThank You!");
      return false;
      }
      else {
        //add new objet to linkList1
    linkList1 = [
      {
        title: y,
        url: z,
        author: x
      }
	];
	//Add new link to content div
    
    var content = document.getElementById("content");
    linkList1.forEach(function (link) {
    var linkElement = createLinkElement(link);
    content.insertAdjacentElement("afterbegin", linkElement);
	});
   
	//Add New div (Success message)
    //document.getElementById("form2").appendChild(createAddedDiv());
	createAddedDiv();
    
		}
	} 
	
	//Set onclick Event on Add button
    document.getElementById("Add").onclick = validateForm;
	
	//Create div With "Success Message" after Validation
	function createAddedDiv() {
	var formArea = document.getElementById("form1");
    var sucDiv = document.getElementById("form2");
    formArea.innerHTML = "";
	var successText = document.createElement("h4");
    successText.id = "successText";
    successText.appendChild(document.createTextNode("The link to "+'"'+linkTitle.value+'"'+" was added successfully!!"));
    sucDiv.appendChild(successText);
	// Modify the sucDiv after 2 seconds
        setTimeout(function () {
        document.getElementById("form2").innerHTML = "";
          //Magic Button
        formArea.insertAdjacentHTML("afterbegin", '<button onclick="showForm()" id="theButton" >Add link</button>');  
      }, 2000);
	}
}













