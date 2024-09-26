def detect_palindrome (word):
    word = word.replace(" ", "").lower()
    word_reversed = word[::-1]
    if(word != ""):
        print(word == word_reversed)

while True:    
    print("Podaj wyraz: ")
    word = input()
    detect_palindrome(word)