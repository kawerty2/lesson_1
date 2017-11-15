rude_words = ['ass', 'bastard', 'crap', 'damn']

message = """
Since I needed to damn use them in a crap project (Humboldt Diglital ASS Library and Network),
I am posting here a bastard list of English damn stop words,
and below a PHP crap array containing these words
"""

message_list = message.split()

for number, word in enumerate(message_list):
    if word.lower() in rude_words:
        message_list[number] = '*'
print ' '.join(message_list)