# news_relay
실행 시각 기준의 뉴스를 크롤링해서 인터넷편지를 발송해줍니다.

## 세팅 방법

1. `news_relay/credentials.py` 에 더캠프 아이디와 비밀번호를 입력합니다.
2. `soldier_info.py` 에 보고싶은 군인 정보를 입력합니다.

### With Docker

- `./build.sh` 로 Docker 이미지를 빌드합니다.
- `./run.sh` 로 빌드한 이미지를 실행합니다.
- 9 AM KST 에 자동으로 발송되도록 설정되어 있습니다.

### Without Docker

- `python3 execute.py` 를 실행하면 됩니다.
