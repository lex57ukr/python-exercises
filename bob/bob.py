def hey(text):
    if is_shouting(text):
        response = 'Whoa, chill out!'
    elif is_question(text):
        response = 'Sure.'
    elif is_silence(text):
        response = 'Fine. Be that way!'
    else:
        response = 'Whatever.'

    return response


def is_shouting(text):
    return text.isupper()


def is_question(text):
    return text.rstrip().endswith('?')


def is_silence(text):
    return not text or text.isspace()
