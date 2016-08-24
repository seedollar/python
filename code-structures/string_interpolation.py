# Examples of how to apply interpolation to strings.

# ====================================================================
# OLD STYLE Interpolation within Python
# ====================================================================
print("%s" % 42) # String
print("%d" % 42) # Decimal
print("%f" % 42) # Float
print("%x" % 42) # Hexadecimal
print("%o" % 42) # Octal
print("%d%%" % 42) # Literal %

print("I am %d years old" % 59)
print("My name is %s, and I am %d years old" % ("Henry", 59))

print("%10d : 10 left spaces" % 97957)
print("%-10d : 10 right spaces" % 97957)

print("%10.4d %10.4f %10.4s" % (86, 86, 'Interpolation')) # limit out size to 4 characters long
print("%*.*d %*.*f %*.*s" % (5, 3, 86, 7, 3, 86.4868, 12, 4, 'Interpolation')) # replace the * with custom values

# ====================================================================
# NEW STYLE Interpolation within Python using {}
# ====================================================================
print('{} {} {}'.format(55, 863.342, "bleeding edge"))
print('{2} {0} {1}'.format(55, 863.342, "bleeding edge")) # you can specify the order of the placeholders
print('{f} {n} {s}'.format(n=453, s="diction", f=58.5527)) # You can use a dictionary and match on the key names

dict_values = {'num': 9979, 'floater': 38.3979, 'strval':'impressive'}
print("{0[num]} {0[strval]} {0[floater]}, {1}".format(dict_values, 'extraOne')) # Use dictionary variable to interpolate

print("{0:5d} {1:10f} {2:15s}".format(8682, 0.458, "cloudy")) # new style field width specified after the ":" character
print("{0:5d} {1:10.2f} {2:2.3s}".format(8682, 0.458, "cloudy")) # new style field limit specified
print("{0:!^20s}".format("BIG SALE")) # Fill characters

