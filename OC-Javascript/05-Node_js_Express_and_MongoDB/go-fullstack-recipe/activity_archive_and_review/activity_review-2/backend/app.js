
const express = require('express');
const bodyParser= require('body-parser');
const mongoose=require('mongoose');
const Recipe= require('./models/recipe');
const app= express();

app.use((req,res,next)=>{
	res.setHeader('Access-Control-Allow-Origin','*');
	res.setHeader('Access-control-allow-Headers','Origin,X-Requested-With,Content, Accept,Content-Type, Authorization');
	res.setHeader('Access-Control-Allow-Methods','Get, POST,PUT,DELETE,PATCH, OPTIONS');
	next();
});

mongoose.connect('mongodb+srv://mongo-marc:2d4x02cMCVxuvf84@marccluster-yyppi.mongodb.net/test?retryWrites=true')
.then(()=>{
console.log('Successfully connected to MongoDB Atlas!');
})
.catch((error)=>{
	console.log('Unable to connect to MongoDB Atlas!');
	console.error(error);
});


app.use(bodyParser.json());


// app.get('/api/recipes',(req,res,next)=>{

// 	const recipes=[{
// 		 title: 'Marc recipe',
// 		  ingredients: 'mmmm',
// 		  instructions: 'read one line by line',
// 		  difficulty: 5,
// 		  time: 5,
// 		  _id: 'sdfasdfsadfas'
// 		},
// 		{
// 		 title: 'recipe',
// 		  ingredients: 'adad',
// 		  instructions: 'rrwerwe one line by line',
// 		  difficulty: 3,
// 		  time: 3,
// 		  _id: 'srwefsadfas'
// 		},
// 	];

// 	res.status(200).json(recipes);
// 	next();
// });

app.get('/api/recipes',(req,res,next)=>{
				Recipe.find().then((recipes)=>{
					res.status(201).json(recipes);
				})
				.catch(
					(error)=>{
						res.status(400).json({
							error:error
						});
					});
});

app.post('/api/recipes',(req,res,next)=>{
	
					const recipe= new Recipe({
						title:req.body.title,
						ingredients: req.body.ingredients,
						instructions: req.body.instructions,
						difficulty: req.body.difficulty,
						time: req.body.time

					});


					return recipe.save()
						.then(()=>{
							res.status(201).json({
								message: 'Post saved successfully!'
							});
							//console.log(req.body);
						})
						.catch((error)=>{

							res.status(400).json({
								error:error
							});
					});
		next();
});

app.get('/api/recipes/:id',(req,res,next)=>{

			Recipe.findOne({
				"_id":req.params.id
			})
			.then((recipes)=>{

					//console.log(recipes);
					res.status(200).json(recipes);
				})
				.catch((error)=>{
					res.status(404).json({
						error: error
					});
					
				});
				//console.log('recipexxx');
});

app.put('/api/recipes/:id',(req,res,next)=>{
	
	const recipe = new Recipe({
		_id: req.params.id,
	title:req.body.title,
	ingredients: req.body.ingredients,
	instructions: req.body.instructions,
	difficulty: req.body.difficulty,
	time: req.body.time
	});
	console.log('recipexxx'+recipe);

		 Recipe.updateOne({ _id: req.params.id }, recipe)
				.then(
						 	()=>{
						return	res.status(201).json({

								message: "Recipe updated successfully!"
							});
					})
				.catch(
					(error)=>{
						res.status(400).json({
							error:error
						});
					});
 });

app.delete('/api/recipes/:id',(req,res,next)=>{
	Recipe.deleteOne({_id: req.params.id}).then(
()=>{
	return res.status(200).json({
		message: 'Deleted!'
	});
}
		).catch(
(error)=>{
	res.status(400).json({
		error:error
	});
}
		);
});
module.exports=app;