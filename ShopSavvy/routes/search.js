// routes/search.js
const express = require('express');
const router = express.Router();
const Product = require('../models/Product');

router.get('/search', async (req, res) => {
  const query = req.query.q;
  const products = await Product.find({ $text: { $search: query } });
  res.json(products);
});

module.exports = router;