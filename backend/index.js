import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import ip from "ip"
import axios from "axios"

import http, { get } from 'http';

const app = express();
const server = http.createServer(app);

const port = 3000;
app.use(cors());
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', (req, res) => {
    //console.log(get)

    axios.get('http://date.jsontest.com/')
    .then(response => {
        res.send({"time": response.data.time});
    })
    .catch(error => {
        console.log(error);
    });
})

server.listen(port, () => {
    console.log(`Le serveur écoute sur le port ${port}`);
})