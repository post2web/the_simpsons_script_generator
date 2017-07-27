import string
import re

value_to_token = {
    '.': '[period]',
    ',': '[comma]',
    '"': '[quotation_mark]',
    "'": '[apostrophe]',
    ':': '[colon]',
    ';': '[semicolon]',
    '!': '[exclamation_mark]',
    '?': '[question_mark]',
    '(': '[left_parentheses]',
    ')': '[right_parentheses]',
    '-': '[dash]',
    '/': '[fslash]',
    '\\': '[bslash]',
    '\n': '[return]',
    '\t': '[tab]',
    ' ': '[space]',
}

token_to_value = dict(zip(value_to_token.values(), value_to_token.keys()))

def text_to_tokens(text):
    text = text.replace('[', '(').replace(']', ')')
    for key, token in value_to_token.items():
        text = text.replace(key, token)
    
    tokens = re.compile("(\\[.*?\\])").split(text)
    # tokens will have empty results so better filter it
    tokens = list(filter(None, tokens))
    
    # fix capital letters
    new_tokens = []
    for token in tokens:
        if token[0].isupper():
            new_tokens.append('[capital]')
        new_tokens.append(token.lower())

    return new_tokens

def tokens_to_text(sentence_tokens):
    text = ''
    capitalize = False
    for token in sentence_tokens:
        if token == '[capital]':
            capitalize = True
            continue
        if capitalize:
            capitalize = False
            if token not in token_to_value:
                token = token.title()
        if token in token_to_value:
            text += token_to_value[token]
        else:
            text += token
    return text
