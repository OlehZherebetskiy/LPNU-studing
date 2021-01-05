import { TestBed } from '@angular/core/testing';

import { RegistrationService } from './registration.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { HttpClient } from '@angular/common/http';

describe('RegistrationService', () => {
  let service: RegistrationService;
  let httpTestingController: HttpTestingController;
  let httpClient: HttpClient;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [RegistrationService],
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(RegistrationService);
    httpClient = TestBed.inject(HttpClient);
    httpTestingController = TestBed.inject(HttpTestingController);
  });

 

  it('should be created: LogUp service', () => {
    expect(service).toBeTruthy();
  });

  describe('#LogUp', () => {
    

    it('should return access and refresh token: LogIn service', () => {
      service.registerNewUser({
        "username": "oleh",
        "email": "rtws1sk@a.com",
        "password": "1234213235"
    }).subscribe(
        data => expect(data!=null).toBe(true, 'should return expected data'),
        fail
      );
    });
  });
});