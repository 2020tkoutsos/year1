def encrypt(string, shift):
    a = list("abcdefghijklmnopqrstuvwxyz")
    num_hash = {}
    a_hash = {}
    count = 1
    for x in range(len(a)):
        num_hash[x+1] = a[x]
    for y in a:
        a_hash[y] = count
        count += 1

    w = list(string)
    n_word = []

    for letter in w:
        if letter in a:
            place = a_hash[letter]
            place += shift
            if place > 26:
                place -= 26
                n_letter = num _hash[place]
                N
w.append(n_letter)
            else:
                n_letter = num_hash[place]
                n_word.append(n_letter)
        else:
            n_word.append(letter)

    print(''.join(n_word))

encrypt("yaya", 1)

def decrypt(string, shift):
    # def function
    a = list("abcdefghijklmnopqrstuvwxyz")
    # create the list of the alphabet
    num_hash = {}
    a_hash = {}

    count = 1
    for x in range(len(a)):
        num_hash[x+1] = a[x]
    for y in a:
        a_hash[y] = count
        count += 1


    w = list(string)
    n_word = []

# loop through word
    for letter in w:
#check if letter is in the hash
        if letter in alphabet:
#get the number matching the letter
            place = alphabet_hash[letter]
#subtract the shift from the number value
            place -= shift
# check if shift is too far
            if place < 0:
#put value back in boundaries
                place += 26
#locate new letter
                n_letter = number_hash[place]
#add letter to word
                n_word.append(n_letter)
            else:
                n_letter = number_hash[place]
                n_word.append(n_letter)
        else:
            n_word.append(letter)
#join word
    print(''.join(n_word))


decrypt("yaya", 1)
