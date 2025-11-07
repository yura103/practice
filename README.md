
# 제 13회 2025 AI·데이터 경진대회 | 빅데이터 콘테스트

## **프로젝트: 우리 동네 가맹점, 위기 신호를 미리 잡아라!**

### [📑 PPT](https://drive.google.com/drive/folders/1jaDh55LWAPJujv6u-DLDoSJ272of5uh4?usp=sharing) | [보고서](https://drive.google.com/file/d/1_OR-3VCOVa8mbY9fBRuCy_6IzK4U3knx/view?usp=drive_link) | [Figma](https://www.figma.com/make/tQnBekMXRiWVxQO6LbhUz7/Franchisee-Support-Web-App?node-id=0-1&p=f&fullscreen=1)

---

## **1. 프로젝트 개요**

### **1.1. 배경 및 목표**

소상공인, 특히 프랜차이즈 가맹점은 지역 경제의 중요한 축을 담당하지만, 경기 변동, 경쟁 심화 등 다양한 외부 요인으로 인해 항상 위기에 노출되어 있습니다. 가맹점의 갑작스러운 폐업이나 매출 급락은 가맹점주 개인의 경제적 어려움을 넘어, 지역 사회와 프랜차이즈 본사에도 큰 영향을 미칩니다.

본 프로젝트는 가맹점의 운영 데이터를 심층적으로 분석하여, **폐업이나 매출 급락과 같은 위기 징후를 사전에 예측하고 경보하는 시스템을 구축**하는 것을 최종 목표로 합니다. 데이터 기반의 예측 모델을 통해 가맹점의 잠재적 위험을 조기에 발견하고, 가맹점주와 프랜차이즈 본사가 선제적으로 대응할 수 있는 과학적 근거를 제공하고자 합니다.

### **1.2. 기대 효과**

- **가맹점주**: 자신의 가맹점이 처한 위험 수준을 객관적으로 파악하고, 컨설팅, 마케팅 강화 등 위기 극복을 위한 조치를 적시에 취할 수 있습니다.
- **프랜차이즈 본사**: 부실 위험이 높은 가맹점을 조기에 식별하여 맞춤형 지원 프로그램을 제공하고, 브랜드 가치를 안정적으로 관리할 수 있습니다.
- **금융 기관**: 가맹점 대상 대출 심사 시, 데이터 기반의 신용 평가 모델로 활용하여 리스크를 정교하게 관리할 수 있습니다.

---

## **2. 데이터 소개**

### **2.1. 데이터 출처 및 구성**

본 분석에는 대회에서 제공된 3개의 주요 데이터셋과 추가적인 거시 경제지표 데이터가 사용되었습니다. 각 데이터는 가맹점의 기본 정보, 월별 매출 정보, 고객 정보 등을 포함하고 있으며, '가맹점구분번호'와 '기준년월'을 기준으로 통합하여 시계열 분석을 수행했습니다.

