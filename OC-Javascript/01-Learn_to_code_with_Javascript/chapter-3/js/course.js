// Conditions
var number = Number(prompt("Enter a number: "));
if (number > 0) {
    console.log(number + " is positive");
}
else if (number < 0) {
    console.log(number + " is negative")
}
else {
    console.log(number + " is zero");
}

if ((number >= 0) && (number <=100)) {
    console.log(number + " is between 0 and 100, both included");
}

// Logic
console.log("true && false", true && false);
console.log("true || false", true || false);
console.log("!true", !true);
console.log("!false", !false);

// Switch
var weather = prompt("What's the weather like?");
switch (weather) {
    case "sunny":
        console.log("T-Shirt");
        break;
    case "rainy":
        console.log("Umbrella");
        break;
    default:
        console.log("Not a valid weather type")
}