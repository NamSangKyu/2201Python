def get_average(marks):
    total = 0
    for key in marks:
        total += marks[key]
    return total / len(marks)

marks = {'국어':90,'영어':80,'수학':85}
average = get_average(marks)
print(f'평균은 {average}점 입니다.')