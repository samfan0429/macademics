const firestoreService = require('firestore-export-import');

const serviceAccount = require('../privateServiceAccountKey.json');
const databaseURL= "https://macademics-8cf04.firebaseio.com";



firestoreService.initializeApp(serviceAccount, databaseURL);


// import data
firestoreService.restore(
    '../scraper/spring20.json',
);