def detect_palindrome (word):
    """funkcja usuwa spacje, zmniejsza litery, odwraca kolejność liter w wyrazie i porównuje z wyrazem podanym przez uzytkownika"""
    word = word.replace(" ", "").lower()
    word_reversed = word[::-1]
    if(word != ""):
        print(word == word_reversed)

help(detect_palindrome)
while True:    
    print("Podaj wyraz: ")
    word = input()
    detect_palindrome(word)