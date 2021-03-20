
      export function getProfile(api, token) : any {
        return   new Promise((resolve, reject) => {
          api.getProfile().subscribe(
            data => { 
              resolve(data)
            },
            error => {
              console.log(error)
                console.log(error.error.code=="token_not_valid")
                if(error.error.code=="token_not_valid"){
                  token.refreshTokenSubs().then( newToken => { api.getProfile().subscribe(data => {resolve(data)})})
                  .catch(error=>reject(error ))
                }
            }
          )
        })
      }