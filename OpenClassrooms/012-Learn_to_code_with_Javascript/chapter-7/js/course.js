/* JavaScript and objects */
var pen = {
    type: "ballpoint",
    color: "blue",
    brand: "Bic",

    //Describe the cake
    describe: function() {
        var description = this.type + this.color + this.brand;
        return(description);
    }
}
console.log(pen.color);

pen.color = "red";
console.log(pen.color);

console.log(pen.describe());