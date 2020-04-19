
# 패키지의 모듈을 사용해보겠습니다. 다음 내용을 프로젝트 폴더(C:\project) 안에 main.py 파일로 저장한 뒤 실행해보세요(main.py 파일을 mylib.graphic 패키지 폴더 안에 넣으면 안 됩니다).
#
# import 패키지.모듈
# 패키지.모듈.변수
# 패키지.모듈.함수()
# 패키지.모듈.클래스()
# main.py


# mylib.graphic 패키지의 geometry 모듈을 가져옴
import mylib.graphic.test
import mylib.graphic.geometry

# mylib.sound 패키지의 echo 모듈을 가져옴
import mylib.sound.echo

# mylib.operation 패키지의 run 모듈을 가져옴
import mylib.operation.run  # ==>run 모듈만 import

# mylib.graphic 패키지 geometry 모듈의 triangle_area 함수 사용
value = mylib.graphic.geometry.triangle_area(30, 40)
print(value)

# mylib.graphic 패키지 geometry 모듈의 rectangle_area 함수 사용
value = mylib.graphic.geometry.rectangle_area(30, 40)
print(value)

# mylib.graphic 패키지 test 모듈의 test_graphic 함수 사용
value = mylib.graphic.test.test_graphic()
print(value)

# mylib.operation 패키지 run 모듈의 render_test 함수 사용
