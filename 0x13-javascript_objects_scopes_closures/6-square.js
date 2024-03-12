#!/usr/bin/node

const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrinti (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
