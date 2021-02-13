# DataScraping_with_Selenium_in_Ubuntu_20.04

Setting for the data scrapers in ubuntu 20.04

### 파이썬(python3) 설치

1. 파이썬 설치 여부 확인하기
- python3 -V , pip3 -V
- 버전이 화면에 표시가 없을 시, 명령어를 통해서 다운

```bash
sudo apt install python3
```

---

### 구글 크롬(google-chrome) 설치

1. 구글 크롬 설치 여부 확인하기

```bash
google-chrome --version
```

2. 없을 시, 설치를 진행합니다.

```bash
wget -P ~/Downloads/ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

- 위 명령문이 실행되지 않을 시, sudo apt-get install -f 입력

3. 설치한 deb 파일 실행

```bash
sudo dpkg -i ~/Downloads/google-chrome*.deb
```

- dpkg는 데비안 패키지 관리 시스템의 기초가 되는 소프트웨어입니다.
- deb 패키지의 설치, 삭제, 정보 제공을 위해 사용되는 명령어입니다.

↓ 출처 및 더 알아보기

[[Ubuntu] dpkg 명령어 사용법](https://miiingo.tistory.com/183)

4. "1번" 명령어를 재입력하여, 설치가 성공적으로 된 것을 확인합니다.

---

### 크롬 드라이버(chromedriver) 설치

1. 크롬 드라이버 설치 여부 확인하기

```bash
chromedriver --version
```

2. 없을 시, 설치를 진행합니다.

```bash
wget -P ~/ http://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip
```

3. zip파일의 압축을 풀어줍니다.

```bash
unzip ~/chromedriver_linux64.zip
```

4. 크롬 드라이버 파일의 위치를 조정합니다.

```bash
chmod +X ~/chromedriver                                # 크롬 드라이버를 잘라내기 합니다.
sudo mv ~/chromedriver /usr/local/share/chromedriver   # 잘라낸 크롬 드라이버를 해당 폴더로 옮깁니다.
```

5. < 이 부분을 왜 하는 지에 대해 찾아 봐야 함 >

```bash
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

6. "1번" 명령어를 재입력하여, 설치가 성공적으로 된 것을 확인합니다.

---

### pyvirtualdisplay 설치

[ponty/PyVirtualDisplay](https://github.com/ponty/pyvirtualdisplay/tree/2.0)

- selenium을 활용할 때 필요한 라이브러리입니다.
- 리눅스 환경에서 Headless 브라우저를 띄워주는 역할을 해줍니다.

    < 이 부분에 대해서 좀 더 공부가 필요함 >

```bash
sudo pip install xlrd
sudo apt-get install xvfb

sudo pip install pyvirtualdisplay
```

---

### Crontab 설정하기

- 대표적인 crontab 명령문

```bash
crontab -e # crontab 편집하기
crontab -l # crontab 목록보기
crontab -r # crontab 목록 모두 삭제하기
```

- crontab 작성법 예시

```bash
*/10 9-10 * * * cd Shine_DataBase && /usr/bin/python3 test_file_one.py > /dev/null 2>&1

0 */1 * * * sync && echo 3 > /proc/sys/vm/drop_caches

tail -f /var/log/syslog
```
