# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def generate_pass(word):
    password = get_first_two_letters(word)
    password += str(len_word(word))
    password += even_odd(len(word))
    password += middle_letters(word, len(word))
    password += str(count_vowels(word))
    password += get_last_two_letters(word)
    return password

def get_first_two_letters(word):
    return word[0] + word[1]

def get_last_two_letters(word):
    return word[-1] + word[-2]

def len_word(word):
   return len(word)

def even_odd(lenWord):
   return '@' if lenWord % 2 == 0 else '$'

def middle_letters(word, lenWord):
    middle = int(lenWord / 2)
    return word[middle -1] + word[middle]

def count_vowels(word):
    count = 0;
    for a in ('a', 'e', 'i', 'o', 'u'):
        count += word.count(a)
    return count 

if __name__ == '__main__':
    if len(sys.argv) >= 2 and len(sys.argv[1]) > 2:
        print(generate_pass(sys.argv[1]))
    else:
        print('Argumento no valido')
