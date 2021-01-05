//implement

const config = require('./config');
const mongoose = require('mongoose')


module.exports= () => {
    return new Promise((resolve, reject) => {
        mongoose.Promise = global.Promise;
        console.log("I AM HERE1 /////////////////////////")

        mongoose.set('debug', true);

        mongoose.connection
          .on('error', error => reject(error))
          .on('close', () => console.log('Database connection closed.'))
         .once('open', () => resolve(mongoose.connections[0]));

        mongoose.connect(config.MONGO_URL, {useNewUrlParser: true });
  });
}