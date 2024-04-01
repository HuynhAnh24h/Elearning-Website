import express, {NextFunction, Request,Response}from 'express';
export const app = express();
import cors from 'cors';
import cookiePaser from 'cookie-parser';
import { ErrorMiddleWare } from './middleware/error';


require("dotenv").config();


// Body Parser
app.use(express.json({limit: "50mb"}));

// Cookie Paser
app.use(cookiePaser());

// cors origin resoucre sharing API once Domain
app.use(cors({
    origin: process.env.CLIENT_DOMAIN,
}));

// Test Route
app.get('/test/api',(req:Request,res:Response,next:NextFunction)=>{
    res.status(200).json({
        success: true,
        message: "Huỳnh Anh Đang viết backend bằng express typescript"
    })
})

// Unknow Route
app.all("*",(req:Request, res:Response,next:NextFunction)=>{
    const err = new Error(`Unknow ${req.originalUrl} you have check url request`) as any;
    err.statusCode = 404;
    next(err)
})

// Check middle ware server
app.use(ErrorMiddleWare)
