def saveToFile(fileName, format, content):
    with open(f'{fileName}.{format}', 'w', encoding='utf-8') as f:
        f.write(content)


def saveWebPageToFile(fileName, content):
    saveToFile('./_html/' + fileName, 'html', content)


def saveJsonToFile(fileName, content):
    saveToFile('./_json/' + fileName, 'json', content)
