import { TestBed } from '@angular/core/testing';

import { CarService } from './car.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { HttpClient } from '@angular/common/http';

describe('CarService', () => {
  let service: CarService;
  let httpTestingController: HttpTestingController;
  let httpClient: HttpClient;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CarService],
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(CarService);
    httpClient = TestBed.inject(HttpClient);
    httpTestingController = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpTestingController.verify();
  });

  it('should be created: Car service', () => {
    expect(service).toBeTruthy();
  });

  describe('#Car', () => {
    

    it('should return expected data about car: Car service', () => {
      service.getCar("1").subscribe(
        data => expect(data!=null).toBe(true, 'should return expected car data'),
        fail
      );

      const req = httpTestingController.expectOne('http://localhost:8000/car/1/');
      expect(req.request.method).toEqual('GET');
    });

    it('should return expected data about top rent car: Car service', () => {
        service.getTopRentCar().subscribe(
          data => expect(data!=null).toBe(true, 'should return expected car data'),
          fail
        );
  
        const req = httpTestingController.expectOne('http://localhost:8000/toprent/');
        expect(req.request.method).toEqual('GET');
      });
  });
});