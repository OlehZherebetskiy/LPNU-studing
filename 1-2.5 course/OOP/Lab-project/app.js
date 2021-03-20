var express = require('express');

const bodyParser = require('body-parser')
const User = require('./models/user');
const Rtoken = require('./models/reftok');
const bcrypt = require('bcrypt-nodejs');
const config = require('./config.js');
const jwt = require('jsonwebtoken');
const uuid = require('uuid/v4');
var app = express();
var token;
var refreshToken


app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({extended: true}))
//app.use(session({ secret: config.secret, cookie: { maxAge: 60000 }, resave: false, saveUninitialized: false }));

/////////////////////////////////////////////////////////////////////////////////////////
app.get('/auth', function (req, res) {
    
  res.render('auth');
});




app.get('/reg', function (req, res) {
    res.render('reg');
});



//////////////////////////////////////////////////////////////////////////////////////////


var authLine ;
app.post('/auth', function (req, res) {
    //res.redirect('/');
    const na = req.body.name;
    const pa = req.body.pass;
  

    if(!na || !pa) 
    {
        console.log("Всі поля мусять бути заповненні"),
        res.json(
            {
                ok:false,
                error:"Всі поля мусять бути заповненні",
            }
        )
        
    }
    else
    {
        
        User.findOne(
            {name : na}
          ).then(user => {

            if(!user)
            {
                console.log('Логін і пароль не правильні!(403)');
                res.json({
                    ok: false,
                    error: 'Логін і пароль не правильні!(403)',
            })}
            else{
                bcrypt.compare(pa,user.pass,function(err, result)
                {
                    //console.log(result)
                    if(result)
                    {
                      
                        console.log(user._id)
                         refreshToken = uuid();


                        
                        Rtoken.create({
                          
                          id: user._id,
                          refreshtoken: refreshToken
                        })

                         token =jwt.sign({id:user._id},config.secret,{expiresIn: '10000ms'});
                        res.json({
                          token,
                          refreshToken,
                          status: 200
                        }) 
                        
                                              
                       
                    }
                    else
                    { console.log('Логін і пароль не правильні!(403)');
                    res.json({
                        ok: false,
                        error: 'Логін і пароль не правильні!(403)',
                })}
                })
            }

             
            
            
        })
        .catch(err =>{
                console.log(err);
                res.json({
                    ok: false,
                    error: 'Ошибка, попробуйте позже!'
                })
            })
    }
    
    
});



/*
----------------
----------------------
-------------------
*/
app.post('/reg', function (req, res) {
    //res.redirect('/');
    const na = req.body.name;
    const pa = req.body.pass;
    const paco = req.body.passconf;
    

    if(!na || !pa || !paco) 
    {
        console.log("Всі поля мусять бути заповненні"),
        res.json(
            {
                ok:false,
                error:"Всі поля мусять бути заповненні",
            }
        )
        
    }
    else if (!/^[a-zA-Z0-9]+$/.test(na)) {
        res.json({
          ok: false,
          error: 'Только латинские буквы и цифры!'
        });
      }
    else if (na.length < 3 || na.length > 16) {
        res.json({
          ok: false,
          error: 'Длина логина от 3 до 16 символов!'
        });
      }
    else if (pa !== paco) {
        res.json({
          ok: false,
          error: 'Пароли не совпадают!'
        });
      }
    else if (pa.length < 5) {
        res.json({
          ok: false,
          error: 'Минимальная длина пароля 5 символов!',
          fields: ['password']
        });
      }  
      else {
        User.findOne(
          {name : na}
        ).then(user => {
           
          if (!user) {
            
            bcrypt.hash(pa, null, null, (err, hash) => {
              User.create({
                name: na,
                pass: hash
              })
              
                .then(post =>{
                 console.log(post)
                 res.json({
                    ok : true
                }) 
            })
                
                .catch(err => {
                  console.log(err);
                  res.json({
                    ok: false,
                    error: 'Ошибка, попробуйте позже!'
                  });
                });
            });
          } else {
            res.json({
              ok: false,
              error: 'Имя занято!'
            });
          }
        });
      }
    });

/////////////////////////////////////////////////
//////////////////////////////////////////////////
////////////////////////////////////////////////






/*
app.use(jwtmiddleware({
  secret : config.secret
}))
*/

app.get('/show', function (req, res)
  {
    jwt.verify(token, config.secret, function(err, decoded) 
    {
      if (err) 
      {
        console.log("I am here")
        Rtoken.findOne(   {refreshtoken : refreshToken} ).then(rtoken => 
          { if(rtoken){
            let id = rtoken.id;
            
            Rtoken.remove({refreshToken : refreshToken});
            refreshToken = uuid();
            Rtoken.create({            
              id: id,
              refreshtoken: refreshToken
            })
            token =jwt.sign({id:id, refreshtoken: refreshToken},config.secret,{expiresIn: '10000ms'});
          
            
          }
          else{
            res.json({
                ok: false,
                error: 'Acces token expired!',
                status: 401
              })
          }
        
        
        })
      }
      else{
        User.find({}).then(users => {
          res.render('show',{users: users});
        })
      }
    })
  })

    
/*
app.get('/show', function (req, res){
  {
    
      User.find({}).then(users => {
          res.render('show',{users: users});
      })
  }

}).set('Authorization',`Bearer $(authLine)`);*/
module.exports = app;

/////////////////////

 /*.then(user => {
                  console.log(user);
                  req.session.userId = user.id;
                  req.session.userLogin = user.login;
                  res.json({
                    ok: true
                  });
                }*/
