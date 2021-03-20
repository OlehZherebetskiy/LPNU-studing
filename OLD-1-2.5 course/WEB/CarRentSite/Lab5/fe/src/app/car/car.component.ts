import { Component, OnInit, AfterViewInit } from '@angular/core';
import $ from 'node_modules/jquery'
import { TokenService } from '../token.service';
import { Router, ActivatedRoute } from '@angular/router';
import { ProfileService } from '../profile/profile.service';
import { CarService } from './car.service';

@Component({
  selector: 'app-car',
  templateUrl: './car.component.html',
  styleUrls: ['./car.component.sass']
})
export class CarComponent implements OnInit, AfterViewInit {

  username =""
  car ={"id": 2, "type": "\u041c\u043e\u0442\u043e", "brand": "\u042f\u043c\u0430\u0445\u0430", "model": "x-max", "region": "\u041b\u044c\u0432\u0456\u0432", "year": "2018", "price": "2000", "phone": "+38097043567", "engine": "1 \u043b", "color": "\u0447\u043e\u0440\u043d\u0438\u0439", "mark": "5", "url": "https://cdn1.riastatic.com/photosnew/auto/photo/yamaha_x-max-250__323490321fx.webp", "about": ""}
  id = "";

  constructor(private token :TokenService,
    private router: Router, private route: ActivatedRoute, private profileService :ProfileService, private api :CarService) {
      this.id = this.route.snapshot.paramMap.get("id")
     }

     ngAfterViewInit(): void {
      $('.dropdown-head-panel').width($('.head-log-panel').width()+4)
    }
  
    onSidebarCollapse(): void {
      $('#sidebar').toggleClass('active');
    }
    onDropdownLogOut(): void {
      this.token.logout();
          this.router.navigate(['../login'])
    }
    onSidebarTop(): void {
      $('#sidebar').toggleClass('active');

      this.api.getTopRentCar().subscribe(
        this.getTopRentCarData(),
        this.getTopRentCarError()
      )
    }

    getTopRentCarData(): any {
      return data => { 
        this.router.navigate(['../car/'+data.id])
      }
    }

    getTopRentCarError(): any {
      return error => {
        alert(error.massage)
      }
    }


  ngOnInit(): void {
    if (!this.token.getRefresh()){
      this.router.navigate(['../login'])
      return
    } else {
      this.token.verifyTokenSubs().catch(()=>{
        this.router.navigate(['../login'])
        return
      })
    }
    this.profileService.getProfile().subscribe(data => { $('#username')[0].innerHTML= data.username; },error => { alert(error.massage)  })

    this.api.getCar(this.id).subscribe(data => { this.car=data}, error => { alert(error.massage) } )
  }
  }


