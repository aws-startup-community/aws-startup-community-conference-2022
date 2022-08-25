import csv
from fileinput import filename
import shutil


def replace(file, row):
    with open(file, encoding="utf-8") as f:
        data_lines = f.read()
    data_lines = data_lines.replace("${id}", row['id'])
    data_lines = data_lines.replace("${title}", row['title'])
    data_lines = data_lines.replace("${name}", row['name'])
    data_lines = data_lines.replace("${track}", row['track'])
    data_lines = data_lines.replace("${company}", row['company'])
    data_lines = data_lines.replace("${starttime}", row['starttime'])
    data_lines = data_lines.replace("${nexttime}", row['nexttime'])

    with open(file, mode="w", encoding="utf-8") as f:
        f.write(data_lines)


if __name__ == "__main__":
    with open('data.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            file_name = f"scripts/inter-session-speeches-{row['id']}.md"
            if row['id'] in ('a-6', 'b-6'):
                shutil.copyfile("inter-session-speeches-template_last.md", file_name)
            else:
                shutil.copyfile("inter-session-speeches-template.md", file_name)
            replace(file_name, row)



