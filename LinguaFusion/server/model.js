// model.js
const natural = require('natural');

const sentimentModel = new natural.SentimentAnalyzer('english');
const entityModel = new natural.EntityRecognizer('english');

module.exports = {
  sentimentModel,
  entityModel,
};