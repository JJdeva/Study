# 자체 시퀀스 생성
# __getitem__ 매직 메소드
# -> myobject[key]와 같은 형태 사용할 때 호출되는 메소드

# 시퀀스는 __getitem__, __len__을 모두 구현하는 개체이므로 반복이 가능하다
# -> 리스트, 튜플, 문자열은 표준 시퀀스 객체

# 시퀀스, 이터러블 객체 생성하지 않고 키로 객체의 특정 요소를 가져오는 방법

# 클래스가 표준 라이브러리 객체를 감싸는 래퍼인 경우
# 기본 객체에 가능한 많은 동작을 위임할 수 있음
class Items:
    def __init__(self, *values):
        # 리스트의 래퍼 -> 리스트의 동일한 메소드 호출하여 호환성 유지가능
        self._values = list(values)
    
    def __len__(self):
        return len(self._values)
    
    def __getitem__(self, item):
        return self._values.__getitem__(item)
    

if __name__ == "__main__":
    item = Items('a', 'b', 1, 3, 4, 5)
    print(item)
    print(type(item))
    print(len(item))
    print(item[1])
    print(item[3:])