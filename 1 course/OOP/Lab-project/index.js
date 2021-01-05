//implement
const app = require('./app');
const database = require('./dbconect.js');
const databaseT = require('./tokendbconect.js');
const config = require('./config');


app.listen(config.PORT, () =>
      console.log(`Example app listening on port ${config.PORT}!`)
    );
database();

