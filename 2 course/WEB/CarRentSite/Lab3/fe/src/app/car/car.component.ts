import { Component, OnInit, AfterViewInit } from '@angular/core';
import $ from 'node_modules/jquery'
import { TokenService } from '../token.service';
import { Router, ActivatedRoute } from '@angular/router';
import { ProfileService } from '../profile/profile.service';
import { getProfile } from '../profile/profileService';
import { CarService } from './car.service';
import { getCar } from './carService';
import { getTopRentCar } from '../car-list/carService';

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
    $( "span" ).off();
    $('.dropdown-head-panel').width($('.head-log-panel').width()+4)
    $('#sidebarCollapse').on('click', ()=> {
      $('#sidebar').toggleClass('active');
      $(this).toggleClass('active');
    });
    $('#dropdown-log-out').on('click', ()=> {
      this.token.logout();
      setTimeout(() => {
        this.router.navigate(['../login'])
      }, 500);
  })

  
  $('#dropdown-change-password').on('click', ()=> {
    this.router.navigate(['../change-password'])
  })
  $('#dropdown-profile').on('click', ()=> {
    this.router.navigate(['../profile'])
  })
  $('#sidebar-about').on('click', ()=> {
    $('#sidebar').toggleClass('active');
      $(this).toggleClass('active');
    this.router.navigate(['../about'])
  })
  $('#sidebar-top').on('click', ()=> {
      $('#sidebar').toggleClass('active');
      $(this).toggleClass('active');
      getTopRentCar(this.api, this.token).then(data=> {this.router.navigate(['../car/'+data.id])}).catch(error => this.router.navigate(['../login']))
  })
  $('#sidebar-partners').on('click', ()=> {
    $('#sidebar').toggleClass('active');
      $(this).toggleClass('active');
    this.router.navigate(['../partners'])
  })
  $('#sidebar-all-cars').on('click', ()=> {
    $('#sidebar').toggleClass('active');
      $(this).toggleClass('active');
      this.router.navigate(['../carlist'])
  })
  $('#sidebar-profile').on('click', ()=> {
      $('#sidebar').toggleClass('active');
      $(this).toggleClass('active');
      this.router.navigate(['../profile'])
  })
      
      
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
    getProfile(this.profileService, this.token).then((data)=>{
      $('#username')[0].innerHTML= data.username 
    }).catch(error => this.router.navigate(['../login']))
    getCar(this.api, this.token, this.id).then((data)=>{
      this.car=data
    }).catch(error => this.router.navigate(['../login']))
  }
  }


