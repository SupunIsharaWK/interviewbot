filename = ['python_tutorial.pdf', 'php_tutorial.pdf']


# filename = ['python_tutorial.pdf', 'Python Lists.pdf', 'example3.pdf', 'example4.pdf', 'example5.pdf', 'example6.pdf',
#             'example7.pdf', 'example8.pdf', 'example9.pdf', 'example10.pdf']

def getFileName(num):
    numberOfFiles = len(filename)

    for fileNum in range(0, numberOfFiles):
        if fileNum == num:
            pdfFileName = filename[fileNum]
            return pdfFileName


if __name__ == '__main__':
    # getFileName(filename)
    print(getFileName(1))
