import mongoose, { Document, Model, Schema } from 'mongoose'
import bcrypt from 'bcryptjs'

// Make model user
const emailRegexPatten: RegExp = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g

export interface IUser extends Document {
    name: string
    email: string
    password: string
    avatar: {
        public_id: string
        url: string
    }
    role: string
    isVerified: boolean
    course: Array<{ courseId: string }>
    comparePassword: (password: string) => Promise<boolean>
}

const userSchema: Schema<IUser> = new mongoose.Schema({
    name: {
        type: String,
        required: [true, "Please enter your name"]
    },

    email: {
        type: String,
        required: [true, "Please enter your email"],
        validate: {
            validator: function (value: string) {
                return emailRegexPatten.test(value);
            },
            message: "please enter a valid email"
        },
        unique: true
    },

    password: {
        type: String,
        required: [true, "Please enter your password"],
        minlength: [6, "Password must be at least 6 characters"],
        select: false
    },

    avatar: {
        public_id: String,
        url: String,
    },

    role: {
        type: String,
        default: 'user'
    },

    isVerified: {
        type: Boolean
    },

    course: {
        courseId: String
    }
}, { timestamps: true })

// Hash password before Saving
userSchema.pre<IUser>('save', async function (next) {
    if (this.isModified('password')) {
        next()
    }
    this.password = await bcrypt.hash(this.password, 10)
    next()
})

// compare password
userSchema.methods.comparePassword = async function (enteredPassword: string): Promise<boolean> {
    return await bcrypt.compare(enteredPassword, this.password)
}

const userModel: Model<IUser> = mongoose.model("User", userSchema)
export default userModel