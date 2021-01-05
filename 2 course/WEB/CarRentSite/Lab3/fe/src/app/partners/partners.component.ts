import { Component, OnInit, AfterViewInit } from '@angular/core';
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import { ProfileService } from '../profile/profile.service';
import $ from 'node_modules/jquery'
import { getProfile } from '../profile/profileService';
import { getTopRentCar } from '../car-list/carService';
import { CarService } from '../car-list/car.service';

@Component({
  selector: 'app-partners',
  templateUrl: './partners.component.html',
  styleUrls: ['../car/car.component.sass','./partners.component.scss']
})
export class PartnersComponent implements OnInit, AfterViewInit {

  username =""

  constructor(private token :TokenService,
    private router: Router, private profileService :ProfileService, private carService: CarService) { }

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
      getTopRentCar(this.carService, this.token).then(data=> {this.router.navigate(['../car/'+data.id])}).catch(error => this.router.navigate(['../login']))
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
}
