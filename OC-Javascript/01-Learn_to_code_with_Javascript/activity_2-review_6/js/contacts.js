// Constructor for a contact
function Contact(first, last) {
  this.first = first;
  this.last = last;
}
// Add the two initial contacts
var contacts = [];
var contact0 = new Contact("John", "Smith");
contacts.push(contact0);
var contact1 = new Contact("Jane", "Doe");
contacts.push(contact1);

console.log("Welcome to your contacts manager!");
console.log("1: List contact");
console.log("2: Add a contact");
console.log("0: Quit");
var choice = prompt();

while (choice != 0) {

  if(choice == 1) {
    console.log("Here's the list of all your contacts:");
     for(var i = 0; i < contacts.length; i++) {
       console.log("Last name: " + contacts[i].last + ", first name: " + contacts[i].first);
     }
   }
   else if(choice == 2) {
     var toAddContact = prompt("Contact name: ");
     fullName = toAddContact.split(" ");
     var newContact = new Contact(fullName[0], fullName[1]);
     contacts.push(newContact);
     console.log("Contact added");
   }
   else {
     console.log("Invalid choice, sorry :( ");
   }
   console.log("1: List contact");
   console.log("2: Add a contact");
   console.log("0: Quit");
   choice = prompt();
}
console.log("Goodbye!");