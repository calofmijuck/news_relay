# news_relay
실행 시각 기준의 뉴스를 크롤링해서 인터넷편지를 발송해줍니다.

## 세팅 방법

1. `news_relay/credentials.py` 에 더캠프 아이디와 비밀번호를 입력합니다.
2. `soldier_info.py` 에 보고싶은 군인 정보를 입력합니다.

## With Docker

### 직접 빌드

- `./build.sh` 로 Docker 이미지를 빌드합니다.
- `./run.sh` 로 빌드한 이미지를 실행합니다.
- 9 AM KST 에 자동으로 발송되도록 설정되어 있습니다.

### Pull image from Docker Hub

- `docker pull calofmijuck/news_relay`
- `sha256:3ac0cfc59b250853ae4d63eb915b090ad97814a4867e0d7111204ce001910cbc`
- 세팅 방법의 1, 2 를 하면 됩니다.

## Without Docker

- `python3 execute.py` 를 실행하면 됩니다.

## TODO

### 세팅 방법 더욱 간편화 하기

- 군인 정보를 입력하고 Docker 를 빌드하는 것은 불편하다.
  - Environment variable 로 넣어서 `docker run` 해버리면 되지 않을까?
