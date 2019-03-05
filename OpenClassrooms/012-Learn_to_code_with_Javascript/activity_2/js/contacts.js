/* 
Activity: Contact manager
*/

// Define the Contact object
function Contact(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
};

// Default contact list
contact1 = new Contact("Jane", "Doe");
contact2 = new Contact("John", "Smith");
var contacts = [contact1, contact2];

// Welcome message
console.log("Welcome to your contacts manager!");

// Main loop
var stayInLoop = true;
while (stayInLoop) {
    console.log("1: List contacts");
    console.log("2: Add a contact");
    console.log("0: Quit");
    userInput = Number(prompt("Enter a number: "));
    switch (userInput) {
        case 0:
            // Quit
            stayInLoop = false;
            console.log("Goodbye!");
            break;
        case 1:
            // List contacts
            console.log("Here's the list of all your contacts:")
            contacts.forEach(function (contact) {
                                 console.log("Last name: " + contact.lastName + ", "
                                             + "first name: " + contact.firstName);
            });
            break;
        case 2:
            // Quit
            lastName = prompt("Please enter last name: ");
            firstName = prompt("Please enter first name: ");
            contactToAdd = new Contact(lastName, firstName);
            contacts.push(contactToAdd);
            console.log("Contact added");
            break;
    };
};