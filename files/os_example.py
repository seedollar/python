import os

print(os.path.exists('oops.txt'))
print(os.path.exists('relativity'))
print(os.path.exists('.'))
print(os.path.exists('..'))

print(os.path.isfile('relativity'))
print(os.path.isdir('relativity'))

# Check if the path is absolute
print(os.path.isabs('relativity'))
print(os.path.isabs('/tmp'))

# get the absolute path
print(os.path.abspath('relative'))

# Create a unix symbolic link
# os.link("relativity", "relativity_link")
# Now get the realpath of the symbolic link
#print(os.path.realpath('relativity_link'))

# Rename a file
# print(os.rename('relativity', 'relativity_renamed'))

# chmod file permission
os.chmod('relativity', 0o755)

# chown a file
# uid = 5
# gid = 22
# os.chown('relativity', uid, gid)
