
      export function getCar(api, token, id) : any {
        return   new Promise((resolve, reject) => {
          api.getCar(id).subscribe(
            data => { 
              resolve(data)
            },
            error => {
              console.log(error)
                console.log(error.error.code=="token_not_valid")
                if(error.error.code=="token_not_valid"){
                  token.refreshTokenSubs().then( newToken => { api.getCar(id).subscribe(data => {resolve(data)})})
                  .catch(error=>reject(error ))
                }
            }
          )
        })
      }

      export function getTopRentCar(api, token) : any {
        return   new Promise((resolve, reject) => {
          api.getTopRentCar().subscribe(
            data => { 
              resolve(data)
            },
            error => {
              console.log(error)
                console.log(error.error.code=="token_not_valid")
                if(error.error.code=="token_not_valid"){
                  token.refreshTokenSubs().then( newToken => { api.getTopRentCar().subscribe(data => {resolve(data)})})
                  .catch(error=>reject(error ))
                }
            }
          )
        })
      }