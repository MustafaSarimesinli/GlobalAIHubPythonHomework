import random
from word_list import animal_list,plants_list

man = ["""
   +---+
   |   |
       |
       |
       |
       |
   --------""","""
   +---+
   |   |
   O   |
       |
       |
       |
   --------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
   --------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
   --------""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
   --------""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
   --------""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
   --------"""]

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "Hangman Game" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~")

sys_user = input("Please enter your user name: ").upper()
print("""
                                  01010101010101
                                   1	      01
                                   1          10
                                  0 0         01
                                 0   0        10
                                 0   0        01
                                  000         10
                                   0          01
                                  000         10
                                 0 0 0        01 
                                0  0  0       10
                               0   0   0      01
                                   0          10
                                  000         01
                                 0   0        10
                                0     0       01
                               0       0      10
                                              01
                                    010101010101010101
""")
print("\t\t\t\t\t\t\tW E L C O M E","  ", *sys_user,sep=" ")
print("\n")

def get_word():
    while True:
        print("""
        Categorys:(Kelimeler Türkçe seçilmiştir...)\n
        Transaction Numbers:
        1 - Animals
        2 - Fruits and Vegetables
        """)
        category = int(input("Choose a category (1 or 2): "))
        if category == 1:
            word = random.choice(animal_list)
            return word.replace("i","İ").upper()

        elif category == 2:
            word = random.choice(plants_list)
            return word.replace("i","İ").upper()

        else:
            print("Invalid Category... Please select one of the existing categories.\n")

def play(word):
    word_display = "_" * len(word)
    guessed = False
    step = 0
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("----------------------------------- L E T ' S    S T A R T -----------------------------------")
    print(man[step],"\n")
    print("The word has {} letters...".format(len(word)))
    print(word_display)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Enter your guess: ").replace("i","İ").upper()
# tahmin True veya deneme hakkı bittiğinde bu döngü sonlanacaktır.
        if len(guess) == 1 and guess.isalpha():
        # eğer tahmin uzunluğu 1 ise bu harf demektir ve harf olduğunu isalpha metodu ile kontrol ediyoruz.
            if guess in guessed_letters:
                print("You have entered the letter %s before..." %(guess))
            elif guess not in word:
                tries -= 1
                step += 1
                print(man[step], "\n")
                print("The letter %s does not exist in the word." %(guess))
                print("You have %d rights left" %(tries))
                guessed_letters.append(guess)
            else:
                print(man[step],"\n")
                print("You're Super... The letter %s is present in the word..." %(guess))
                guessed_letters.append(guess)
                word_array = list(word_display)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_array[index] = guess
                word_display = "".join(word_array)
                if "_" not in word_display:
                    guessed = True
                # Ö N E M L İ
# kelimeyi harflere parçalayarak eğer harf ile tahmin tutuyor ise i diyerek endeksi döndürüyoruz..
# eğer o harften, kelime içerisinde birden fazla var ise onlara kontrol edecek...
# daha sonra index değerleri üzerinden "_" değerini tahimin değeri ile değiştirecek..
# kelimeleri parçaladığımız için de tekrardan boşluk olamayacak şekilde join işlemi yapıyoruz.


        elif len(guess) == len(word) and guess.isalpha():
        # eğer tahmin uzunluğu kelime uzunluğu ile aynı boyda ise bunu kelime olarak algılayacaktır.
            if guess == word:
                guessed = True
                word_display = word
            elif guess in guessed_words:
                print("%s tried this word before..." %(guess))
            else:
                step += 1
                print(man[step],"\n")
                print("Wrong Answer...")
                print("You have %d rights left" % (tries))
                guessed_words.append(guess)
                tries -= 1

        else:
            print("Invalid Guessed....")
        print(word_display)
        print("\n")
        # eğer kullanıcı bu tahminler dışında bir kelime veya harf girerse hata verecektir.
    if guessed:
        print("Congratulations... You Know... :)")
# Eğer tahmin True ise yani tahmin doğru ise programı bitir..
    else:
        print("You Lost... Another Time...")
        print("Correct Answer: %s" % (word))
# Aksi taktirde tahmin False ise program sonlanacaktır...
def main():
    word = get_word()
    play(word)
    while input("Try Again?(Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
main()




























