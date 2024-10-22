# 저선량 CT 영상의 품질 개선을 위한 프로그램 개발
### 영상의학과 의사 선생님들이 FBP,DLA 결과를 비교한 결과를 저장해 CSV 파일로 저장해 주는 프로그램

[ Window version ]

---

**윈도우와 맥에서 모두 사용 가능합니다. 다만 운영체제에 맞는 파일이 다르니 사용하고 있는 환경에 맞게 다운 받아 사용하시면 될 것 같습니다.**

**실행 파일 위치**는 아래와 같습니다. dist, build, login.spec 폴더 및 파일은 지우시면 절대 안 됩니다!

파일의 용량이 커 클릭 후 시간이 꽤 걸릴 수 있습니다. 여러번 클릭하지 마시고 조금 기다려 주세요 :)

보안 세팅에 따라 경고 메세지가 뜨는 것을 확인 하였습니다. 무시하시고 실행 버튼 눌러주시면 됩니다!

- **Mac**
    - **CATPHAN -> login.app**
- **Window**
    - **CATPHAN -> login.exe**
    - **위의 파일이 실행되지 않을 경우 : dist -> login 또는 login.exe(노란색 아나콘다 아이콘)**

문제가 생긴다면 해당 **메일( 김영주 : kjuzoojuk@naver.com )** 로 연락 주시면 감사하겠습니다.

---

# **[ 요구사항 ]**

- background image가 tutorial, problem 각각 겹치지 않게 할 것 -> 예를 들면 tutorial image를 만들 때 함께 생성된 background는 tutorial 폴더가 아닌 problem 폴더로 -> 반영 되었습니다.
- 이름과 소속은 선택 사항 -> csv파일을 생성할 때 파일명이 겹치는 일이 발생할 수 있어 필수 사항으로 반영 되었습니다.
- tutorial은 10회씩 총 2회 수행 되도록 -> 반영 되었습니다.
- problem은 300회 진행, background, denoising(philips), fbp(siemens/philips) 각 파트별로 50개씩 -> 반영 되었습니다.
- 3점 이상을 positive로 처리할 것 - 반영 되었습니다.
- 입력값은 넣어도 되고 안 넣어도 되지만 answer는 꼭 넣어야 함 -> 비교를 위해 모두 넣었습니다.
- 결과는 csv파일로 -> 반영 되었습니다

---

# **[ 기능 ]**

- login
    - **name, affiliation을 모두 적어야 tutorial로 넘어갈 수 있습니다.**
    - 둘 중 하나라도 입력하지 않은 경우 뜨는 경고 창은 enter 키를 눌러 닫을 수 있습니다.
    - 두가지 입력사항을 모두 입력한다면 enter 창을 눌러 tutorial 로 넘어갈 수 있습니다.
- tutorial, problem
    - **점수 버튼을 누를 때 마우스를 이용해도 되고, 각 점수에 해당되는 키보드의 숫자 키(1, 2, 3, 4, 5)를 눌러 입력할 수도 있습니다.**
    - **enter 키를 누르면 버튼이 비활성화 되어 점수를 입력할 수 없습니다.** 프로그램 수행 중 자리를 이동해야 할 경우 enter 키를 눌러 버튼을 비활성화 시킨 후 이동해주시면 될 것 같습니다.
- end
    - end 버튼을 마우스로 누르거나 직접 프로그램을 종료를 눌러 창을 닫을 수 있습니다.
    - enter 키로 창을 닫을 수 없습니다.

---

# **[ 프로그램 실행 순서 ]**

1. **이름, 소속은 모두 적어야 다음 단계로 넘어갈 수 있습니다**: 결과를 csv 파일로 저장하기 위한 절차입니다.
2. **tutorial 은 각각 10회, 총 2번 진행**되며 결과를 확인할 수 있습니다:
    - 각 이미지의 좌측 상단: 수행자가 선택한 결과 (정답 여부)
3. **problem 은 총 300회 진행**됩니다.
4. **결과는 csv 형태로 result_csv 폴더 하위에 생성** 됩니다. 각 column은 다음과 같습니다.
    - Question_Path : 문제로 출제 된 이미지의 경로를 의미합니다.
    - Answer_Path : 문제로 출제 된 이미지의 정답을 의미합니다.
        1. object가 포함 된 이미지 : 빨간색 동그라미로 object의 위치가 표시되어 있습니다.
        2. object가 포함 되지 않은 이미지 : 빨간색 동그라미가 존재하지 않습니다.
    - Score : 수행자가 선택한 점수를 의미합니다.
        1. 1 : [ 1 ] Definitely Absent
        2. 2 : [ 2 ] Probably Absent
        3. 3 : [ 3 ] Indeterminate
        4. 4 : [ 4 ] Probably Present
        5. 5 : [ 5 ] Definitely Present
    - Right_Answer : 실제 정답을 의미합니다.
        1. 1 : object가 실제 존재하는 경우
        2. 0 : object가 실제 존재하지 않은 경우
    - Result : 정답 여부를 의미합니다 : 3점 이상을 Postive로 처리해 달라는 요구사항을 반영하였습니다.
        1. 1 : 정답 :  (*입력 값이 3 이상이고 실제로 object가 존재했다) 또는 (입력값이 3 미만이고 실제로 object가 존재하지 않았다*
        2. 0 : 오답
