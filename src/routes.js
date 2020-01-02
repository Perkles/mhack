import Router from 'express';
const path = require('path');
const request = require('request');

const routes = new Router();

// import UserController from './app/controller/UserController';

// routes.post('/users', UserController.store);


routes.get('/', (req, res) => {
    res.sendFile(path.join(__dirname+'/index.html'));
});

routes.get('/profile', (req, res) => {
    // Check if a user already has a profile if not create one
    
    res.sendFile(path.join(__dirname+'/index.html'));
});

routes.get('/users/signin/callback', (req, res) => {
    const code = req.query.code;
    console.log(code);

    // request.js post request npm run dev
    const options = {
        url: 'https://github.com/login/oauth/access_token',
        json: true,
        body: {
            client_id: 'dc885fbf11d3232616bc',
            client_secret: 'a9d70f98b5bd165cbe45f9b767a9869e25792587',
            code: code
        }
    };
    
    request.post(options, (err, res, body) => {
        if (err) {
            return console.log(err);
        }
        console.log(`Status: ${res.statusCode}`);
        console.log(body);
    });

});

export default routes;