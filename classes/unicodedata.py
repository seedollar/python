# Illustates the use of the unicodedata function from the standard library
snowman = '\u2603'
print(snowman)
snowman_encoded_utf8 = snowman.encode('utf-8')
snowman_encoded_ascii = snowman.encode('ascii', 'backslashreplace')
snowman_encoded_ascii_xmlcharref = snowman.encode('ascii', 'xmlcharrefreplace')
print("UTF-8:", snowman_encoded_utf8)
print("ASCII: ", snowman_encoded_ascii)
print("ASCII XmlCharRef:", snowman_encoded_ascii_xmlcharref)

