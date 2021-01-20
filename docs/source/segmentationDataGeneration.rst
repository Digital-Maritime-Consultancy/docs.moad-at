.. _segmentationDataGeneration:

세그멘테이션 데이터 생성
==============================

본 어노테이션 도구의 '세그먼트 어노테이션 편집'을 수행하기 위해선 각 이미지의 세그멘테이션 데이터가 필요합니다.

어노테이션 도구 버전 |version| 에선 세그멘테이션 데이터 생성 기능이 제공되지 않기 때문에 아래의 파이썬 스크립트를 사전에 수행하여 생성해두셔야 합니다.


**파이썬 스크립트 링크**:

https://github.com/Digital-Maritime-Consultancy/docs.moad-at/blob/master/docs/source/_static/codes/exportSegmentation.py

**실행 요구사항**:

* 파이썬 버전 3.7 이상
* scikit-image 0.17.2 이상 설치

스크립트 수행 전 이미지들을 한 폴더 안에 준비해 놓습니다. 본 예제에선 'images' 폴더를 사용합니다.

스크립트 수행 방식은 스크립트 코드 내에서 아래의 함수를 실행하는 것이며 각 파라미터는 다음과 같습니다: 이미지 폴더, 산출 폴더, 산출 해상도 너비, 산출 해상도 높이::

    convert('./images', './', 1024, 768)

해당 스크립트는 아래와 같이 터미널에서도 수행하실 수 있습니다. 파라미터의 순서와 의미는 상기와 동일합니다::

    python exportSegmentation.py ./images ./ 1024 768

산출물로 이미지 파일과 동일한 수의 .seg 파일들이 지정된 산출 폴더에 생성될 것입니다.

모든 .seg 파일들은 프로젝트의 Metadata connection에서 지정하는 폴더 내에 위치시킵니다.
