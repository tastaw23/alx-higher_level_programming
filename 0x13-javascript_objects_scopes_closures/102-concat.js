#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }

    const concatenatedData = dataA.trim() + '\n' + dataB.trim();

    fs.writeFile(destinationFile, concatenatedData, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Concatenated files ${fileA} and ${fileB} into ${destinationFile}`);
    });
  });
});
