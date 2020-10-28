

import re


SENTENCE = r"\b([A-ZА-ЯЇІЄ].+?[\.?!])(?<![A-ZА-ЯЇІЄ][a-zа-яїіє]\.)(?<!\w\.[a-zа-яїіє].)\s"


if __name__ == '__main__':
    with open("input.txt", "r", encoding="utf-8") as inp:
        text = inp.read()
        rgx = re.compile(SENTENCE, flags=re.S)
        sents = rgx.findall(text)
        print(*sents[:100], sep="\n~\n")
    with open("output.txt", "w", encoding="utf-8") as out:
        print(*sents, sep="\n~\n", file=out)
