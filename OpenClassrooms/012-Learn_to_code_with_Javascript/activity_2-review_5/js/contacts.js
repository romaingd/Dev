console.log('Welcome to contact Manager!');
let a ='1:List of contacts \n2:Add a contact\n0:Quit';
console.log(a);
var contacts = ["John","Smith","Jane","Doe"];
var contact = {
    init: function (firstname,lastname) {
        this.firstname = firstname;
        this.lastname = lastname;
    },
    describe: function(){
        var description ="First name: " + this.firstname + "; " + "Last name: " + this.lastname + "."
        return description;
    }
   
};

var contact1 = Object.create(contact);
contact1.init("John","Smith");

var contact2 = Object.create(contact);
contact2.init("Jane","Doe");
var contacts = [];
contacts.push(contact1);
contacts.push(contact2);

    var number = Number(prompt("Enter a number:"));
    if (number===1) {
        console.log("Here is the list of your contacts:" )
   contacts.forEach(function(contact) {
    console.log(contact.describe())
   });
    console.log(a);
} else if (number===2) {
    var name = prompt ("Enter your First and Last name:");
    contacts.forEach(function(contact) {
    console.log(contact.describe())
   });
    console.log(a);
    console.log(name);
    console.log(a);
} else if ( number===0) {
    console.log();
}

        

   




    





    




 
