import express from "express";
let app = express();

const github_base_route = 'https://api.github.com/';
const app_base_route = '';

app.get('/', function(req, res) {
  res.send('Hello World!');
});

app.listen(3000, function() {
  console.log('Example app listening on port 3000!');
});
