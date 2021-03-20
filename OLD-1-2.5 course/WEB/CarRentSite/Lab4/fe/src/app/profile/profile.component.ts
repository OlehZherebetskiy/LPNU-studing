import { Component, OnInit, AfterViewInit } from '@angular/core';
import $ from 'node_modules/jquery'
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import { getProfile } from './profileService'
import { ProfileService } from './profile.service'
import { getTopRentCar } from '../car-list/carService';
import { CarService } from '../car-list/car.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.sass']
})
export class ProfileComponent implements OnInit, AfterViewInit {

  email =""
  username =""

  constructor(private token :TokenService,
    private router: Router, private api: ProfileService, private carService: CarService) { }


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
    getProfile(this.api, this.token).then( data=>{
      this.email = data.email;
      this.username=data.username;
      $('#username')[0].innerHTML= data.username;
    }).catch( error => this.router.navigate(['../login']));

  }
  }


