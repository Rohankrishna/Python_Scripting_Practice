# with open('test_file.txt','r+') as test:
#     test.write("Adding this content to the existing text in the file")
#     print("closed or not: ",test.closed)
#     print("Name of file: ",test.name)
#     print("Opening mode: ",test.mode)
#     print(test.read(1000))


import subprocess

with open("output.txt", "w+") as output:
    subprocess.call(["python3.6", "element_search.py"], stdout=output);
    output.close()