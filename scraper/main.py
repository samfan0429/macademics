from bs4 import BeautifulSoup
import json
import re
from datetime import *

with open("clicked.html", "r") as f:
    contents = f.read()

bs4_content = BeautifulSoup(contents, "html.parser")

page_structure = bs4_content.prettify()

headers = ["numsection", "name", "days", "time", "room", "instructor", "availmax"]
distributions = {"Writing WA", "Writing WP", "Writing WC", "U.S. Identities and Differences", "Internationalism",
                 "Humanities", "Social science", "Fine arts", "Natural science and mathematics",
                 "Quantitative Thinking Q1", "Quantitative Thinking Q2""Quantitative Thinking Q3"}


def row_to_json(content):
    dept_tables = content.find_all('tbody')

    sections = []

    for i in range(0, len(dept_tables)):
        rows = dept_tables[i].find_all('tr')
        for j in range(0, len(rows), 2):
            cells = rows[j].find_all('td')

            items = {}

            for i in range(len(cells)):

                infopiece = cells[i].text.strip()

                # removing characters like "instructor:"
                if i in range(2, 7):
                    infopiece = re.sub(".+:\s", "", infopiece)

                    if i == 6:
                        infopiece = re.sub("[\w]{6}\s", "", infopiece)
                items[headers[i]] = infopiece.strip()

            # items["courseid"] = course_id

            items["course-num"] = items["numsection"].split('-')[0]
            items["dept"] = items["numsection"].split(' ')[0]

            items["start"] = items["time"].split('-')[0]

            if items["start"] != "TBA":
                items["end"] = items["time"].split('-')[1]
            else:
                items["end"] = "TBA"

            # TODO: get <span> content of this issue
            # TODO: somehow parse through all the tags to reach span
            # TODO: Can't use find_all('span) because that way we can't attribute to this specfic course-section
            # TODO: maybe we can use specific course id (these course id also aviablel in <tr data-id="">)

            # add each course to the courses list
            sections.append(items)

    # Section Grouper
    courses = {}
    for section in sections:
        if section['course-num'] not in courses:
            courses[section['course-num']] = {
                # 'course-num': section['course-num'],
                'dept': section['dept'],
                'name': section['name'],
                'sections': []
            }

        courses[section['course-num']]['sections'].append({
            'numsection': section['numsection'],
            'instructor': section['instructor'],
            'days': section['days'],
            'availmax': section['availmax'],
            'start': section['start'],
            'end': section['end'],
            # 'sectionid': section['courseid']
        })

    # export as JSON
    export_dict = {"fall20": courses}

    with open('fall20.json', 'w') as fout:
        json.dump(export_dict, fout, indent=4)


def main():
    startTime = datetime.now()
    row_to_json(bs4_content)
    print('\nTime elasped: ', datetime.now() - startTime)


if __name__ == '__main__':
    main()