### **2.2. 외부데이터**
- **출처**: [서울열린데이터광장 - 서울시 고용지표 통계](https://data.seoul.go.kr/dataList/59/S/2/datasetView.do)
- **칼럼**: 경제활동참가율, 실업률, 고용률

---

## **3. 탐색적 데이터 분석 (EDA)**

데이터에 대한 깊은 이해를 바탕으로 효과적인 특성(Feature)을 생성하고 모델링 전략을 수립하기 위해, `1_eda.ipynb`에서 다각적인 EDA를 수행했습니다.

### **3.1. 기타 시각화**
| ![시각화1](https://drive.google.com/uc?export=view&id=188rD8Kya6-lhkLfHfJV0YEW52sGS_bpl) | ![시각화2](https://drive.google.com/uc?export=view&id=10254V0xNUGDOQ-aWmHhBARvaqREFBfnI) |
| :---: | :---: |
| ![시각화3](https://drive.google.com/uc?export=view&id=1q15QJjm8wsOd5rb1whoZAJX8apMYnLDu) | ![시각화4](https://drive.google.com/uc?export=view&id=1Ujodb7tE0sBNLOXT54BillY1y8vMwruf) |
| ![시각화5](https://drive.google.com/uc?export=view&id=1pDD3G9_VUSA1XsG-xFk1n72MLoRZC2Vf) | ![시각화6](https://drive.google.com/uc?export=view&id=13dqcBfllvOVWkniy-LQfJwGbOzVsOCZ5) |
| ![시각화7](https://drive.google.com/uc?export=view&id=1a3jfd5QzYp-QgLbHBVc17LiUHay5_eBB) | ![시각화8](https://drive.google.com/uc?export=view&id=1aUsq55GKYKzNC45-F0T45E1sgm3itkoJ) |



### **3.2. 변수 간 관계 탐색**
| ![상관관계1](https://drive.google.com/uc?export=view&id=1HHodj6iFTif4Bkdcdw-sJbtCunfQYF9E) | ![상관관계2](https://drive.google.com/uc?export=view&id=1D7qgx9OOHachf3Z1OcEj3xXEol-JtjNZ) |
| :---: | :---: |


### **3.3. 가설검증**
| ![가설1](https://drive.google.com/uc?export=view&id=1iYbz-pjhvzJJ4fKnEaJwmXm-0X2LahFk) | ![가설2](https://drive.google.com/uc?export=view&id=1hoayVjf0VO0rD1b1b-HhTLCfJ3734pQ6) |
| :---: | :---: |
| ![가설3](https://drive.google.com/uc?export=view&id=1fNxnc1a82ppZ-RpaPr9fritD1xmkxBNr) | ![가설4](https://drive.google.com/uc?export=view&id=1IadVn0x99AbwSLdkJG_oGgchUX_9yl_g) |
| ![가설5](https://drive.google.com/uc?export=view&id=1jHZIdi_fI_iJ_Wd-R6s9mt6zmv4TZqsm) | ![가설6](https://drive.google.com/uc?export=view&id=1xWDVKRdZPuX2ITf1yYvn6F3v-v3NaUVf) |
| ![가설7](https://drive.google.com/uc?export=view&id=1fBtquxSkuAsIKSbGPCKm69iK4vRvAXKw) | ![가설8](https://drive.google.com/uc?export=view&id=19BSQz5Qu7avaNrfLwhrrtR3nYeyE-zE5) |
| ![가설9](https://drive.google.com/uc?export=view&id=11-9KoFzxSz7tgsLQlpoS2ny1k-A6s9d-) | ![가설10](https://drive.google.com/uc?export=view&id=1Du7sU6e-SmXmO89NmBC8C9Y2GpvZ0VN1) |
| ![가설11](https://drive.google.com/uc?export=view&id=1HN-CpNTimDVOPJNVd3o83Zegc760rnnZ) | ![가설12](https://drive.google.com/uc?export=view&id=1Tm_XdYlRUDL0sSO0n6WT8MrTkwBPdUlu) |

---

## **4. 모델링**

가맹점의 위기 신호를 예측하는 모델을 개발했습니다.

### **4.1. 특성 공학 (Feature Engineering)**

모델의 예측 성능을 극대화하기 위해, 원본 데이터를 가공하여 의미 있는 새로운 변수들을 생성했습니다.

- **위험 지표 정의 (`Target_Final`)**: 가맹점의 위기 상황을 종합적으로 판단하기 위해 다음과 같은 세부적인 위험 지표들을 정의하고, 이 중 하나라도 해당될 경우 최종 위험 신호(`Target_Final=1`)로 간주했습니다.
    1.  **`Target_폐업`**: 특정 시점으로부터 1년 이내에 폐업한 경우
    2.  **`Target_매출급락`**: 최근 6개월간의 매출 중앙값 대비 50% 이상 하락한 경우
    3.  **`Target_낮은매출`**: 최근 6개월간의 매출 구간 점수가 지속적으로 최하위(1, 2등급)에 머무른 경우

- **동적/정적 변수 생성**: 시간에 따라 변하는 **동적 변수**와 변하지 않는 **정적 변수**를 구분하여 모델링에 활용했습니다.
    - **동적 변수**: 매출/고객 관련 지표들의 최근 6개월 추세(기울기), 변동성(변화량 평균), 최신 값 등을 롤링(Rolling) 기법으로 생성
    - **정적 변수**: 업종, 상권, 최초 개설일 등 가맹점의 고유한 정보

### **4.2. 생존 분석 (Survival Analysis)**

가맹점의 '생존'(운영)과 '사망'(폐업)이라는 사건 발생까지의 시간을 분석하기 위해 생존 분석 기법을 적용했습니다. 이 방법론은 단순히 폐업 여부(0/1)를 예측하는 것을 넘어, **시간의 흐름에 따른 폐업 확률**을 분석할 수 있게 해줍니다.

- **Kaplan-Meier 생존 곡선**: 시간에 따른 가맹점의 누적 생존율을 시각적으로 보여줍니다. 이를 통해 특정 기간 내에 가맹점이 얼마나 살아남는지를 직관적으로 파악할 수 있습니다.

![생존곡선](https://drive.google.com/uc?export=view&id=1Ggo8d1zygGf2OdRvHcA6dx_2VNO2TDpK)

- **Cox 비례위험 모델**: 여러 변수들이 가맹점의 생존(폐업)에 미치는 영향을 분석하는 모델입니다. 각 변수의 위험 비율(Hazard Ratio)을 통해, 특정 변수가 폐업 위험을 얼마나 높이거나 낮추는지를 정량적으로 해석할 수 있습니다.

### **4.3. 위기 예측 모델링**

- **모델 선택 (PyCaret)**: `PyCaret` 라이브러리를 활용하여 Logistic Regression, LightGBM, RandomForest 등 10여개의 다양한 분류 모델의 성능을 신속하게 비교 평가했습니다. AUC, Accuracy, F1-Score 등 종합적인 평가지표를 고려하여 최종 모델을 선정했습니다.

![모델 선정](https://drive.google.com/uc?export=view&id=1GCYNMLBECJ9J6YQ4dQt6AaGin_EADDJD)


- **최종 모델: RandomForest**: 비교 평가 결과, 개별 의사결정나무(Decision Tree)들을 결합하여 예측 안정성과 정확도를 높인 앙상블 모델인 **RandomForest**가 가장 우수한 성능을 보여 최종 모델로 선정했습니다. RandomForest는 과적합(Overfitting)에 강하고, 변수 중요도를 제공하여 모델 해석이 용이하다는 장점이 있습니다.

---

## **5. 모델 해석 및 결과**

### **5.1. 특성 중요도 (Feature Importance)**

학습된 RandomForest 모델이 어떤 변수를 중요하게 보고 위기 신호를 예측했는지 분석했습니다. 특성 중요도 분석 결과, 다음과 같은 변수들이 가맹점 위기 예측에 큰 영향을 미치는 것으로 나타났습니다.

- **상위 중요 변수**: `동일 업종 내 매출 순위 비율`, `총운영일`, `매출금액 구간 점수` 등

![특성중요도](https://drive.google.com/uc?export=view&id=1JgyEFgnv0hUnDukoGEmDjOMaYMBpIwzw)

### **5.2. 모델 성능 평가**

- **혼동 행렬 (Confusion Matrix)**: 모델의 예측 결과를 실제 값과 비교하여, 모델이 얼마나 정확하게 위기(True Positive)와 정상(True Negative) 상태를 예측했는지 평가했습니다. 이를 통해 모델의 정밀도(Precision)와 재현율(Recall)을 파악할 수 있습니다.

| KNN 혼동 행렬 | ET 혼동 행렬 |
| :---: | :---: |
| ![KNN 혼동 행렬](https://drive.google.com/uc?export=view&id=1TYK1wjT_UEnfZKf-vN4TaH000l72D45L) | ![ET 혼동 행렬](https://drive.google.com/uc?export=view&id=1EDHD0WAyKgRelmG5XaXvSCYrYCIXPPmm) |

- **기타 평가지표**: AUC(Area Under the Curve), F1-Score 등을 통해 모델의 전반적인 성능을 종합적으로 평가했습니다.


---

## **6. 모델 활용 방안**

### **6.1. 위기 경보 대시보드 구축**

개발된 예측 모델을 기반으로, 각 가맹점의 현재 위험도를 실시간으로 모니터링할 수 있는 대시보드를 구축할 수 있습니다. 가맹점주와 본사 담당자는 이 대시보드를 통해 위험도 상위 가맹점 목록, 주요 위험 요인, 과거 위험도 변화 추이 등을 한눈에 파악하고 신속하게 대응할 수 있습니다.

![피그마1](https://drive.google.com/uc?export=view&id=1kjWaJSCEG8rBkOyWXsZ6ggqQRtzCDbIa)
![피그마2](https://drive.google.com/uc?export=view&id=1WcD3a4DFVNjcMlw1nO9Nz-QZN2CZX5Bx)
![피그마3](https://drive.google.com/uc?export=view&id=1mQYDz0wpyEgvX4T8IaOji1fsmlf2RMuC)

### **6.2. 가맹점 맞춤형 컨설팅 지원**

모델이 제시하는 주요 위험 요인을 바탕으로 가맹점별 맞춤형 컨설팅을 제공할 수 있습니다. 예를 들어, '재방문 고객 비중'이 주요 위험 요인으로 나타난 가맹점에는 고객 충성도 프로그램을, '동일 상권 내 매출 순위'가 문제인 가맹점에는 지역 타겟 마케팅 전략을 제안하는 등 데이터 기반의 구체적인 해결책을 제시할 수 있습니다.

---

## **7. 결론**

본 프로젝트를 통해 가맹점의 다양한 운영 데이터를 활용하여 위기 신호를 예측하는 모델을 성공적으로 개발했습니다. RandomForest 모델과 생존 분석을 결합하여, 단순히 위기 발생 여부를 예측하는 것을 넘어 위기에 영향을 미치는 주요 요인과 시간의 흐름에 따른 위험도를 종합적으로 분석할 수 있었습니다. 이 모델은 가맹점의 안정적인 운영을 지원하고 프랜차이즈 산업의 건전한 발전에 기여할 수 있는 실질적인 도구가 될 잠재력을 가지고 있습니다.


## Team & Roles

| 이름   | 역할 |
|--------|------------------------------------------------|
| 김성현 | 피처 엔지니어링 및 모델링 |
| 김유라 | 전처리 및 EDA |
| 김초아 | 피처 생성 및 모델링 |
| 박진서 | 전처리 및 EDA |
