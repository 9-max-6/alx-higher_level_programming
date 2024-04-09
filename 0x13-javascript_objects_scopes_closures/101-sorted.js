#!/usr/bin/node
const { dict } = require('./101-data.js');
const newDict = {};
for (const [userId, occurrence] of Object.entries(dict)) {
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }
  newDict[occurrence].push(parseInt(userId));
}
console.log(newDict);
