lines_seen = set()

with open('hw11_miniproj_data1.txt', 'r+') as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i not in lines_seen:
            f.write(i)
            print(i)
            lines_seen.add(i)
    f.truncate()
    
    num_lines = sum(1 for line in open('hw11_miniproj_data1.txt')) - 1
    print("Number of people = " + str(num_lines))
    f.close()
    
# if you find 2, then remove it from the file

# number of non-duplicates in new file + number of lines in duplicate list = total number of people

# when we find the line in the file, and that matches the line in the set

