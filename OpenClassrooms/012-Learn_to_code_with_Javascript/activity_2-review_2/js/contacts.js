var Contacts = {
	init: function(firstName, lastName) {
		this.firstName = firstName;
		this.lastName = lastName;
	},

	describe: function() {
		var description = "Last name: " + this.lastName + ", first name: " + this.firstName;
		return description;

	}
	
};

var contact_0= Object.create(Contacts);
contact_0.init("John", "Smith");

var contact_1 = Object.create(Contacts);
contact_1.init("Jane", "Doe");

var contactLists = [contact_0, contact_1];

function displayMessage() {
	console.log("1: List contacts \n2: Add a contact \n0: Quit");

}

console.log("Welcome to your Contacts manager!");

var action = "";
while(action !== "Quit"){
	displayMessage();
	console.log("Here's the list of all your contacts: ");
	
	for (var i = 0; i < contactLists.length; i++) {
		console.log(contactLists[i].describe());
	}

	var first_name = prompt("Enter first name to add contact or type 'Quit' to exit:");
	action = first_name;
	displayMessage();
	if (first_name !== "Quit") {
		console.log("Contact added");
		var second_name = prompt("Enter last name to add contact:");
	}

	var contact = Object.create(Contacts);
	contact.init(first_name, second_name);
	contactLists.push(contact);
	
}

