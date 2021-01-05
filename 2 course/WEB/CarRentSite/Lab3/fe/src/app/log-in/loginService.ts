
      export function login(api, token,  data, router) : any {
        return new Promise((resolve, reject) => {
          api.login(data).subscribe(
          data => {
            token.setCookie(data)
            router.navigate(['/carlist']);
            resolve();
          },
          error => {
            console.log(error)
            reject(error);
          }
        )})
      }