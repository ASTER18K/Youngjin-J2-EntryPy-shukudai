import Entry

s = 0

def when_start():
    while True:
        Entry.input("성적입력")
        s = Entry.answer()
        if s == -1:
            Entry.print_for_sec("프로그램 종료", 3)
            break
        if s > 100 or s < 0:
            Entry.print_for_sec("다시입력", 3)
        if s >= 95 and s <= 100:
            Entry.print_for_sec("학점: A+", 3)
        if s >= 90 and s <= 94:
            Entry.print_for_sec("학점: A", 3)
        if s >= 85 and s <= 89:
            Entry.print_for_sec("학점: B+", 3)
        if s >= 80 and s <= 84:
            Entry.print_for_sec("학점: B", 3)
        if s >= 75 and s <= 79:
            Entry.print_for_sec("학점: C+", 3)
        if s >= 70 and s <= 74:
            Entry.print_for_sec("학점: C", 3)
        if s >= 65 and s <= 69:
            Entry.print_for_sec("학점: D+", 3)
        if s >= 60 and s <= 64:
            Entry.print_for_sec("학점: D", 3)
        if s >= 0 and s <= 59:
            Entry.print_for_sec("학점: F", 3)
