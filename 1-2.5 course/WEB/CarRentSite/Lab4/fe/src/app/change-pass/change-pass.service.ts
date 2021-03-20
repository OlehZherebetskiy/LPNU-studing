import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { Observable } from 'rxjs';
import { TokenService } from '../token.service';

@Injectable({
  providedIn: 'root'
})
export class ChangeService {
  baseUrl = 'http://localhost:8000'

  httpHeaders = ()=>{ return {headers : new HttpHeaders({'Content-Type': 'application/json',
  'Authorization':'Bearer '+ this.tokenService.getAccess()})}}

  constructor(private http: HttpClient, private tokenService: TokenService) { }


  change(data): Observable<any> {
    const body = {newPassword: data.newPassword, oldPassword: data.oldPassword}
    const url = this.baseUrl + '/user/'

    return this.http.patch(url, body, this.httpHeaders())
  }

}
