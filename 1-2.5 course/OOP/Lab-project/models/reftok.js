const mongoose = require('mongoose')
const Schema = mongoose.Schema;

const schema = new Schema({
    id: {
        type : String,
        required : true,
        //unique : true
    },
    refreshtoken:
    {
        type : String,
        required : true
    }
},
{
    timestamps: true
}



)

schema.set('toJSON',
{
    virtuals : true
})

module.exports = mongoose.model('Rtoken', schema)