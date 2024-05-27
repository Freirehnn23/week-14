def palindromeAsik(s, b):
    s = s.lower().replace(" ", "")
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return palindromeAsik(s[1:-1], b)
    else:
        return False

input_string = input("Masukkan kalimat: ")
batas_rekursi = int(input("Masukkan batas rekursi: "))
print(palindromeAsik(input_string, batas_rekursi))

# print(palindromeAsik("#Al#p@!rO@*)A$sik*(k$is#A$O@r@$pl$!_A",37))
