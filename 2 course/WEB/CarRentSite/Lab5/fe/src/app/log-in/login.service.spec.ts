import { TestBed } from '@angular/core/testing';

import { LoginService } from './login.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { HttpClient } from '@angular/common/http';

describe('LoginService', () => {
  let service: LoginService;
  let httpTestingController: HttpTestingController;
  let httpClient: HttpClient;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [LoginService],
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(LoginService);
    httpClient = TestBed.inject(HttpClient);
    httpTestingController = TestBed.inject(HttpTestingController);
  });


  it('should be created: LogIn service', () => {
    expect(service).toBeTruthy();
  });

  describe('#Login', () => {
    

    it('should return access and refresh token: LogIn service', () => {
      service.login({
        "email": "rtws1sk@a.com",
        "password": "1234213235"
    }).subscribe(
        data => expect(data!=null).toBe(true, 'should return expected data'),
        fail
      );

    });

    
  });
});