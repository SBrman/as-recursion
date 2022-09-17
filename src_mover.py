import os

for root, folders, files in os.walk('.'):
    if root.startswith(r'./.git') or '.git' in root:
        continue

    for file in files:
        fileName = file.split('.')[0]
        firstLineJs = fr'<script type="text/javascript", src="{fileName}.js">'
        path = os.path.join(root, file)

        if file.endswith('html'):
            with open(path) as htmlFile:
                code = htmlFile.readlines()
                if len(code) == 0:
                    continue
                if firstLineJs in code[0]:
                    continue 
            
            with open(path.replace('html', 'js'), 'w') as jsFile:
                jsFile.write(''.join(code[1:-2]))

            with open(path, 'w') as htmlFile:
                htmlFile.write(firstLineJs)
                htmlFile.write(r'</script>')

