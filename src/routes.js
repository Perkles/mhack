import Router from 'express';
const routes = new Router();

// Exemplo de instanciacao de rotas 
routes.get('/', (req, res) => {
    return res.json({ message: 'hello word '});
});

export default routes;