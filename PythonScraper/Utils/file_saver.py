import csv


def saveToFile(fileName, format, content, append):
    with open(f'{fileName}.{format}', "a" if append else "w", encoding='utf-8') as f:
        f.write(content)


def saveWebPageToFile(fileName, content):
    saveToFile('./_html/' + fileName, 'html', content)


def saveJsonToFile(fileName, content, append=False):
    saveToFile('./_json/' + fileName, 'json', content, append)


def saveToCsv(fileName, content, append=False):
    with open(f"./_csv/{fileName}.csv", mode="a" if append else "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",", quotechar="\"",
                            quoting=csv.QUOTE_MINIMAL)
        for entry in content:
            writer.writerow(entry.values())
