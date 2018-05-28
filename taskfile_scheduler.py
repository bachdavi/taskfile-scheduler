import sys, os

NOTE_PATH='/Users/david/ownCloud/nvALT/Taskpaperxcopy.txt'
TASK = ''

HELP_STRING= """ task_keeper:
        -h(--help): Return this string
        -w: Weekly schedule and test of the task file
        -m: Monthly schedule and testing of task file
        -n: Not changeing the task file"""

def test_arguments():
    '''Testing the usage of the script'''
    if len(sys.argv) != 2:
        print(HELP_STRING)
        exit(1)
    elif sys.argv[1] == "-h":
        print(HELP_STRING)
        exit(1)
    elif sys.argv[1] in ["-t", "-tm"]:
        pass
    else:
        print(HELP_STRING)
        exit(1)

def create_notification(content):
    '''Creating an output string depending on what the content was'''
    if content == 'today':
        return ""

def change_task(content):
    '''Alter the content to match due(...)'''

def archive_tasks(content):
    '''Archive tasks which are done while running the weekly/monthly'''


def main():
    output_list= []
    parameter_dict = {'-t':"today", '-tm':"tomorrow"}
    '''Main method of the script'''
    with open(NOTE_PATH) as f:
        for line in f.readlines():
            splitted_line = [tag.rstrip() for tag in line.split('@')]
            tags = splitted_line[1:]
            if parameter_dict[sys.argv[1]] in tags and "done" not in tags:
                content = splitted_line[0].split('-')[1].strip()
                output_list.append(('- ' + content + '\n', tags))
    os.system('./notification.scpt "{}"'.format(" ".join([x[0] for x in output_list])))
    if sys.argv[1] == "-tm":
        for line in output_list:
            sed_command = 'sed -i "" "s/{} @.*/{} @today/g" {}'.format(line[0].rstrip(), line[0].rstrip(), NOTE_PATH)
            os.system(sed_command)




if __name__ == "__main__":
    test_arguments()
    main()
