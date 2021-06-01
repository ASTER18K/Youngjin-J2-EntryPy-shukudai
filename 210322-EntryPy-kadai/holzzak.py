import Entry

a = 0

def when_start():
    while True:
        Entry.input("0을 제외한 숫자를 입력하세요")
        a = Entry.answer()
        if a == 0:
            Entry.print_for_sec("프로그램 종료", 3)
            break
        if a % 2 == 0:
            Entry.print_for_sec("짝수입니다", 3)
        else:
            Entry.print_for_sec("홀수입니다", 3)
