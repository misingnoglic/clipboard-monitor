import clipboard
text = clipboard.paste()
with open('clipboard.txt', 'w') as clipboard_file:
    while True:
        while text == clipboard.paste():
            pass
        print clipboard.paste()
        clipboard_file.write("%s\n" % clipboard.paste())
        text = clipboard.paste()
