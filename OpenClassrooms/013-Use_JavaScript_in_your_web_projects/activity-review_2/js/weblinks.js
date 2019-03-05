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
};

//CREATES NEW DIV ELEMENT 
function addDiv() {
    var newDiv = document.createElement('div');
    newDiv.style.display = 'block';
    newDiv.className = 'addlink-div'

    return newDiv;
};

//CREATES NEW LINK BUTTON INPUT FIELD
function addLink() {
    var addNewLink = document.createElement('button');

    addNewLink.textContent = 'Add Link';
    addNewLink.style.height = '1.5rem'
    addNewLink.style.marginBottom = '1rem';
    addNewLink.style.padding = '0.25rem 0.5rem';
    

    
    addNewLink.id = 'add-link-button';

    return addNewLink;
};

//CREATES NEW NAME INPUT FIELD
function addNameForm() {
    var addedForm = document.createElement('input');
    var textArea = document.createElement('span');
   
    
    addedForm.placeholder = 'Your Name';
    addedForm.type = 'text';
    addedForm.attributes.required = 'true';

    addedForm.style.textAlign = 'center';
    addedForm.style.margin = '1rem 0';
    addedForm.style.marginRight = '0.5rem';
    addedForm.style.padding = '.25rem 0';
    addedForm.style.display = 'none';

    addedForm.id = 'name';

    
    addedForm.appendChild(textArea);

    return addedForm

};

//CREATES NEW TITLE INPUT FIELD
function addTitleForm() {
    var addedForm = document.createElement('input');
    var textArea = document.createElement('span');
    
    addedForm.placeholder = 'Link title';
    addedForm.type = 'text';
    addedForm.required;

    addedForm.style.textAlign = 'center';
    addedForm.style.margin = '1rem 0';
    addedForm.style.marginRight = '0.5rem';
    addedForm.style.padding = '.25rem 0';
    addedForm.style.display = 'none';


    addedForm.id = 'link-title';

    addedForm.appendChild(textArea);

    return addedForm

};

//CREATES NEW LINK INPUT FIELD
function addLinkForm() {
    var addedForm = document.createElement('input');
    var textArea = document.createElement('span');
    
    addedForm.placeholder = 'Link-url';
    addedForm.type = 'text';
    addedForm.required;

    addedForm.style.width = '15%';
    addedForm.style.textAlign = 'center';
    addedForm.style.margin = '1rem 0';
    addedForm.style.marginRight = '0.5rem';
    addedForm.style.padding = '.25rem 0';
    addedForm.style.display = 'none';

    addedForm.id = 'link-input';

    addedForm.appendChild(textArea);

    return addedForm

};

// ADDS DISPLAY MESSAGE AFTER SUBMIT 
function addMessage() {
    var displayMessage = document.createElement('h2');
    
    displayMessage.style.fontStyle = 'sans serif';
    displayMessage.style.fontSize = '1.8 rem';
    displayMessage.style.backgroundColor = 'rgb(81, 203, 238)';
    displayMessage.style.color = 'rgb(24, 104, 126)';
    displayMessage.style.padding = '.5rem';
    displayMessage.style.paddingLeft = '3rem';
    displayMessage.style.boxShadow = '9px 10px 29px -2px rgba(0,0,0,0.63);'
    displayMessage.style.display = 'none';
    

    displayMessage.id = 'display-message'

    // displayMessage.textContent = 'The link to ' + '"' + linkList[0].title + '"' + ' was successfully added';

    return displayMessage;
}

//CREATES SUBMIT BUTTON ELEMENT
function addSubmitButton() {
    var addedButton = document.createElement('button');
    
    addedButton.textContent = 'Add Link';
    addedButton.setAttribute = 'disabled', 'true';

    addedButton.style.padding = '0.25rem 0.5rem';
    addedButton.style.display = 'none';

    addedButton.id = 'submit-button';

    return addedButton

};

// THESE NEED TO BE ABOVE THE CODE BELOW
var divElement = addDiv();
var content = document.getElementById('content');

// Calling functions and adding them to the DOM NEEDS UPDATING

content.appendChild(divElement);
divElement.appendChild(addMessage());
divElement.appendChild(addLink());
divElement.appendChild(addNameForm());
divElement.appendChild(addTitleForm());
divElement.appendChild(addLinkForm());
divElement.appendChild(addSubmitButton());

//EVENT LISTENERS AND VARIABLES
var nameInput = document.getElementById('name');
var titleInput = document.getElementById('link-title');
var linkInput = document.getElementById('link-input');
var submitButton = document.getElementById('submit-button');
var addLinkButton = document.getElementById('add-link-button');
var displayMessage = document.getElementById('display-message');
var inputFields = document.querySelectorAll('input');

//TOGGLE ADD LINK INPUT FIELDS
addLinkButton.addEventListener('click', function() {
    if(addLinkButton.style.display = 'block') {

        nameInput.style.display = 'inline-block';
        titleInput.style.display = 'inline-block';
        linkInput.style.display = 'inline-block';
        submitButton.style.display = 'inline-block';
        addLinkButton.style.display = 'none';
    }
})

//ADDING FOCUS STYLE TO INPUT FIELDS
divElement.addEventListener('focus', function() {
    divElement.style.color = 'blue';
})

//ADDS TEXT CONTENT OF INPUT FIELDS TO LINKLIST 
submitButton.addEventListener('click', function($event) {

    inputFields.forEach(form => {
        if(form.value.length < 1) {
            form.style.border = '1px solid red';
            submitButton.preventDefault();
        } else {
            form.style.border = '1px solid rgba(81, 203, 238, 1)';
        }
    });

    //CHECKS FOR HTTP://
    if(linkInput.value !== 'http://') {
        var newLinkUrl = 'http://' + linkInput.value;
    } else {
        var newLinkUrl = linkInput.value;
    };

    //TOGGLE ADD LINK INPUT FIELDS
    if(addLinkButton.style.display = 'none') {
        nameInput.style.display = 'none';
        titleInput.style.display = 'none';
        linkInput.style.display = 'none';
        submitButton.style.display = 'none';
        displayMessage.style.display = 'block';
        addLinkButton.style.display = 'block';
    };

    //INPUTS DATA FROM INPUT FIELDS INTO NEW OBJECT
    var newLink = 
    {
        title: titleInput.value,
        url: newLinkUrl,
        author: nameInput.value
    }
 ;

 //ADDS NEW CONTENT TO LINKLIST
 linkList.unshift(newLink);
 
 //APPENDS NEW CONTENT TO DOM
 var linkElement = createLinkElement(newLink);
 content.appendChild(linkElement);

 //DISPLAYS NEW MESSAGE 
 displayMessage.textContent = 'The link to ' + '"' + linkList[0].title + '"' + ' was successfully added';
 
 //DISPLAYS DISPLAY MESSAGE FOR 2 SECONDS
 setTimeout(() => {
    displayMessage.style.display = 'none';

 }, 2000);

 return 
});

//INITIALIY ADDS LINKLIST ITEMS TO THE DOM

linkList.forEach(function (link) {
    var linkElement = createLinkElement(link);
    content.appendChild(linkElement);
});


