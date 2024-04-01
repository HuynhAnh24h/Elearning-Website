import {app} from './app';
import mongoConnectDB from './untils/db';
require("dotenv").config();

const port = process.env.PORT
// create server
app.listen(port,()=>{
    try{
        console.log(`Sever is running with http://localhost:${port}`);
        mongoConnectDB();
    }catch{
        console.log("Sever is disconnected");
    }
});


