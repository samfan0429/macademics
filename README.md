# Macademics

A student-built semester planning webapp for Macalester students.

This app lets you filter by distribution and general education requirments for [Macalester College](https://macalester.edu).

You can also search by Course Number `COMP 123` and Course Title `Introduction to Computer Science`.

_We would love your feedback as users so please find our names on the Student Directory and email us! Thanks! Happy planning!_

---
Development

To request a new feature, create an issue with the tag `feature`.

To report a bug, create an issue with the tag `bug` with screenshots/screencasts if possible.

Technologies used:
1. Python (BeautifulSoup4 library)
2. Vue.js
3. Firebase Firestore
4. Node.js
5. Bootstrap 4


[Current Architecture:](https://imgur.com/a/wjQLDjN)

We are trying to use [commit-conventions](https://www.conventionalcommits.org/en/v1.0.0/) for a better development process.

---
To run scraper:

1. Have  `Python 3`, &nbsp; `pip`,  &nbsp; `poetry` &nbsp; installed.
2. Run `poetry install` in the webscraper directory.
3. Run the script using  `python main.py`.

---
To run `firestore-loader`:

1. Have `node` v12 installed.
2. Have a private ServiceAccountKey to Firebase project.
3. Have npm package `firestore-export-import` installed.

---

To run the web app

1. `cd` into vue directory
2. `npm install` to install depedencies
3. `npm run dev` to run the website in dev mode.

---

This was created in the Spring 2020 by 
Aguilar Alejandro, [Kyaw Za Zaw](https://kyawza.me), Michale Steele, [Ngo Nhat](https://www.linkedin.com/in/nhat-ngo-a9939716a).
