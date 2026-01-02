# 📈 레버리지 ETF 교육 앱

고등학생을 위한 레버리지 ETF(KORU) 이해하기 인터랙티브 교육 자료

## 🚀 Streamlit Cloud 배포 방법

### Step 1: GitHub 저장소 생성

1. [GitHub](https://github.com)에 로그인
2. 우측 상단 `+` → `New repository` 클릭
3. 저장소 이름 입력 (예: `leverage-etf-education`)
4. `Create repository` 클릭

### Step 2: 파일 업로드

저장소에 다음 파일들을 업로드:

```
leverage-etf-education/
├── app.py              # 메인 앱 파일
└── requirements.txt    # 의존성 패키지
```

**업로드 방법:**
1. `Add file` → `Upload files` 클릭
2. `app.py`와 `requirements.txt` 드래그 앤 드롭
3. `Commit changes` 클릭

### Step 3: Streamlit Cloud 연결

1. [Streamlit Cloud](https://share.streamlit.io) 접속
2. `Sign in with GitHub` 클릭
3. `New app` 클릭
4. 설정:
   - **Repository:** `your-username/leverage-etf-education`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. `Deploy!` 클릭

### Step 4: 배포 완료! 🎉

몇 분 후 앱이 배포되면 다음과 같은 URL을 받습니다:
```
https://your-app-name.streamlit.app
```

---

## 📝 블로그 임베딩 방법

### 방법 1: iframe 사용 (권장)

```html
<iframe 
    src="https://your-app-name.streamlit.app?embedded=true"
    width="100%" 
    height="800px"
    style="border: none; border-radius: 10px;">
</iframe>
```

### 방법 2: 링크 버튼

```html
<a href="https://your-app-name.streamlit.app" 
   target="_blank"
   style="display: inline-block; padding: 15px 30px; 
          background: linear-gradient(90deg, #00d4ff, #7b2cbf);
          color: white; text-decoration: none; 
          border-radius: 10px; font-weight: bold;">
    🎮 레버리지 ETF 시뮬레이터 체험하기
</a>
```

### 티스토리 블로그

1. 글쓰기 → `HTML` 모드로 전환
2. 원하는 위치에 iframe 코드 붙여넣기
3. 발행

### 네이버 블로그

네이버는 iframe을 지원하지 않으므로:
1. 링크 버튼 방식 사용
2. 또는 스크린샷 + 링크 조합

---

## 🎨 앱 기능

| 탭 | 내용 |
|---|---|
| 📚 개념 이해 | KORU 기본 개념, 2025년 실제 결과 |
| 🎯 핵심 원리 | 복리 효과 설명, 눈덩이/게임 비유 |
| 🎛️ 직접 실험 | **인터랙티브 시뮬레이터** |
| 📊 실제 데이터 | 연간 차트, 상승장 vs 횡보장 비교 |

---

## 🔧 로컬 실행 방법

```bash
# 패키지 설치
pip install -r requirements.txt

# 앱 실행
streamlit run app.py
```

브라우저에서 `http://localhost:8501` 접속

---

## 📄 라이선스

교육 목적 자유 사용 가능