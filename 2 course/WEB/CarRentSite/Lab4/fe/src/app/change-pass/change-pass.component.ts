import { Component, OnInit, Input } from '@angular/core';
import { ValidatorFn, FormControl, FormGroup } from '@angular/forms';
import $ from 'node_modules/jquery'
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import ValidateServ from '../services/ValidateServ';
import { ProfileService } from '../profile/profile.service';
import { getProfile } from '../profile/profileService';
import { getTopRentCar } from '../car-list/carService';
import { CarService } from '../car-list/car.service';
import { change } from './change-passService';
import { ChangeService } from './change-pass.service';

@Component({
  selector: 'app-change-pass',
  templateUrl: './change-pass.component.html',
  styleUrls: ['../log-in/log-in.component.sass','../car-list/car-list.component.sass']
})
export class ChangePassComponent implements OnInit {

  @Input() myvalidator:ValidatorFn;
  changeForm : any;
  oldPassword: FormControl;
  newPassword: FormControl;
  confirmPassword: FormControl;
  username ="";

  constructor(private api: ChangeService, private profileService :ProfileService, private token :TokenService,
    private router: Router, private carService: CarService) { }

  ngAfterViewInit(): void {
    
    $( "span" ).off();
    $('#change-btn').on('click', ()=> {
      if(!this.newPassword.errors && !this.confirmPassword.errors){
        this.change().then(()=>{
          this.router.navigate(['../carlist'])
        }).catch(error=>{
          $('#error').css('display','initial')
        });
      }
  })
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
    getProfile(this.profileService, this.token).then((data)=>{
      $('#username')[0].innerHTML= data.username 
    }).catch(error => this.router.navigate(['../login']))
    this.initFormControl()
  }

  initFormControl(): void {
    this.oldPassword =  new FormControl('', ValidateServ.validatePassword)
    this.newPassword  = new FormControl('', ValidateServ.validatePassword)
    this.confirmPassword  = new FormControl('', ValidateServ.validatePassword)

    this.changeForm = new FormGroup({
      inputGroup: new FormGroup({
        oldPassword: this.oldPassword,
        newPassword: this.newPassword,
        confirmPassword: this.confirmPassword,
      })
    })
  }

  change(): any {
    var data = {
      "oldPassword" : this.oldPassword.value,
      "newPassword": this.newPassword.value
    }
    
    return change(this.api, this.token, data, this.router)
    
  }
}
