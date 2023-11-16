import sys

import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
with open(sys.argv[1], 'r') as f:
    content = f.read()
    tokens = len(enc.encode(content))
    words = len(content.split())
    chars = len(content)
    print(f'{tokens} tokens, {words} words, {chars} characters.\ntok/word {round(tokens/words, 4)}, avg word l {round(chars/words, 4)}, char/tok {round(chars/tokens, 4)}')
