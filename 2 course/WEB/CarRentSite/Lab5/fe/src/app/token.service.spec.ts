import { TestBed } from '@angular/core/testing';

import { TokenService } from './token.service';
import { HttpClient } from '@angular/common/http';
import { HttpTestingController, HttpClientTestingModule } from '@angular/common/http/testing';
import { resolve } from 'dns';



describe('TokenService', () => {
  let service: TokenService;
  let httpTestingController: HttpTestingController;
  let httpClient: HttpClient;
  const homeUrl = 'http://127.0.0.1:8000/playlist/';

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TokenService],
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(TokenService);
    httpClient = TestBed.inject(HttpClient);
    httpTestingController = TestBed.inject(HttpTestingController);
  });

 

  it('should be created: Token service', () => {
    expect(service).toBeTruthy();
  });
  it('should return expected data about user: Token service', () => {
    expect(service.logout()==null).toBe(true);
    expect(service.getAccess()!=null).toBe(true);
    expect(service.getRefresh()!=null).toBe(true);

    expect(service.refreshToken()!=null).toBe(true);
    expect(service.verifyToken()!=null).toBe(true);

    expect(service.refreshTokenSubs()!=null).toBe(true);
    expect(service.setCookie({"access":"accessToken", "refresh":"refreshToken"})==null).toBe(true);
    expect(service.verifyTokenSubs()!=null).toBe(true);
    new Promise((resolve, reject)=>{
      expect(service.refreshTokenSubData(resolve)({"access":"accessToken", "refresh":"refreshToken"})==null).toBe(true);
      expect(service.refreshTokenSubError(reject)({"massage":"msg"})==null).toBe(true);
    }) 
    new Promise((resolve, reject)=>{
      expect(service.verifyTokenSubData(resolve)({"access":"accessToken", "refresh":"refreshToken"})==null).toBe(true);
      expect(service.verifyTokenSubError(reject)({"massage":"msg"})==null).toBe(true);
    }) 
  });

});
