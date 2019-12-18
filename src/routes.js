import Router from 'express';
const routes = new Router();

import UserController from './app/controller/UserController';

routes.post('/users', UserController.store);

// Exemplo de instanciacao de rotas 
// routes.get('/', (req, res) => {
//     return res.json({ message: 'hello word '});
// });

export default routes;