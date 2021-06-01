# 엔트리봇 오브젝트의 파이선 코드
import Entry

a = 1
b = 0
result = 0

def when_start():
    while True:
        a = 1
        b = 0
        result = 0
        Entry.input("1부터 10까지의 숫자 입력 (0 입력시 프로그램 종료)")
        b = Entry.answer()
        if b > 10 or b < 0:
            Entry.print_for_sec("잘못된 입력", 5)
            break
        if b == 0:
            Entry.print_for_sec("프로그램 종료", 5)
            break
        while a <= b:
            result = result + a
            a += 1
        Entry.print_for_sec(("합계 " + result), 5)
