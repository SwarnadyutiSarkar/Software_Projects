// server.js
const express = require('express');
const app = express();
const port = 3000;

const natural = require('natural');
const tokenizer = new natural.WordTokenizer();

app.use(express.json());

app.post('/analyze', (req, res) => {
  const text = req.body.text;
  const tokens = tokenizer.tokenize(text);
  const sentiment = natural.sentiment.analyze(tokens);
  const entities = natural.entityRecognition.recognize(tokens);
  res.json({ sentiment, entities });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});