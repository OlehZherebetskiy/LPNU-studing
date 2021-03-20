import { TestBed } from '@angular/core/testing';

import { ProfileService } from './profile.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { HttpClient } from '@angular/common/http';

describe('ProfileService', () => {
  let service: ProfileService;
  let httpTestingController: HttpTestingController;
  let httpClient: HttpClient;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ProfileService],
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(ProfileService);
    httpClient = TestBed.inject(HttpClient);
    httpTestingController = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpTestingController.verify();
  });

  it('should be created: Profile service', () => {
    expect(service).toBeTruthy();
  });

  describe('#Profile', () => {
    

    it('should return expected data about user: Profile service', () => {
      service.getProfile().subscribe(
        data => expect(data!=null).toBe(true, 'should return expected data'),
        fail
      );

      const req = httpTestingController.expectOne('http://localhost:8000/user/');
      expect(req.request.method).toEqual('GET');
    });
  });
});