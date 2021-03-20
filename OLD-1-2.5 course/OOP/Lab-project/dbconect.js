//implement
const app = require('./app');
const database = require('./database');
const databaseT = require('./tokendb');
const config = require('./config');


module.exports= () => {
    return new Promise((resolve, reject) =>
database()
  .then(info => {
    console.log(`Connected to   ${info.host}:   port   :   ${info.port}   /    name   :  ${info.name}`);
    
    
    
  })
  .catch(() => {
    console.error('Unable to connect to database');
    process.exit(1);
  })

    )}
