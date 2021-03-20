
      
      export function change(api, token,  data, router) : any {
        return   new Promise((resolve, reject) => {
          api.change(data).subscribe(
            data => {
              router.navigate(['/carlist']); 
              resolve(data)
            },
            error => {
              console.log(error)
                console.log(error.error.code=="token_not_valid")
                if(error.error.code=="token_not_valid"){
                  token.refreshTokenSubs().then( newToken => { api.change(data).subscribe(data => {router.navigate(['/carlist']); resolve(data)})})
                  .catch(error=>reject(error ))
                }
            }
          )
        })
      }