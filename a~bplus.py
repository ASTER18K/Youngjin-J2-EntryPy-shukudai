import Entry

a = 0
b = 0
result = 0

def when_start():
    a = 0
    b = 0
    result = 0
    Entry.input("첫번째 숫자를 입력하세요")
    a = Entry.answer()
    Entry.input("두번째 숫자를 입력하세요")
    b = Entry.answer()
    while a <= b:
        result = result + a
        a += 1
    Entry.print_for_sec(("합계 " + result), 5)
