import { ApiProperty } from "@nestjs/swagger";

export class CreateUserDto {


    @ApiProperty({ description: 'email' })
    email: string;
    @ApiProperty({ description: 'username' })
    nickname: string;
    @ApiProperty({ description: 'password' })
    pw: string;
}