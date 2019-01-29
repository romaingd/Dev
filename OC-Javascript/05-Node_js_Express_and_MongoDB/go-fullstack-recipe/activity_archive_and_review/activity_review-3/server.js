const mongoose = require("mongoose");
const RecipeModel = require("./models/recipeModels");
const app = require("./app");

//DB connection|| mongodb+srv://Recipes:<PASSWORD>@cluster0-yix9w.mongodb.net/test?retryWrites=true
mongoose
    .connect(
        "mongodb+srv://Recipes:Recipes@cluster0-yix9w.mongodb.net/test?retryWrites=true"
    )
    .then(() => console.log("MongoDb connection successfull"))
    .catch(() => console.log("failed to connect to MongoDb Atlas"));

/****** Post /api/recipes */
app.post("/api/recipes", async (req, res) => {
    const newRecipe = new RecipeModel({
        title: req.body.title,
        ingredients: req.body.ingredients,
        instructions: req.body.instructions,
        difficulty: req.body.difficulty,
        time: req.body.time

    });
    const saveRecipe = await newRecipe.save();
    if (saveRecipe) {
        return res.status(201).json({
            message: "Data saved sucessfull!"
        });
    } else {
        return res.status(400).json({
            message: "failed to save data"
        });
    }
});

/****** GET /api/recipes */
app.get("/api/recipes", async (req, res) => {
    const recipes = await RecipeModel.find();
    res.json(recipes);
});
/****** GET /api/recipes/:id */
app.get("/api/recipes/:id", async (req, res) => {
    const recipeOne = await RecipeModel.findById({
        _id: req.params.id
    });
    console.log("data with given id gathered!");
    res.send(recipeOne);
});

/******* PUT /api/recipes/:id */
app.put("/api/recipes/:id", async (req, res) => {
    const updateOneRecipe = new RecipeModel({
        _id: req.params.id,
        title: req.body.title,
        ingredients: req.body.ingredients,
        instructions: req.body.instructions,
        time: req.body.time,
        difficulty: req.body.difficulty
    });
    const result_for_Update = await RecipeModel.findOneAndUpdate({
            _id: req.params.id
        },
        updateOneRecipe, {
            new: true
        }
    );
    res.send(result_for_Update);
});

/******* DELETE /api/recipes/:id */
app.delete("/api/recipes/:id", async (req, res) => {
    const recipeDeleteOne = await RecipeModel.findByIdAndRemove({
        _id: req.params.id
    });
    console.log("data with given id have been deleted!");
    res.send(recipeDeleteOne);
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Recipe app is running on port ${port}`));