import emoji

def emoji_func(text):
    return emoji.emojize(text)

user_input = input('Enter text to generate emoji: ')
gen_emoji = emoji_func(user_input)

print('Final result: ', gen_emoji)


# Try this https://app.testdome.com/screening/challenge/45

