"""Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.

Декілька правил:

ніяких символів з набору string.punctuation не повинно бути, в тому числі й пробілів;
підсумкова довжина hashtag має бути не більше 140 символів.
кожне слово починається з великої літери.
якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

'Python Community' -> #PythonCommunity
'i like python community!' -> #ILikePythonCommunity
'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

"""

import string

user_input = input("Enter your sentence: ")
capitalized_text = user_input.title()
print(capitalized_text)

prohibited_symbols = string.punctuation + " "
for i in prohibited_symbols:
    capitalized_text = capitalized_text.replace(i, "")

hashtag_text = "#" + capitalized_text
hashtag = hashtag_text[:140]
print(hashtag)
