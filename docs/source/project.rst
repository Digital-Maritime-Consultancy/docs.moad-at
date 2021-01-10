.. _project:

.. |icon_home| image:: _static/images/icons/home.png  
.. |icon_geometryAnno| image:: _static/images/icons/geometryAnno.png  
.. |icon_segmentAnno| image:: _static/images/icons/segmentAnno.png  
.. |icon_metadataEdit| image:: _static/images/icons/metadataEdit.png  
.. |icon_projectSetting| image:: _static/images/icons/projectSetting.png  
.. |icon_export| image:: _static/images/icons/export.png  
.. |icon_activeLearning| image:: _static/images/icons/activeLearning.png  
.. |icon_connection| image:: _static/images/icons/connection.png 
.. |icon_token| image:: _static/images/icons/token.png 

프로젝트 관리
===================================================

프로젝트 관리 방법은 프로젝트 생성과 로컬/클라우드 프로젝트를 불러오는 것이 있습니다.

새로운 프로젝트 생성에 대해서는 :ref:`프로젝트 생성<projectCreation>` 페이지를 참고해주세요.


프로젝트 불러오기
^^^^^^^^^^^^^^^^^^^^^^^
기존에 작업 및 저장된 프로젝트는 로컬 혹은 클라우드에서 불러올 수 있습니다.

프로젝트 불러오기를 위해서는 :ref:`프로젝트 파일<projectFiles>` 페이지에서 다루어진 파일들이 한 폴더에 저장되어 있어야 합니다.


최근 프로젝트 불러오기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
프로그램 초기 실행 화면의 우측 '최근 프로젝트' 탭에서 프로젝트 이름을 선택하면 가장 최근에 저장된 프로젝트를 불러옵니다.

.. figure:: _static/images/screenshots/projectLoad.png
    :align: center
    :alt: 최근 프로젝트 불러오기 화면
    
    예시: 프로젝트 이름 'moad'를 선택하여 해당 프로젝트 불러오기

프로젝트 저장
^^^^^^^^^^^^^^^^^^^^^^^

본 어노테이션 도구의 프로젝트는 매 편집의 순간 자동으로 저장됩니다.

프로젝트 중간 저장물 형식에 대해서는 :ref:`프로젝트 파일<projectFiles>` 페이지를 참조해주세요.

.. _connection:

연결 관리
^^^^^^^^^^^^^^^^^^^^^^^^^^^

프로젝트의 연결은 주 메뉴의 |icon_connection| 버튼을 눌러 편집할 수 있습니다.

.. figure:: _static/images/screenshots/connectionSetting.png
    :align: center
    :alt: 연결 설정 화면

상기의 예시 화면은 연결로써 로컬 파일 시스템의 폴더와 연결하는 방법을 보여줍니다. 먼저 프로젝트 이름에서 연결명을 설정하고 공급자를 '로컬 파일 시스템'으로 선택합니다. 

로컬 파일 시스템 선택 시 하위에 폴더 경로를 선택할 수 있는 입력 창 및 '폴더 선택' 버튼이 나타납니다. '폴더 선택' 버튼 클릭 시 나타나는 창에서 폴더를 특정한 후 '저장' 버튼을 눌러 연결을 저장합니다.

.. _mainMenu:

주 메뉴 설명
^^^^^^^^^^^^^^^^^^^^^^^
본 어노테이션 도구의 좌측에는 주 메뉴가 위치하고 있으며 각각 아래의 기능과 연결되어 있습니다.

* |icon_home|: 초기 화면
* |icon_geometryAnno|: :ref:`다각형 어노테이션 편집<geometryAnnotation>`
* |icon_segmentAnno|: :ref:`세그먼트 어노테이션 편집<segmentAnnotation>`
* |icon_metadataEdit|: :ref:`메타데이터 편집<imageMetadata>`
* |icon_projectSetting|: 프로젝트 속성
* |icon_export|: :ref:`어노테이션 결과 산출 관리<export>`
* |icon_activeLearning|: 인공지능 모델 속성
* |icon_connection|: :ref:`연결 관리<connection>`
* |icon_token|: 토큰 관리
