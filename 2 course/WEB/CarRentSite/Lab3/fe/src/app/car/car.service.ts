import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { Observable } from 'rxjs';
import { TokenService } from '../token.service';

@Injectable({
  providedIn: 'root'
})
export class CarService {
  baseUrl = 'http://localhost:8000'

  httpHeaders = ()=>{ return {headers : new HttpHeaders({'Content-Type': 'application/json',
  'Authorization':'Bearer '+ this.tokenService.getAccess()})}}

  constructor(private http: HttpClient, private tokenService: TokenService) { }


  getCar(id): Observable<any> {
    const url = this.baseUrl + '/car/'+id+'/'

    return this.http.get(url, this.httpHeaders())
  }

  getTopRentCar(): Observable<any> {
    const url = this.baseUrl + '/toprent/'

    return this.http.get(url, this.httpHeaders())
  }

}
