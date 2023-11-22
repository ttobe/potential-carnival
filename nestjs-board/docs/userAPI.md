# 사용자 생성

## 엔드포인트: POST /create
설명: 제공된 데이터를 기반으로 새로운 사용자를 생성합니다.
### 파라미터:
createUserDto (요청 본문): CreateUserDto 스키마를 따르는 사용자 생성 데이터.


### 예시 요청:
```
POST /create
Content-Type: application/json

{
  "username": "예시사용자",
  "password": "예시비밀번호",
  "email": "user@example.com"
}
```


### 예시 응답:
/user/create/question로 리다이렉트되며 생성된 사용자 데이터를 반환합니다.

## 사용자 질문 폼 렌더링
### 엔드포인트: GET /create/question
설명: form-question.hbs 템플릿을 사용하여 사용자 질문 폼을 렌더링합니다.


### 예시 요청:
 `GET /create/question`

### 예시 응답:
`form-question.hbs` 템플릿을 렌더링합니다.


## 사용자 질문 제출
### 엔드포인트: POST /create/question
설명: 사용자 설문조사 데이터를 제출합니다.


파라미터:
`tmp` (요청 본문): 설문조사 폼에서 제출된 데이터.

### 예시 요청:
```http
POST /create/question
Content-Type: application/json

{
  "question1": "답변1",
  "question2": "답변2"
} 
```
### 예시 응답:
/user/login로 리다이렉트되며 제출된 설문조사 데이터를 반환합니다.


## 사용자 로그인
### 로그인 폼 렌더링
### 엔드포인트: 
`GET /login`

설명: login.hbs 템플릿을 사용하여 로그인 폼을 렌더링합니다.

### 예시 요청:

`GET /login`

### 예시 응답:
login 템플릿을 렌더링합니다.


## 사용자 로그인
### 엔드포인트: POST /login
설명: 제공된 자격 증명으로 사용자를 로그인합니다.
파라미터:
authCredentialsDto (요청 본문): AuthCredentialsDto 스키마를 따르는 사용자 인증 자격 증명.
### 예시 요청:
```http
POST /login
Content-Type: application/json

{
  "email": "예시사용자",
  "password": "예시비밀번호"
}
```
### 예시 응답:
인증 자격 증명을 기록하고 동일한 자격 증명을 반환합니다.
