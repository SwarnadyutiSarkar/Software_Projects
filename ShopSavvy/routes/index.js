// index.js
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const searchRouter = require('./routes/search');

app.use(bodyParser.json());
app.use('/search', searchRouter);

mongoose.connect('mongodb://localhost/shopsavvy', { useNewUrlParser: true, useUnifiedTopology: true });

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});