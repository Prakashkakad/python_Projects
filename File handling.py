# import os
# os.mkdir("file.txt")

# f = open('file1.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# ----------------------------------Read,Readlines-----------------
# f = open('file1.txt','r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of Student {i} in maths is:{m1}")
#     print(f"Marks of Student {i} in English is:{m2}")
#     print(f"Marks of Student {i} in marathi is:{m3}")


# ---------------WriteLines------------
# f = open('file1.txt', 'w')
# lines = ['line 1/n', 'line 2/n', 'line 3/n', 'line 4/n', 'line 5/n']
# f.writelines(lines)
# f.close()


# ---------------seek()-------
#with open('file1.txt','r') as f:
    # print(type(f))
    # f.seek(2)
    # data = f.read(5)
    # print(data)


# -------------------truncate ()
with open('file1.txt', 'w') as f:
    f.write('Helllo World')
    f.truncate(5)

with open('file1.txt','r') as f:
    print(f.read())


