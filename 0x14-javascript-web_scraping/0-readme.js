#!/usr/bin/node
const fs = require('fs');
// Gets the file path from the command line arguments
const file_path = process.argv[2];

// Reads the content of the file
fs.readFile(file_path, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  console.log('File content:', data);
});
