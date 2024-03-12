#!/usr/bin/node

const { dict } = require('./101-data');

const usersByOccurrence = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (occurrences in usersByOccurrence) {
    usersByOccurrence[occurrences].push(userId);
  } else {
    usersByOccurrence[occurrences] = [userId];
  }
}

console.log(usersByOccurrence);
