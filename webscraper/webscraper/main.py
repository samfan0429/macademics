from bs4 import BeautifulSoup
import json
import re
import requests
from datetime import *
from concurrent.futures import ThreadPoolExecutor

distributions = {"Writing WA", "Writing WP", "Writing WC", "U.S. Identities and Differences", "Internationalism",
                 "Humanities", "Social science", "Fine arts", "Natural science and mathematics",
                 "Quantitative Thinking Q1", "Quantitative Thinking Q2", "Quantitative Thinking Q3"}


def section_scraper(content) -> list:
    """Scrape all the sections on the course schedule page"""
    dept_tables = content.find_all('tbody')
    sections = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        for section in executor.map(section_parser, dept_tables):
            sections.append(section)

    return sections


def section_grouper(sections) -> dict:
    """Groups sections of the same course under same course"""
    courses = {}
    for dept_list in sections:
        for section in dept_list:
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
                'module': section['module']
            })

    return courses


def section_parser(dept_table) -> list:
    """Parse all the sections within a department"""
    rows = dept_table.find_all('tr')
    dept_items = []
    for j in range(0, len(rows), 2):

        items = {}

        # unique CRN code
        section_id = rows[j].get("data-id")
        items["section-id"] = section_id

        cells = rows[j].find_all('td')
        headers = ["numsection", "name", "days", "time", "room", "instructor", "availmax"]
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
        details_url = "https://webapps.macalester.edu/registrardata/classdata/fall2020/" + section_id

        details_page = requests.get(details_url, verify=False)
        details_soup = BeautifulSoup(details_page.text, features="lxml")
        distributions = details_soup.find_all('span')
        for item in distributions:
            items["distributions"].append(item.text)

        description_element = details_soup.find('p')
        items["description"] = description_element.text.strip()

        module_title = dept_table.find_previous("h4").text
        if module_title.split()[-1] == "Full":
            # last word in module title is 'Full'
            module = "full"
        else:
            # module title ends in a number
            module = module_title[-1]
        items["module"] = module

        # add each course to the courses list
        dept_items.append(items)
    return dept_items


def main():
    startTime = datetime.now()

    semester_url = "https://www.macalester.edu/registrar/schedules/2020fall/class-schedule/"
    semester_requests = requests.get(semester_url).text
    bs4_content = BeautifulSoup(semester_requests, "lxml")

    sections = []
    courses = section_grouper(section_scraper(bs4_content))

    # export as JSON
    export_dict = {"fall20": courses}
    with open('fall20.json', 'w') as fout:
        json.dump(export_dict, fout, indent=4)

    print('\nTime elasped: ', datetime.now() - startTime)


if __name__ == '__main__':
    main()
