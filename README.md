# 🎢 경기침체와 여가활동 변화 분석 프로젝트 (SQL + Python)

> 경기 침체가 여가활동에 어떤 영향을 미치는지 SQL과 Python을 활용해 분석한 프로젝트입니다.

---

## 📁 폴더 구조

leisure_economy_project/ │ ├── data/ # 데이터 폴더 │ ├── active_economy_data.csv │ ├── inactive_economy_data.csv │ ├── employment_data.csv │ ├── unemployment_data.csv │ ├── economy.csv │ ├── economy_population.csv │ ├── income_impacts.csv │ ├── interest_rate.csv │ ├── hotspring_data.csv │ ├── park_fixed.csv │ ├── ski_fixed.csv │ ├── tour_fixed.csv │ ├── leisure_tour_김영혜.sql # SQL 테이블 생성 및 데이터 삽입 쿼리 ├── outdoor_activity.ipynb # Python 분석 메인 노트북 ├── test.py # Python 테스트용 스크립트 └── README.md

---

## 💡 분석 목표

- **가설**: 경기침체 시 필수소비가 아닌 여가활동 지출이 줄어들 것이다.
- **분석 방향**: SQL로 데이터베이스를 구성하고, Python으로 연동해 **경제지표와 여가활동 지표의 상관관계** 분석 및 시각화.

---

## 🗃️ SQL 테이블 및 데이터 구성

- `leisure_tour_김영혜.sql` 실행하여 MySQL에 테이블 및 데이터 삽입  
- 관계형 DB 기반 테이블 설계: `economic_summary`, `park_fixed`, `tour_fixed`, `ski_fixed`, `hotspring_data` 등  
- 연도(`year`) 기준으로 연결된 외래키 기반 설계

> 💻 실행 환경: MySQL (DBeaver 추천)

---

## 👩‍💻 Python 분석 실행

```bash
pip install pandas matplotlib seaborn pymysql koreanize-matplotlib
```
- outdoor_activity.ipynb 실행
- SQL → Python 연동 후 데이터프레임 생성 및 시각화
- matplotlib + seaborn 기반 다양한 그래프 구성

---

## 💬 프로젝트 회고

- ✅ PM 역할 수행: 타임라인 관리, 역할 분담, DB/분석 설계 총괄
- ✅ SQL → Python 연동 기반 실무 흐름 체험
- ✅ 가설 기반 분석 설계 및 시각화 중심 인사이트 도출 시도
- 🔧 PPT 구성 통일, 발표자료의 디자인 개선 등 발표 측면에서 개선 포인트 도출

---

## 👩‍💻 제작자

- **이름:** Emily  
- **역할:** PM / DB 설계 / SQL 구축 / Python 시각화 / 분석 및 발표

---

## 🔗 프로젝트 링크

🧾 [프로젝트 상세 노션 페이지](https://yeonghyekim.notion.site/19de2859370c80968a9ed627d2a7617d?pvs=4)  