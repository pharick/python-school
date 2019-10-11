lession_count = int(input())
break_count = lession_count - 1

lessions = 45 * lession_count
even_breaks = break_count // 2 * 15
odd_breaks = (break_count - break_count // 2) * 5

result = 9 * 60 + lessions + even_breaks + odd_breaks

print(result // 60, result % 60)
