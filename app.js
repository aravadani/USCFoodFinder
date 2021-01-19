// Imports
const express = require('express');
const app = express();

// Constants
const PORT = process.env.PORT || 4000

// Default Get 
app.get('/', (req, res) => {
  res.send(`<title>USC Food Finder</title><h1>USC Food Finder running w/ NodeJS & ExpressJS on port ${PORT}</h1>`);
})

// Server Listen
const server = app.listen(PORT, () => {
  console.log(`Server running at port ${server.address().port}`);
});
