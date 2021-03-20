
      export function getCarList(api, token) : any {
        return   new Promise((resolve, reject) => {
          api.getCarList().subscribe(
            data => { 
              resolve(data)
            },
            error => {
              console.log(error)
                console.log(error.error.code=="token_not_valid")
                if(error.error.code=="token_not_valid"){
                  token.refreshTokenSubs().then( newToken => { api.getCarList().subscribe(data => {resolve(data)})})
                  .catch(error=>reject(error ))
                }
            }
          )
        })
      }

      export function getCarListPar(api, token, type, brand, region) : any {
        return   new Promise((resolve, reject) => {
          api.getCarListPar(type, brand, region).subscribe(
            data => { 
              resolve(data)
            },
            error => {
              console.log(error)
                console.log(error.error.code=="token_not_valid")
                if(error.error.code=="token_not_valid"){
                  token.refreshTokenSubs().then( newToken => { api.getCarListPar(type, brand, region).subscribe(data => {resolve(data)})})
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