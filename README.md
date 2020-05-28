# Macademics

A student-built semester planning webapp for Macalester students.

This app lets you filter by distribution and general education requirments for Macalester.
You can also search by Course Number and Course Title.

To request a new feature, create an issue with the tag `feature`.
To report a bug, create an issue with the tag `bug` with screenshots/screencasts if possible.

----

Technologies used:
1. Python (BeautifulSoup4 library)
2. Vue.js
3. Firebase Firestore
4. Node.js
5. Bootstrap 4


[Current Architecture:](https://imgur.com/a/wjQLDjN)

---
To run scraper:

1. Have  `Python 3`, &nbsp; `pip`,  &nbsp; `virtualenv` &nbsp; installed.
2. Create a new virtual environment.
3. Install depedenices in that virtualenv using &nbsp;
`pip install -r requirements.txt`.
4. Run the script using  `python main.py`.

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
