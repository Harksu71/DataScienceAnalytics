# Snyk Python Vulnerable Demo

이 프로젝트는 Snyk에 Python 프로젝트를 등록하고 SCA 취약점 탐지를 확인하기 위한 데모 프로젝트입니다.
실제 서비스 배포 목적이 아니며, 의도적으로 오래된 취약 패키지 버전을 고정했습니다.

## 포함된 취약 패키지

- Django==2.2
- PyYAML==5.3.1
- urllib3==1.23

## Snyk 스캔 예시

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
snyk auth
snyk test --file=requirements.txt --package-manager=pip
snyk monitor --file=requirements.txt --package-manager=pip --project-name=snyk-python-vulnerable-demo
```

## GitHub 등록 방식

1. 이 폴더를 GitHub 저장소로 push합니다.
2. Snyk Web Console에서 **Add project > GitHub**를 선택합니다.
3. 해당 저장소를 선택합니다.
4. `requirements.txt` 기반 Python dependency scan 결과를 확인합니다.

## 주의

- 이 프로젝트는 취약점 탐지 데모용입니다.
- 외부 네트워크에 서비스하지 마십시오.
- 운영환경에 배포하지 마십시오.
