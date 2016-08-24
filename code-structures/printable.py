# Illustration of the string standard library's printable property
import string, re

printable = string.printable
print(printable)

digits_only_match = re.findall("\d", printable)
print("Digits only: ", digits_only_match)

alphanumeric_match = re.findall("\w", printable)
print("Aplhanumeric characters: ", alphanumeric_match)

spaces_match = re.findall("\s", printable)
print("Space characters: ", spaces_match)

# special characters are also found when using \w
text_with_ascii_chars = "abc" + "-/*" + "\u00ea" + "\u0115"
special_char_match = re.findall("\w", text_with_ascii_chars)
print("Special chars included: ", special_char_match)




