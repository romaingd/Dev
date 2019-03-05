const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const path = require('path');

/* Import routes */
const stuffRoutes = require('./routes/stuff');
const userRoutes = require('./routes/user');


const app = express();


/* Connecting to MongoDB cluster */
mongoose.connect('mongodb+srv://harry:harryros@go-fullstack-fmhoo.mongodb.net/test?retryWrites=true')
  .then(() => {
    console.log('Successfully connected to MongoDB Atlas!');
  })
  .catch((error) => {
    console.log('Unable to connect to MongoDB Atlas!');
    console.error(error);
  }
);


/* Middleware series */
app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Headers', 
                'Origin, X-Requested-With, Content, Accept, Content-Type, '
                + 'Authorization');
  res.setHeader('Access-Control-Allow-Methods',
                'GET, POST, PUT, DELETE, PATCH, OPTIONS');
  next();
});

app.use(bodyParser.json());

app.use('/api/stuff', stuffRoutes);
app.use('/api/auth', userRoutes);
app.use('/images', express.static(path.join(__dirname, 'images')));


module.exports = app;