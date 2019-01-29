//object creation
function contact(firstname, lastname) {
    this.firstname = firstname;
    this.lastname = lastname;
    this.affiche = function () {
        console.log("first name : " + this.firstname + " last name : " + this.lastname);
    };
}
//table creation
var contTab = new Array;
// function that i need 
function addcontact() {
    var f = prompt("first name");
    var l = prompt("last name");
    var cont = new contact(f, l);
    contTab.push(cont);
}

function afficheContact() {
    console.log(contTab.length);
    for (var i = 0; i < contTab.length; i++) {
        contTab[i].affiche();
    };
}
//traitement
var c = 3;
while (c > 0) {
    console.log("welcome to your contact manager ! ");
    console.log("1: lister contact ");
    console.log("2: add contact ");
    console.log("0: quitter ");
    c = prompt("your choice");
    switch (c) {
        case "0":
            break;
        case "1":
            console.log("Here's the list of all your contact ");
            afficheContact();
            break;
        case "2":
            addcontact();
            console.log("contact added ");
            break;
    }
}