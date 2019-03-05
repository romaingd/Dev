const mongoose = require('mongoose');

const recipeSchema = mongoose.Schema({
    title: String,
    ingredients: String,
    instructions: String,
    time: Number,
    difficulty: Number,
});

module.exports = mongoose.model('Recipe', recipeSchema);