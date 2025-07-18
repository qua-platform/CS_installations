# CS_installations - Qualibrate Setup Guide / 설치 가이드

This repository contains configuration files and setup instructions for Qualibrate experiments with quantum computing hardware.

Choose your language / 언어를 선택하세요:

<details>
<summary>🇰🇷 한국어 (Korean)</summary>

## Qualibrate 설치 가이드

Qualibrate 실험을 위한 설정 파일 및 설치 방법을 담은 저장소입니다.

## 사전 준비

### Python 버전 (필수) 
- Python 3.9.0 ~ 3.12.0 
- 참고: (2025.07.18 기준) 3.9.0 / 3.10.0 / 3.10.18 / 3.11.13 / 3.12.0 설치 및 작동 확인
> ⚠️ **중요**: Python 버전이 맞지 않으면 설치 중 오류 발생. 아래 예시는 qualibrate 이라는 이름의 가상환경 생성.
> ```bash
> python -m venv qualibrate
> or
> conda create -n qualibrate python==3.11.13
> ```

## 설치 순서

### 1. QUA 라이브러리 클론 및 설치
```bash
git clone https://github.com/qua-platform/qua-libs.git
cd qua-libs/qualibration_graphs/superconducting
pip install -e .
```

### 2. (QUAlibrate 코드를 저장할 원하는 폴더로 이동 후) 코드 클론 및 QUAlibate Config 실행
```bash
git clone https://github.com/Kyung-hoon-Jung0/CS_installations.git
cd CS_installations/KH_20250717
setup-qualibrate-config
```

### 3. QUAM Config 생성
```bash
cd quam_config
python generate_quam.py
```
정상적으로 실행되면,
- OPX wiring visulization 생성 → 유저 확인용.(확인 후 창 닫음)
- 실험별 config 파일 생성

### 4. Qualibrate 실행
```bash
qualibrate start
```
표시된 주소를 웹 브라우저로 실행 후 Node가 정상 로드되는지 확인할 것.

### 설정 관련 참고사항
- 초기 설정값(wiring, qubit frequency, resonator frequency)은 임의값으로 설정됨
- 실험 setup에 맞게 생성된 config 파일에서 수정 필요

## 라이선스
이 프로젝트는 BSD-3 Clause 라이선스를 따릅니다.

</details>

<details>
<summary>🇺🇸 English</summary>

## Qualibrate Setup Guide

This repository contains configuration files and setup instructions for Qualibrate experiments.

## Prerequisites

### Python Version (Required)
- Python 3.9.0 ~ 3.12.0
- Note: (As of 2025.07.18) Tested and confirmed working with 3.9.0 / 3.10.0 / 3.10.18 / 3.11.13 / 3.12.0
> ⚠️ **Important**: Installation errors will occur if Python version is incompatible. Please refee the following example to create a python environment.
> ```bash
> python -m venv qualibrate
> or
> conda create -n qualibrate python==3.11.13
> ```

## Installation Steps

### 1. Clone and Install QUA Libraries
```bash
git clone https://github.com/qua-platform/qua-libs.git
cd qua-libs/qualibration_graphs/superconducting
pip install -e .
```

### 2. (Move where you want to install QUAlibrate code) Clone Code and Setup QUAlibrate Config
```bash
git clone https://github.com/Kyung-hoon-Jung0/CS_installations.git
cd CS_installations/KH_20250717
setup-qualibrate-config
```

### 3. Generate QUAM Config
```bash
cd quam_config
python generate_quam.py
```
When executed successfully:
- OPX wiring visualization generated → For user verification (close window after checking)
- Experiment-specific config files generated

### 4. Start Qualibrate
```bash
qualibrate start
```
Open the displayed URL in a web browser and verify that nodes are loading correctly.

## Troubleshooting

### Configuration Notes
- Initial config values (wiring, qubit frequency, resonator frequency) are set to default values
- Modify these in the generated config files according to your experimental setup

## License
This project is licensed under the BSD-3 Clause License.
</details>