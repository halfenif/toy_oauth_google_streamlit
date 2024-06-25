# toy_oauth_google_streamlit
![!](/doc/screen01.png)


Google oAuth2 for Dev.

## Concept
- Google oAuth를 구현한다
- FastAPI의 open-api 화면을 수정려다 말고 이것을 만들기로 한다
- Google 인증 후 id_token을 화면에 출력하는 것이 목표이다.

## Installation
**Requirements**
- Docker, Docker-Compose or Podman

### Clone
```bash
git clone https://github.com/halfenif/toy_oauth_google_streamlit.git
```

## Change Config
```bash
cp ./oauth_google_front/.env.sample ./oauth_google_front/.env
```
- GOOGLE_CLIENT_ID = "" # Your Data from Google Console
- GOOGLE_CLIENT_SECRET = "" # Your Data from Google Console
- GOOGLE_REDIRECT_URI = "http://localhost:9050"  # Your Data from Google Console, Change if you want

## Build
```bash
./buid.sh
```

## Default Port : 9050
- docker-compose.yaml
- Dockerfile
- .env
