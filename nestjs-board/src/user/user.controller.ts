import { Body, Controller, Get, Param, Post, Redirect, Render, Res, UsePipes, ValidationPipe } from '@nestjs/common';
import { UserService } from './user.service';
import { User } from './user.model';
import { Response } from 'express';
import { CreateUserDto } from './dto/create-user.dto';
import { AuthCredentialsDto } from './dto/auth-credtial.dto';
import { ApiCreatedResponse, ApiOperation, ApiTags } from '@nestjs/swagger';

@Controller('user')
@ApiTags('유저 API')
export class UserController {
    constructor(private userService: UserService) { }

    @Get('/create')
    @ApiOperation({ summary: '유저 생성 페이지', description: '유저를 생성한다.' })
    @ApiCreatedResponse({ description: '회원가입 페이지 form.html 불러오기' })
    @Render('form.hbs')
    renderForm() { }

    @Post('/create')
    @ApiOperation({ summary: '유저 생성 API', description: '유저를 생성한다.' })
    @ApiCreatedResponse({ description: '회원가입', type: CreateUserDto })
    @UsePipes(ValidationPipe)
    createUser(
        @Body() createUserDto: CreateUserDto,
        @Res() res: Response
    ) {
        res.redirect("/user/create/question")
        return createUserDto;
    }

    @Get("/create/question")
    @Render('form-question.hbs')
    @ApiOperation({ summary: '유저 질문 페이지', description: '질문을 받는다.' })
    @ApiCreatedResponse({ description: '질문 페이지 form-question.html 불러오기' })
    question() { }

    @Post('/create/question')
    @UsePipes(ValidationPipe)
    @ApiOperation({ summary: '유저 질문 API', description: '질문을 생성한다.' })
    @ApiCreatedResponse({ description: '질문을 받아서 제출한다' })
    createUserQuestion(
        @Body() tmp: any,
        @Res() res: Response
    ) {
        res.redirect("/user/login")
        return tmp;
    }

    @Get('/login')
    @Render('login.hbs')
    @ApiOperation({ summary: '로그인 페이지', description: '로그인.' })
    @ApiCreatedResponse({ description: '로그인 페이지 login.html 불러오기' })
    renderLogin() { }

    @Post('/login')
    @ApiOperation({ summary: '로그인 API', description: '로그인 요청.' })
    @ApiCreatedResponse({ description: '로그인 요청 후 map으로 redirect', type: AuthCredentialsDto})
    async login(
        @Body() authCredentialsDto: AuthCredentialsDto,
        @Res() res: Response
    ) {
        console.log(authCredentialsDto)
        return authCredentialsDto;
    }
}
