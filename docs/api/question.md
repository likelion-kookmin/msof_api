# Question

질문 목록(#index), 단일 요소(#show), 추가(#new), 수정(#edit), 삭제(#destory)를 지원합니다.

## 질문 목록을 불러오기

### **Request**:

`GET` `/question/`

Parameters:

파라미터명    | 타입    | 필수 유무  | 설명
-----------|--------|----------|------------
X          | X      | X        | X

### **Response**:

```json
Content-Type application/json
200 ok

{
    "success": "true",
    "status code": 200,
    "message": "Question list feteched successfully",
    "data": [
        {
            "id": 4,
            "created_at": "2021-04-22T15:12:47.655422Z",
            "updated_at": "2021-04-22T15:12:47.655456Z",
            "deleted_at": null,
            "author_id": 1,
            "title": "aaaaa",
            "content": "sasdqivelqwe",
            "status": "P"
        },
        ...
    ]
}
```

## 질문 불러오기
### **Request**:

`GET` `/question/:id/`

Parameters:

파라미터명    | 타입    | 필수 유무  | 설명
-----------|--------|----------|------------
X          | X      | X        | X


### **Response**:

```json
Content-Type application/json
200 ok

{
    "success": "true",
    "status code": 200,
    "message": "Question feteched successfully",
    "data": {
        "id": 1,
        "created_at": "2021-05-19T09:31:12.156778Z",
        "updated_at": "2021-05-19T09:31:12.156812Z",
        "deleted_at": null,
        "author_id": 1,
        "title": "질문 제목",
        "content": "질문 내용",
        "status": "P"
    }
}
```

## 질문 추가하기
### **Request**:

`GET` `/question/:id/new/`

Headers:

|헤더명|필수 유무|설명|예시|
|-|-|-|-|
|Authorization|O| 사용자 정보를 위해 JWT 토큰이 필요합니다. `JWT`가 접두어로 와야 합니다.| JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9. ...|

Parameters:

파라미터명    | 타입    | 필수 유무  | 설명
-----------|--------|----------|------------
title      | string | O        | 질문 제목입니다.
content    | string | O        | 질문 내용입니다.(프론트가 원하는 형식 그대로 보내주세요.)


### **Response**:

```json
Content-Type application/json
201 created

{
    "success": "true",
    "status code": 201,
    "message": "Question is created successfully",
    "data": {
        "id": 12,
        "deleted_at": null,
        "author": 3,
        "title": "질문 제목입니다.",
        "content": "질문 내용입니다.",
        "status": "P"
    }
}
```

## 질문 수정하기
### **Request**:

`PUT, PATCH` `/question/:id/edit/`

Headers:

|헤더명|필수 유무|설명|예시|
|-|-|-|-|
|Authorization|O| 사용자 정보를 위해 JWT 토큰이 필요합니다. `JWT`가 접두어로 와야 합니다.| JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9. ...|

Parameters:

파라미터명    | 타입    | 필수 유무  | 설명
-----------|--------|----------|------------
title      | string | PUT: O, PATCH: X | 질문 제목입니다.
content    | string | PUT: O, PATCH: X | 질문 내용입니다.(프론트가 원하는 형식 그대로 보내주세요.)

```
! NOTE: 현재 아래와 같이 json 구조 그대로 body에 담아주어야 정상 작동합니다.

{
    "title": "수정된 질문 제목",
    "content": "수정된 질문 내용"
}
```

### **Response**:

```json
Content-Type application/json
200 ok

{
    "success": "true",
    "status code": 200,
    "message": "Question is updated successfully"
}
```

## 질문 삭제하기
### **Request**:

`DELETE` `/question/:id/destory/`

Headers:

|헤더명|필수 유무|설명|예시|
|-|-|-|-|
|Authorization|O| 사용자 정보를 위해 JWT 토큰이 필요합니다. `JWT`가 접두어로 와야 합니다.| JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9. ...|


### **Response**:

```json
Content-Type application/json
200 ok

{
    "success": "true",
    "status code": 200,
    "message": "Question is destroyed successfully"
}
```