#!/usr/bin/node
class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    this.print(c);
  }
}
module.exports = Square;
