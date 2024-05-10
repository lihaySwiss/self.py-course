def copy_file_content(source, destination):
    source = open(source, 'r')
    with open(destination,  'w') as output_file:
        output_file.write(source.read())

print(copy_file_content("C:\sampleFile.txt", "C:\sampleFile.txt"))