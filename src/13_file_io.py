"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open("foo.txt","r") as f:
    read_data = f.read()
    print(read_data)

with open("bar.txt","a+") as b:
    b.write("testing\n")
    b.write("1\n")
    b.write("2\n")

with open("bar.txt","r") as a:
    read_data = a.read()
    print(read_data)