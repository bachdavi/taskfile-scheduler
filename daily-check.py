NOTE_PATH='/Users/david/ownCloud/nvALT/Taskpaperx.txt'

# How to run:
# task_keeper:
#   -h(--help): Return this string
#   -w: Weekly schedule and test of the task file
#   -m: Monthly schedule and testing of task file
#   -n: Not changeing the task file
#

def test_arguments():


def create_notification(content):
    '''Creating an output string depending on what the content was'''
    if content == 'today':
        return ""

def change_task(content):
    '''Alter the content to match due(...)'''

def archive_tasks(content):
    '''Archive tasks which are done while running the weekly/monthly'''


def main():
    '''Main method of the script'''
    with open(NOTE_PATH) as f:
        for line in f.readlines():
            splitted_line = [tag.rstrip() for tag in line.split('@')]
            tags = splitted_line[1:]
            content = splitted_line[0].split('-')[1].strip()
            if tags:
                print(tags)
                print(content)

if __name__ == "__main__":
    main()
