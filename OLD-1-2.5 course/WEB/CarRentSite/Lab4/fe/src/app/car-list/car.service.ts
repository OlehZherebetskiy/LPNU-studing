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


  getCarList(): Observable<any> {
    const url = this.baseUrl + '/carlist/'

    return this.http.get(url, this.httpHeaders())
  }

  getCarListPar(type, brand, region): Observable<any> {
    const url = this.baseUrl + '/carlist/'+'?'+'type='+type+";brand="+brand+";region="+region

    return this.http.get(url, this.httpHeaders())
  }

  getTopRentCar(): Observable<any> {
    const url = this.baseUrl + '/toprent/'

    return this.http.get(url, this.httpHeaders())
  }

}
