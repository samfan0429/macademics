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

            items = {}

            # unique CRN code
            section_id = rows[j].get("data-id")
            items["section-id"] = section_id

            cells = rows[j].find_all('td')
            for i in range(len(cells)):

                infopiece = cells[i].text.strip()

                # removing characters like "instructor:"
                if i in range(2, 7):
                    infopiece = re.sub(".+:\s", "", infopiece)

                    if i == 6:
                        infopiece = re.sub("[\w]{6}\s", "", infopiece)
                items[headers[i]] = infopiece.strip()

            # data sanitizing
            items["course-num"] = items["numsection"].split('-')[0]
            items["dept"] = items["numsection"].split(' ')[0]
            items["start"] = items["time"].split('-')[0]

            if items["start"] != "TBA":
                items["end"] = items["time"].split('-')[1]
            else:
                items["end"] = "TBA"

            # course additional details 
            items["distributions"] = []
            items["description"] = ""
            detail_element = rows[j + 1].find(id="crs" + section_id)
            if detail_element != None:
                distributions = detail_element.find_all('span')
                for item in distributions:
                    items["distributions"].append(item.text)

                description_element = detail_element.find('p')
                items["description"] = description_element.text.strip()

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
                'description': section['description'],
                # assuming each course has the same distributions, 
                # (edge cases exist with topic courses + a couple more)
                'distrbutions': section['distributions'],
                'sections': [],
            }

        courses[section['course-num']]['sections'].append({
            'numsection': section['numsection'],
            'instructor': section['instructor'],
            'days': section['days'],
            'availmax': section['availmax'],
            'start': section['start'],
            'end': section['end'],
            'section-id': section['section-id'],
            
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
