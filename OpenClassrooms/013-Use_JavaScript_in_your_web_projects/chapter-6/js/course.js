var usernameElement = document.getElementById("username");
usernameElement.value = "MyCoolUsername";


// Focus and blur events
usernameElement.addEventListener("focus", function () {
    document.getElementById("usernameHelp").textContent = "Enter a unique username!";
});
usernameElement.addEventListener("blur", function () {
    document.getElementById("usernameHelp").textContent = "";
});

usernameElement.focus();


// Choice elements
// Checkbox
document.getElementById("confirmation").addEventListener("change", function (e) {
    console.log("Email confirmation request: " + e.target.checked);
});

// Radio
var subscriptionElements = document.getElementsByName("subscription");
for (var i = 0; i < subscriptionElements.length; i++) {
    subscriptionElements[i].addEventListener("change", function (e) {
        console.log("Selected subscription: " + e.target.value);
    });
};

// Dropdown
document.getElementById("nationality").addEventListener("change", function (e) {
    console.log("Nationality code: " + e.target.value);
});


// Validate forms
document.getElementById("password").addEventListener("input", function (e) {
    var password = e.target.value;
    var passwordLength = "weak";
    var messageColor = "red";
    if (password.length >= 8) {
        passwordLength = "strong"
        messageColor = "green";
    } else if (password.length >= 4) {
        passwordLength = "moderate";
        messageColor = "orange";
    };
    var passwordHelpElement = document.getElementById("passwordHelp");
    passwordHelpElement.textContent = "Strength: " + passwordLength;
    passwordHelpElement.style.color = messageColor;
});

document.getElementById("emailAddress").addEventListener("blur", function (e) {
    var emailAddressValidity = "";
    if (e.target.value.indexOf("@") === -1) {
        emailAddressValidity = "invalid address";
    }
    document.getElementById("emailHelp").textContent = emailAddressValidity;
});


// Regex
document.getElementById("emailAddress").addEventListener("blur", function (e) {
    var emailRegex = /.+@.+\..+/;
    var emailAddressValidity = "";
    if (!emailRegex.test(e.target.value)) {
        emailAddressValidity = "Invalid address";
    }
    document.getElementById("emailHelp").textContent = emailAddressValidity;
});