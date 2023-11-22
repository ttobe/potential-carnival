import { ApiProperty } from "@nestjs/swagger";

export class AuthCredentialsDto{
    @ApiProperty({ description: 'email' })
    email:string;

    @ApiProperty({ description: 'password' })
    pw: string;
}