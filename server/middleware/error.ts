import ErrorHandler from '../untils/ErrorHandler';
import {NextFunction, Request,Response} from 'express'

export const ErrorMiddleWare = (
    err:any, 
    req:Request, 
    res:Response, 
    next:NextFunction
)=>{
    err.statusCode = err.statusCode || 500
    err.message = err.message || "Internal Sever Error"

    // Wrong mongodb id error
    if(err.name == "CastError"){
        const message  = `Resoucre not found in valid ${err.path}`
        err = new ErrorHandler(message,400)
    }

    // Duplication key error
    if(err.code == 1100){
        const message = `Duplicate ${Object.keys(err.keyValue)} entered`
        err = new ErrorHandler(message, 400)
    }

    // wrong jwt
    if(err.name = "JsonWebTokenError"){
        const message = `JWT is Valid, try again`
        err = new ErrorHandler(message, 400)
    }

    // JWT exprired error
    if(err.name == "TokenExpiredError"){
        const message = `JWT is expired, try again`
        err = new ErrorHandler(message, 400)
    }

    res.status(err.statusCode).json({
        success: false,
        message: err.message
    })
}