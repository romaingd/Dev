/* 
Activity: Contact manager
*/

// Create the Contact class
function Contact(firstName, lastName) {
	this.firstName = firstName;
	this.lastName = lastName;
}

// Create the string function to return 
Contact.prototype.string = function() {return "Last name: " + this.lastName + ", first name: " + this.firstName;};

// Print out the commands that the user can use
function printCommands() {
	console.log("1: List contacts");
	console.log("2: Add a contact");
	console.log("0: Quit");
}

var contacts = [new Contact("John", "Smith"), new Contact("Jane", "Doe")];

$("#addButton").on("click", function() {
	$("#addContact").show();
});

$("#listButton").on("click", function() {
	$("#addContact").hide();
	$("#contactList").text("");
	contacts.forEach(function(contact){$("#contactList").append(contact.string() + "<br>");});
});

$("#quitButton").on("click", function() {
	$("#container").hide();
	$("#closePrompt").show();
});

$("#submitButton").on("click", function() {
	contacts.push(new Contact($("#firstNameBox").val(), $("#lastNameBox").val()));
	$("input:text").val("");
	$("#addContact").hide();
	$("#contactList").text("");
	contacts.forEach(function(contact){$("#contactList").append(contact.string() + "<br>");});
});