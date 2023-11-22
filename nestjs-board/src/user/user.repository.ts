
import { ConflictException, Injectable, NotFoundException } from "@nestjs/common";
import { User } from "./user.model";
import { CreateUserDto } from "./dto/create-user.dto";
import * as bcrypt from 'bcryptjs'
@Injectable()
export class UserRepository {
    constructor() { }
    
}