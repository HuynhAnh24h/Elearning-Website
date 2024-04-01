import mongoose from 'mongoose'
require('dotenv').config()

const dbUrl: string = process.env.DB_CONNECT || ""
const mongoConnectDB = async()=>{
    try{
        await mongoose.connect(dbUrl).then((data:any)=>{
            console.log("Connect DB successfull")
        })
    }catch(error:any){
        console.log(error.message);
        setTimeout(mongoConnectDB,5000)
    }
}

export default mongoConnectDB