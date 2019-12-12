"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const request = require('request');
let app = express_1.default();
const github_base_route = 'https://api.github.com/';
const app_base_route = '';
app.get('/', function (req, res) {
    request('https://api.github.com/users/defunkt', function (error, response, body) {
        console.log(body);
    });
});
app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
});
//# sourceMappingURL=index.js.map