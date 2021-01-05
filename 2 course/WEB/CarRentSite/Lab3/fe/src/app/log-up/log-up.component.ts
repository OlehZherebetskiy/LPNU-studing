import { Component, OnInit, AfterViewInit, Input } from '@angular/core';
import $ from 'node_modules/jquery'
import  {registerNewUser}  from './registrationService'
import { FormGroup, FormControl, ValidatorFn } from '@angular/forms';
import  ValidateServ from '../services/ValidateServ' ;
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import { RegistrationService } from './registration.service';


@Component({
  selector: 'app-log-up',
  templateUrl: './log-up.component.html',
  styleUrls: ['./log-up.component.sass'],
  providers: [RegistrationService]
})
export class LogUpComponent implements OnInit, AfterViewInit {


  @Input() myvalidator:ValidatorFn;
  
  registrationForm : any;
  username: FormControl;
  email: FormControl;
  password: FormControl;
  confirmPassword: FormControl;

  constructor(private api: RegistrationService, private token :TokenService,
    private router: Router) { }
  ngAfterViewInit(): void {
    $('#registration-btn').on('click', ()=> {
      if(!this.email.errors && !this.password.errors && !this.confirmPassword.errors && !this.username.errors && this.password.value==this.confirmPassword.value){
        this.registerNewUser().then(()=>{
          this.router.navigate(['../login'])
        }).catch(error=>{
          $('#error').css('display','initial')
        });
      }
    })
  }

  ngOnInit(): void {
    $('.navbar-head').css('display','none')
    $('.sidebar').css('display','none')
    this.initFormControl();
  }

  initFormControl(): void {
    $('#username')[0].innerHTML= new FormControl('', ValidateServ.validateUsername)
    this.email =  new FormControl('', ValidateServ.validateEmail)
    this.password  = new FormControl('', ValidateServ.validatePassword)
    this.confirmPassword = new FormControl('', ValidateServ.validatePassword)

    this.registrationForm = new FormGroup({
      inputGroup: new FormGroup({
        username: this.username,
        email: this.email,
        password: this.password,
        confirmPassword: this.confirmPassword
      })
    })
  }

  registerNewUser(): any {
    var data = {
      "username" : this.username.value,
      "email" : this.email.value,
      "password": this.password.value
    }
    return registerNewUser(this.api, this.token, data, this.router)
  }

}
