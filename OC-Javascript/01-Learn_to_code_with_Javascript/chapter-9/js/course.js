var films = ["Jurassic Park", "Titanic", "Toy Story"];

console.log(films.length);
console.log(films[0]);

films.push("The Revenant");
console.log(films[3]);



/* Object arrays */
var Film = {
    init: function (title, year) {
        this.title = title;
        this.year = year;
    },

    describe: function () {
        var description = this.title + " (" + this.year + ")";
        return description;
    }
};

var film1 = Object.create(Film);
film1.init("Jurassic Park", 1993);

var film2 = Object.create(Film);
film2.init("Titanic", 1997);

var film3 = Object.create(Film);
film3.init("Toy Story", 1995);

var films = [];
films.push(film1);
films.push(film2);
films.push(film3);

films.forEach(function (film) {
    console.log(film.describe());
})