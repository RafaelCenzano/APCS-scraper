import sys
import requests

class ReadmeReader():

    def __init__(self):
        pass

    def clean(self, filePath, delete=False, message=True):

        with open(filePath, 'r') as f:
            data = f.readlines()

        start = self.findStudentsIndex(data)

        readme = open(filePath, 'w')

        count = 0
        while count < start:
            readme.write(data[count])
            count += 1

        while start < len(data):
            url = self.extractUrl(data[start])

            try:

                requested = requests.head(url).status_code

                if requested == 404:
                    print(f'Not found: {url}')

                    if delete:
                        if message:
                            readme.write(f'<!-- Hidden: {data[start].rstrip()} -->\n')

                    else:
                        readme.write(f'{data[start].rstrip()} <!-- 404 not found -->\n')

                else:
                    readme.write(data[start])
                start += 1

            except:

                if url != '':
                    print(f'Error with: {url}')
                    readme.write(f'<!-- Hidden: {data[start].rstrip()} Error requesting page -->\n')
                start += 1

        readme.write('''

''')
        readme.close()

    def findStudentsIndex(self, data):

        for count in range(len(data)):
            if 'student work' in data[count].lower():
                return count + 2

    def extractUrl(self, string):
        
        start = 0
        end = 0

        length = len(list(string))

        for count in range(length):
            if string[count:count + 4] == 'http':
                start = count
                break

        for count in range(length):
            if string[count:count + 1] == ')':
                end = count
                break

        return string[start:end]

if __name__ == '__main__':
    path = sys.argv[1]
    try:
        howTo = sys.argv[2]
    except:
        howTo = ''

    readme = ReadmeReader()

    message = True
    delete = False

    if howTo.lower() == 'hide':
        delete = True

    if howTo.lower() == 'delete':
        delete = True
        message = False

    readme.clean(path, delete=delete, message=message)

