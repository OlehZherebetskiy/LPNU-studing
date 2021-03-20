import { TestBed } from '@angular/core/testing';

import { CarService } from './car.service';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { HttpClient } from '@angular/common/http';
import { CarlistModel } from '../CarlistModel'

describe('HomeService', () => {
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


  it('should be created: CarList service', () => {
    expect(service).toBeTruthy();
  });

  describe('#CarList', () => {
    
    var compare = [
      {
          "id": 1,
          "type": "1",
          "brand": "Lada",
          "model": "Веста",
          "region": "Lviv",
          "year": "2020",
          "price": "1000",
          "phone": "+38097043567",
          "engine": "2.2 л",
          "color": "чорний",
          "mark": "4",
          "url": "https://cdn.riastatic.com/photosnewr/auto/new_auto_storage/lada_vesta__477124-620x465x70.webp",
          "about": ""
      },
      {
          "id": 2,
          "type": "2",
          "brand": "BMW",
          "model": "x-max",
          "region": "Lviv",
          "year": "2018",
          "price": "2000",
          "phone": "+38097043567",
          "engine": "1 л",
          "color": "чорний",
          "mark": "5",
          "url": "https://cdn1.riastatic.com/photosnew/auto/photo/yamaha_x-max-250__323490321fx.webp",
          "about": ""
      },
      {
          "id": 4,
          "type": "1",
          "brand": "Honda",
          "model": "Scorpio",
          "region": "Lviv",
          "year": "1994",
          "price": "500",
          "phone": "+380970434567",
          "engine": "0.2 л",
          "color": "синій",
          "mark": "3",
          "url": "https://cdn4.riastatic.com/photosnew/auto/photo/ford_scorpio__333041744fx.webp",
          "about": "Комфорт Бортовий  компютер • Запуск  кнопкою Мультимедіа Система навігації  GPS • CD\r\n© AUTO.RIA.com™"
      },
      {
          "id": 5,
          "type": "3",
          "brand": "Audi",
          "model": "y-max",
          "region": "Ukraine",
          "year": "1999",
          "price": "100",
          "phone": "+380972232123",
          "engine": "1.5 л",
          "color": "голубий",
          "mark": "4",
          "url": "https://cdn0.riastatic.com/photosnew/auto/photo/audi_a6__324099450fx.webp",
          "about": "Комфортний автомобіль"
      }
  ]
    it('should return expected list of cars: CarList service', () => {
      service.getCarList().subscribe(
        data => expect(data==compare).toBe(true, 'should return expected lists'),
        fail
      );

      const req = httpTestingController.expectOne('http://localhost:8000/carlist/');
      expect(req.request.method).toEqual('GET');
    });
    let expectedData: CarlistModel[];

    beforeEach(() => {
      expectedData = [
        {
            id: 1,
            type: "1",
            brand: "Lada",
            model: "Веста",
            region: "Lviv",
            year: "2020",
            price: "1000",
            phone: "+38097043567",
            engine: "2.2 л",
            color: "чорний",
            mark: "4",
            url: "https://cdn.riastatic.com/photosnewr/auto/new_auto_storage/lada_vesta__477124-620x465x70.webp",
            about: ""
        }
    ] as CarlistModel[];
    });
    it('should return expected list of filtered cars: CarList service', () => {
        service.getCarListPar(1,0,1).subscribe(
          data => expect(data).toEqual(expectedData, 'should return expected lists'),
          fail
        );
      });
  });
});