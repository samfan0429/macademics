from bs4 import BeautifulSoup
import json
import re
import time
from datetime import *


with open("clicked.html", "r") as f:
    contents = f.read()

bs4_content = BeautifulSoup(contents, "html.parser")

page_structure = bs4_content.prettify()

headers = ["numsection", "name", "days", "time", "room", "instructor", "availmax"]
distributions = {"Writing WA", "Writing WP", "Writing WC", "U.S. Identities and Differences", "Internationalism", "Humanities", "Social science", "Fine arts", "Natural science and mathematics", "Quantitative Thinking Q1", "Quantitative Thinking Q2""Quantitative Thinking Q3"}


def row_to_json(content):
    startTime = datetime.now()

    # text patterns
    course_pattern = re.compile("\w{2,4}\s\d{2,3}-[a-zA-Z0-9]{2}")  # regex pattern of any course

    rows = content.find_all('tr')
    sections = []
    for i in range(len(rows)):

        cells = rows[i].find_all('td')

        # the first <tr> on the page is blank
        if len(cells) is 0:
            continue

        first_cell = cells[0].text.strip()

        # if it is a course row, scrap each cell content
        items = {}
        if course_pattern.match(first_cell):

            course_id = rows[i]["data-id"]

            # items = {}

            for i in range(len(cells)):

                infopiece = cells[i].text.strip()

                # removing characters like instructor:
                if i in range(2, 7):
                    infopiece = re.sub(".+:\s", "", infopiece)

                    if i == 6:
                        infopiece = re.sub("[\w]{6}\s", "", infopiece)
                items[headers[i]] = infopiece.strip()

            items["courseid"] = course_id
            # print(items["numsection"])

            items["course-num"] = items["numsection"].split('-')[0]
            items["dept"] = items["numsection"].split(' ')[0]

            items["start"] = items["time"].split('-')[0]

            if items["start"] != "TBA":
                items["end"] = items["time"].split('-')[1]
            else:
                items["end"] = "TBA"

            # add each course to the courses list
            sections.append(items)
            # dfd
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
                    'courseid': section['courseid'],
                    'start': section['start'],
                    'end': section['end'],
                    'sectionid': section['courseid']

                    # and so on with the properties you want
                })

        # details row
        else:
            # TODO: get <span> content of this issue
            # TODO: somehow parse through all the tags to reach span
            # TODO: Can't use find_all('span) because that way we can't attribute to this specfic course-section
            # TODO: maybe we can use specific course id (these course id also aviablel in <tr data-id="">)

        export_dict = {"fall20": courses}

    # export as JSON
    with open('fall20.json', 'w') as fout:
        json.dump(export_dict, fout, indent=4)

    print('\nTime elasped: ', datetime.now() - startTime)


def main():
    row_to_json(content)


if __name__ == '__main__':
    main()
