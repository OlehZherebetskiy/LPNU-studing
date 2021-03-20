import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  baseUrl = 'http://localhost:8000'

  httpHeaders = { headers : new HttpHeaders({'Content-Type': 'application/json'})}

  constructor(private http: HttpClient, private cookieService: CookieService) { }


  login(data): Observable<any> {
    const body = {email: data.email, password: data.password}
    const url = this.baseUrl + '/login/token/'

    return this.http.post(url, body, this.httpHeaders)
  }

}
