/* 
Activity: Contact manager
*/

// TODO: Complete the program


console.log("Welcome to your contacts manager!");

do {
    console.log("1: List contacts");
    console.log("2: Add a contact");
    console.log("0: Quit");
    var Person = {
        //initialize the personalbar
        init: function(last, first)
            {
            this.last = last;
            this.first = first;
            },
        //Describe of peoples
        describe: function()
            {
            var description = "Last name: " + this.last + ", first name: " + this.first;
            return description;
            }
    };
    
    var person1 = Object.create(Person);
    person1.init("Smith", "John");
    var person2 = Object.create(Person);
    person2.init("Doe", "Jane");
    var person3;

    var peoples = [];
    peoples.push(person1);
    peoples.push(person2);

    function listPeople()
    {
        peoples.forEach(function(people)
                        {
                            console.log(people.describe());
                        });
    }

    function addNewPerson(last, first)
    {
        person3 = Object.create(Person);
        //  last = prompt("Enter last name for person: ");
        //  first = prompt("Enter first name for person: ");
        person3.init(last, first);
        var arrayPush = peoples.push(person3);
        return arrayPush;
    }
    var nmbr = prompt("Enter your digit(1. List contacts, 2.Add a contact or 0.Quit): ");
    var choice = parseInt(nmbr);
    switch(choice){
        case 1 : 
            console.log("Here`s the list of all your contacts: ");
            listPeople();
            break;
        case 2 : 
            last = prompt("Enter last name for person: ");
            first = prompt("Enter first name for person: ");
            addNewPerson(last, first);
            console.log("Contact added");
            listPeople();
            break;
        default:
            break;
    }
}
while (choice != 0);