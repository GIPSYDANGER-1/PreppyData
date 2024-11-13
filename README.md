# PREPPYDATA
<p align="center">
  <a href="README.md">🇬🇧English</a> |
  <a href="README.ko.md">🇰🇷한국어</a> |
  <a href="README.ja.md">🇯🇵日本語</a> |
  <a href="README.zh.md">🇨🇳中文</a> |
  <a href="README.de.md">🇩🇪Deutsch</a> |
  <a href="README.fr.md">🇫🇷Français</a> |
  <a href="README.ep.md">🇪🇸Español</a>
</p>

# PreppyData
> We provide Data Preprocessing for everybody

## 🔍 Background & Problem Statement

현재 데이터 전처리 서비스들은 자동화된 방식이나 미리 정의된 방법들을 제공하고 있습니다. 하지만 이러한 도구들은 다음과 같은 한계점을 가지고 있습니다:

### 현재 데이터 전처리 서비스의 한계

1. **제한된 커스터마이징** 
   - 데이터 인코딩 방식 선택의 제한
   - 이상치 탐지 기법 선택의 제한
   - 특성 선택 전략의 제한된 옵션

2. **일반화된 접근 방식**
   - 모든 데이터셋에 동일한 방식 적용
   - 도메인 특성을 고려하지 않는 획일화된 처리

3. **사용자 통제력 부족**
   - 전처리 방법 적용 과정의 제한된 제어
   - 데이터 변환 과정의 낮은 투명성
   - 처리 과정에 대한 이해도 저하

## 💡 Our Solution

1. **선택 가능한 전처리 방법**
 - 인코딩 방식의 다양성(원-핫 인코딩, 레이블 인코딩) 
 - 이상치 탐지 방법의 다양성(Z-score, IQR, LOF)
 - 기능 선택 접근 방식의 다양성 (상관 관계 기반, LASSO)

2. **사용자 친화적인 인터페이스**
 - 사용자가 쉽게 데이터를 업로드하고, 원하는 옵션을 선태하고, 적용되는 변환에 대한 피드백을 받을 수 있는 플랫폼

3. **높은 투명성과 통제력**
 - 사용자가 사전 처리 단계를 이해하고 프로세스 중 조정 시 유연성을 제공하는 시스템입ㄴ

## ⭐ Features
### Core Features
 - [사용자 정의 전처리 옵션]: 사용자가 다양한 데이터 전처리 기술을 선택할 수 있습니다.
 - [사용자 친화적 인터페이스]: 사용자가 쉽게 데이터 세트를 업로드하고 사용 가능한 전처리 옵션을 탐색할 수 있는 간단한 웹 기반 플랫폼입니다.
 - [단계별 안내]: 사용자가 전처리 프로세스를 단계별로 이해하고 조정할 수 있도록 도와주는 안내 기능입니다.
 - [데이터 품질 평가]: 사용자가 전처리 전과 후에 데이터 세트의 품질을 평가하여 문제를 효과적으로 식별하고 해결하는 데 도움이 되는 기능입니다.

## 🎯 Goals & Target Users
### Our Goals
 - 이 프로젝트는 사용자가 지정 가능한 데이터 전처리 데이터를 제공하는 것을 목표로 합니다. 사용자가 데이터 준비를 개인화할 수 있도록 함으로 데이터 품질을 향상시키고 분석 및 머신 러닝에 더 쉽게 접근할 수 있도록 합니다.

### Target Users
 - 데이터 전처리에 대한 이해가 부족한 사용자
 - 데이터 전처리 프로세스를 사용자화하고 데이터 품질을 향상시키고 분석 및 머신 러닝에 더 쉽게 접근하고 싶은 사용자

## 📖 How to Use
 - csv 또는 xlsx 파일을 업로드 합니다.
 - 데이터 인코딩, 이상치 감지, 결측치 처리를 포함한 옵션 목록에서 특정 전처리 기술을 선택합니다. (미선택시 자동 적용)
 - 추가 분석을 위해 처리된 데이터를 원하는 형식으로 다운로드 합니다.


