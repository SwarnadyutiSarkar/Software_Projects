// worker.js
const natural = require('natural');
const { sentimentModel, entityModel } = require('./model');

process.on('message', (msg) => {
  if (msg.type === 'analyze') {
    const text = msg.text;
    const tokens = natural.WordTokenizer.tokenize(text);
    const sentiment = sentimentModel.analyze(tokens);
    const entities = entityModel.recognize(tokens);
    process.send({ type: 'result', sentiment, entities });
  }
});