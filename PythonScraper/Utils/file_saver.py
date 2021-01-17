import csv


def saveToFile(fileName, format, content):
    with open(f'{fileName}.{format}', 'w', encoding='utf-8') as f:
        f.write(content)


def saveWebPageToFile(fileName, content):
    saveToFile('./_html/' + fileName, 'html', content)


def saveJsonToFile(fileName, content):
    saveToFile('./_json/' + fileName, 'json', content)


def saveToCsv(fileName, content):
    with open(f"./_csv/{fileName}.csv", mode='w', encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",", quotechar="\"",
                            quoting=csv.QUOTE_MINIMAL)
        for entry in content:
            writer.writerow(entry.values())
