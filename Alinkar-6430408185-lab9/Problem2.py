import re

text = input("Enter Text: ")
pattern = input("Enter pattern: ")
match = (re.search(pattern, text))


#number = len(re.findall(pattern, text))

if match:
    span = match.span()
    start = span[0]
    print(f"Found {pattern} in {text} at {start}")
else:
    print(f"Cannot find {pattern} in {text}")


