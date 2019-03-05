/* Variables */
// Variable declaration
var a = 3.14;
console.log(a);

// Incrementation
var b = 0;
b += 1;
b++;
console.log(b);

// Implicit type conversion
var f = 100;
console.log("The variable f contains the value: " + f);

// Failing type conversion
var g = "five" * 2;
console.log(g);

// Explicit type conversion
var h = "5";
console.log(h + 1);
h = Number("5");
console.log(h + 1);


/* User interactions */
// Entering information
var name = prompt("Enter your first name:");
alert("Hello, " + name);