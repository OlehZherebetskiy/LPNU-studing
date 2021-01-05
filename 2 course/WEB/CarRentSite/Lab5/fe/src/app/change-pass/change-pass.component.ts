import { Component, OnInit, Input } from '@angular/core';
import { ValidatorFn, FormControl, FormGroup } from '@angular/forms';
import $ from 'node_modules/jquery'
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import ValidateServ from '../services/ValidateServ';
import { ProfileService } from '../profile/profile.service';
import { CarService } from '../car-list/car.service';
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
      $('.dropdown-head-panel').width($('.head-log-panel').width()+4)
      
    
    }
  
    onSidebarCollapse(): void {
      $('#sidebar').toggleClass('active');
    }
    onDropdownLogOut(): void {
      this.token.logout();
        setTimeout(() => {
          this.router.navigate(['../login'])
        }, 500);
    }
    onSidebarTop(): void {
      $('#sidebar').toggleClass('active');
      this.carService.getTopRentCar().subscribe(
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
    this.initFormControl()
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
    
    return new Promise((resolve, reject) => {
      this.api.change(data).subscribe(
      data => {
        this.router.navigate(['/carlist']); 
        resolve(data)
      },
      this.changeError()
    )})
    
  }

  changeError(): any {
    return error => {
      alert(error.massage)
    }
  }
  
}
