# 중고거래 & 커뮤니티 웹사이트

## 💡 프로젝트 소개
Django 기반의 중고거래 및 커뮤니티 웹사이트입니다. 사용자들이 중고 물품을 등록하고 거래할 수 있으며, 게시판을 통해 소통할 수 있는 플랫폼입니다.

## 🛠 기술 스택
- **Frontend**: HTML, CSS, JavaScript
  - Bootstrap 5
  - Axios
- **Backend**: Django
- **Database**: SQLite
- **Image Storage**: Django Media Files

## ⚙️ 주요 기능

### 1. 회원 기능
- 회원가입/로그인/로그아웃
- 프로필 관리
  - 프로필 이미지 업로드
  - 등록한 물품 목록
  - 찜한 물품 목록
- 팔로우/팔로워 시스템

### 2. 중고거래 기능
- 물품 CRUD (등록/조회/수정/삭제)
- 이미지 업로드
- 찜하기 기능
- 조회수 기능
- 해시태그 시스템
- 물품 검색
  - 제목/내용/작성자/해시태그 기반 검색
- 정렬 기능
  - 최신순/인기순

### 3. 커뮤니티 기능
- 게시글 CRUD
- 댓글 시스템
- 이미지 업로드
- 조회수 기능

## 🚀 시작하기

### 설치 방법
1. 저장소 클론
```bash
git clone [repository-url]
cd [project-name]
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

4. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

5. 서버 실행
```bash
python manage.py runserver
```

## 📁 프로젝트 구조
```
project/
├── accounts/          # 회원 관리 앱
├── products/          # 중고거래 앱
├── board/            # 게시판 앱
├── static/           # 정적 파일
├── media/            # 미디어 파일
├── templates/        # 템플릿 파일
└── config/           # 프로젝트 설정
```

## 📱 화면 구성
- 메인 페이지: 중고 물품 목록
- 회원 관리
  - 로그인/회원가입
  - 프로필 페이지
- 중고거래
  - 물품 목록/상세 페이지
  - 물품 등록/수정 페이지
- 커뮤니티
  - 게시글 목록/상세 페이지
  - 게시글 작성/수정 페이지

