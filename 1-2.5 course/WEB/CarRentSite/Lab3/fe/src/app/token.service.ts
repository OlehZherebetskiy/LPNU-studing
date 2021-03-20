import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CookieService } from 'ngx-cookie-service';
import jwt_decode from 'jwt-decode'
import { rejects } from 'assert';
@Injectable({
  providedIn: 'root'
})
export class TokenService {

  baseUrl = 'http://localhost:8000';

  constructor(private http: HttpClient, private cookieService: CookieService) { }

  refreshToken(): Observable<any> {
    const body = { refresh: this.cookieService.get('refresh') };
    const url = this.baseUrl + '/login/refresh/';

    const httpHeadersWithToken = { headers : new HttpHeaders({'Content-Type': 'application/json'})};
    return this.http.post(url, body, httpHeadersWithToken);
  }

  verifyToken(): Observable<any> {
    const body = { token: this.cookieService.get('refresh') };
    const url = this.baseUrl + '/login/verify/';

    const httpHeadersWithToken = { headers : new HttpHeaders({'Content-Type': 'application/json'})};
    return this.http.post(url, body, httpHeadersWithToken);
  }

  logout(): any {
    this.cookieService.delete('access');
    this.cookieService.delete('refresh');
  }

  refreshTokenSubs(): any {
    return new Promise((resolve, reject) => {
      this.refreshToken().subscribe(
        data => {
          this.setCookie({access: data.access, refresh: data.refresh});
          resolve();
        },
        error => {
          console.log(error)
          reject(error);
        }
      );
    });
  }

  verifyTokenSubs(): any {
    return new Promise((resolve, reject) => {
      this.verifyToken().subscribe(
        data => {
          resolve();
        },
        error => {
          console.log(error);
          reject(error)
        }
      );
    });
  }

  setCookie(data): void {
    this.cookieService.set('access', data.access);
    if (data.refresh){
      this.cookieService.set('refresh', data.refresh);
    }
  }

  getAccess(): any {
    return this.cookieService.get('access');
  }
  getRefresh(): any {
    return this.cookieService.get('refresh');
  }
}
