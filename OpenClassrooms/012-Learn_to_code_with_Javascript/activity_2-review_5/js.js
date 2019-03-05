/* 
Activity: Contact manager
*/
  
// TODO: Complete the program
  
var contact = {
    // initialize the contact
    init: function (firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    },
 
    describe: function () {
        var contacts = this.firstName + " " + this.lastName;
        return contacts;
    }
};
 
  
var contact1 = Object.create(contact);
contact1.init("John ", "Smith");
 
var contact2 = Object.create(contact);
contact2.init("Jane ", "Doe");
  
// Creating the table containing the contacts
var contacts=[];
contacts.push(contact1);
contacts.push(contact2);
 
 
  
// Creating the table containing the options
var option = ["1 : List of contacts", "2 : Add a contact", "0 : Quit"];
  
console.log ("Welcome to the contact manager !");
  
while (userChoice !== 0) {
    for (var i = 0; i < option.length; i++) {
        console.log(option[i]);
    };
    var userChoice = Number(prompt("Choose an option :"));
    switch (userChoice) {
  
        case 1:
        console.log("Here's the list of all your contacts :");
        console.log("-------------------------------------");
            for (var i = 0; i < contacts.length; i++) {
            console.log("First name : " + contacts[i].firstName +", "+" Last name : " + contacts[i].lastName);
            };
            console.log("-------------------------------------");
            break;
        case 2:
            var firstName = prompt("Entrer the first name");
            var lastName = prompt("Entrer the last name");
            var contactName = "contact" + contacts.length;
            contactName = Object.create(contact);
            contactName.init(firstName, lastName);
            contacts.push(contactName);
            console.log("The contact was added !");
            break;
        case 0:
            console.log("--------------------------------------------");
            console.log("--------------- Goodbye ! ------------------");
            console.log("--------------------------------------------");
        }
}