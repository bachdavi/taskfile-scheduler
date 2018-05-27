NOTE_PATH='/Users/david/ownCloud/nvALT/Taskpaperx.txt'

def create_notification(tag):
    '''Creating an output string depending on what the tag was'''
    if tag == 'today':
        return ""


with open(NOTE_PATH) as f:
    for line in f.readlines():
        splitted_line = [tag.rstrip() for tag in line.split('@')]
        tags = splitted_line[1:]
        content = splitted_line[0].split('-')[1].strip()
        if tags:
            print(tags)
            print(content)
