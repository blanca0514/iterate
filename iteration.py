def fizz_buzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FIzzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz()

def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0, 100)
s1 = ss(numbers, 22)
print(s1)
s2 = ss(numbers, 202)
print(s2)


def palindrome(word):
    word = word.lower()
    return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Mom"))

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram("cinema", "iceman"))
print(anagram("leaf", "tree"))


def count_character(string):
    count_dict = {}

    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)

count_character("Blanca")

def bottles_of_beer(bob):
    if bob < 1:
        print("No more bottles of beer on the wall. No more bottles of beer.")
        return
    tmp = bob
    bob -= 1
    print("{} bottles of beer on the wall. {} bottles of beer. Take one down, pass it around, {} bottles of beer on the wall.".format(tmp, tmp, bob))
    bottles_of_beer(bob)

bottles_of_beer(99)
