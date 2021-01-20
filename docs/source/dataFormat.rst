.. _dataFormat:

데이터 형식
===================================================

본 어노테이션 도구에서 사용하는 파일의 용도와 형식은 아래와 같습니다.

 * 원본 이미지 (.jpg)
 * 세그먼트 캔버스 (.svg): 세그먼트 어노테이션에 사용되는 벡터 이미지 및 작업 저장 데이터. 메타데이터 연결 폴더에 존재해야 함.
 * 세그먼테이션 데이터 (.seg): 슈퍼 픽셀 세그멘테이션 수행 결과 파일 (내부는 json 형식) 
 * 프로젝트 설정 json (.json): 대상 연결 폴더에 저장됨.
 * 어셋 작업 저장물 json (.json): 각 이미지에 해당하는 기하학 및 세그먼트 어노테이션 작업 저장 데이터. 대상 연결 폴더에 저장됨.
 * 마스크 이미지 (.png): 학습에 활용되는 마스크 이미지. 대상 연결 폴더 내에 산출됨.
 * MOAD JSON (.json): MOAD 프로젝트를 위해 정의된 최종 산출물. 기하학 어노테이션과 세그먼트 어노테이션 형식이 아래와 같이 별도로 정의됨. 대상 연결 폴더 내에 산출됨.

    * :download:`기하학 어노테이션 JSON 스키마 <./_static/jsonSchema/moad_BBPG_data_schema.json>`
    * :download:`세그먼트 어노테이션 JSON 스키마 <./_static/jsonSchema/moad_PS_data_schema.json>`

 * 이미지 메타데이터 (.json): MOAD 프로젝트에서 사용되는 이미지 별 메타데이터. 메타데이터 연결 폴더에 저장됨.

    * :download:`이미지 메타데이터 JSON 스키마 <./_static/jsonSchema/image_metadata_schema.json>`

