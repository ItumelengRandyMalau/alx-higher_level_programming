#!/usr/bin/node
const fs = require('fs');
// Gets the file path from the command line arguments
const filePath = process.argv[2];

// Reads the content of the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  else console.log('File content:', data);
});
