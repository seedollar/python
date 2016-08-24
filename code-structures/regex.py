# Regex examples in Python
import re

text = "Young Frankenstein"
result = re.match("You", text)
print(result.group())

match1 = re.match('Frank', text)
if match1:
    print("Match1: ", match1.group())

match2 = re.match('.*Frank', text)
if match2:
    print("Match2: ", match2.group())

match3 = re.findall('n', text)
print("Match3: ", match3)

match4 = re.findall('n.', text)
print("Match4: ", match4)

match5 = re.findall('n.?', text)
print("Match5: ", match5)

match6 = re.split('n', text)
print("Match6: ", match6)

# replace example
match7 = re.sub('n', 'z', text)
print("Match7: ", match7)

# =====================================================================================================
source_text = "I wish I may, I wish I might\n... Have a dish of fish tonight."
# =====================================================================================================

match8 = re.findall('wish', source_text)
print("Match8: ", match8)

# Find words wish or fish
match9 = re.findall('wish|fish', source_text)
print("Match9: ", match9)

# Find word 'wish' at the beginning
match10 = re.findall('^wish', source_text)
print("Match10: ", match10)

# Find words 'I wish' at the beginning
match11 = re.findall('^I wish', source_text)
print("Match11: ", match11)

# Find word 'fish' at the end
match12 = re.findall('fish$', source_text)
print("Match12: ", match12)

# Find word 'fish tonight.' at the end
match13 = re.findall('fish tonight.$', source_text)
print("Match13: ", match13)

# Start by finding w or f, followed by 'ish'
match14 = re.findall('[wf]ish', source_text)
print("Match14: ", match14)

# Find one or more runs of w, s or h characters
match15 = re.findall('[wsh]+', source_text)
print("Match15: ", match15)

# Find 'ght' followed by a non-alphanumeric character
match16 = re.findall('ght\W', source_text)
print("Match16: ", match16)

# Find 'I' followed by 'wish'
match17 = re.findall('I (?=wish)', source_text)
print("Match17: ", match17)

# Find 'wish' preceeded by 'I'
match18 = re.findall('(?<=I) wish', source_text)
print("Match18: ", match18)

# Find a boundary word ("\b") fish. NOTICE you have to disable python character exscaping bacause Python escapes \b as backspace.
# You disable python character escape by placing the character 'r' before the regex expression.
match19 = re.findall(r"\bfish", source_text)
print("Match19: ", match19)
