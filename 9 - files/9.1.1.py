
def are_files_equal(file1, file2):
    file1 = open(file1, 'r')
    file2 = open(file2, 'r')
    if file1.read() == file2.read():
        return True
    return False

print(are_files_equal(r"C:\Users\LIAMR\Documents\Magshimim\Python\9 - files\Files\abc.txt", r"C:\Users\LIAMR\Documents\Magshimim\Python\9 - files\Files\def.txt"))