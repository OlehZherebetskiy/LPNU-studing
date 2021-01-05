import { Component, OnInit, AfterViewInit } from '@angular/core';
import $ from 'node_modules/jquery'
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import { getProfile } from '../profile/profileService'
import { ProfileService } from '../profile/profile.service'
import { CarService } from './car.service';
import { getCarList, getTopRentCar, getCarListPar } from './carService';
@Component({
  selector: 'app-car-list',
  templateUrl: './car-list.component.html',
  styleUrls: ['./car-list.component.sass']
})
export class CarListComponent implements OnInit, AfterViewInit {

  username =""
  carlist = []

  constructor(private token :TokenService,
    private router: Router, private profileService :ProfileService, private api :CarService) { }


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
    $('.btn--filter').on('click', ()=> {
      this.carlist=[],
      getCarListPar(this.api, this.token, $('#types')[0].value, $('#brands')[0].value, $('#regions')[0].value).then((data)=>{
        this.carlist=data,
        setTimeout(() => {
          $('#car-panel-small').on('click', ()=> {
            this.router.navigate(['../car'])
          })
        }, 100); 
      }).catch(error => this.router.navigate(['../login']))
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
    getCarList(this.api, this.token).then((data)=>{
      this.carlist=data,
      setTimeout(() => {
        $('#car-panel-small').on('click', ()=> {
          this.router.navigate(['../car'])
        })
      }, 100); 
    }).catch(error => this.router.navigate(['../login']))

  }

  }


