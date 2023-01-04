from os import walk
inputFiles = next(walk("input"), (None, None, []))[2]
outputFiles = next(walk("output"), (None, None, []))[2]

inputsList = []
outputsList = []

for filename in inputFiles:
    with open(f"input/{filename}") as file:
        lines = file.readlines()
        result = "".join(lines).strip()
        inputsList.append(result)

for filename in outputFiles:
    with open(f"output/{filename}") as file:
        lines = file.readlines()
        result = "".join(lines).strip()
        outputsList.append(result)

elementy = []
for element in range(0, len(inputsList)):
    element = f"<tr> <th>{inputsList[element]} </th><th> {outputsList[element]}</th> </tr>"
    elementy.append(element)

file_html = open("raport.html", "w")
file_html.write('''
<html>
    <head>
        <title>Raport</title>
        <link rel="stylesheet" href="styles.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;700&display=swap" rel="stylesheet">
    </head>
    <body>
        <div class="container">
            <h1>Raport</h1>
            <table>
                <tr class="top-row">
                    <th>Input</th>
                    <th>Output</th>
''')

for element in elementy:
    file_html.write(element)

file_html.write('''
            </table>
            <footer>
                <p>Created by <a href=https://github.com/Hunterlios>Jakub Mrozek</a></p>"
            </footer>
        </div>
    </body>
</html>
''')

file_html.close()
