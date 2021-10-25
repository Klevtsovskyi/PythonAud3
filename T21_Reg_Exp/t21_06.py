import re


EMAIL = r"^(?P<email>(?:[A-za-z]\w*\.?)+\b@(?:[a-z]\w+\.)+[a-z]{2,})"
MESSAGE = r": (?P<message>.*)"
PATTERN = EMAIL + MESSAGE


if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as inp:
        text = inp.read()

    emails = []
    messages = []

    for match in re.finditer(PATTERN, text, flags=re.MULTILINE):
        emails.append(match.group("email"))
        messages.append(match.group("message"))
    
    print(*zip(emails, messages), sep="\n")

    with open("output.txt", "w", encoding="utf-8") as out:
        print(*set(emails), sep="\n", file=out)
