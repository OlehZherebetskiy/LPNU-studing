import { Component, OnInit, AfterViewInit, Input } from '@angular/core';
import $ from 'node_modules/jquery'
import { ValidatorFn, FormControl, FormGroup } from '@angular/forms';
import { LoginService } from '../log-in/login.service';
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import ValidateServ from '../services/ValidateServ';
import { login } from './loginService';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.sass'],
  providers: [LoginService]
})
export class LogInComponent implements OnInit, AfterViewInit {

  @Input() myvalidator:ValidatorFn;
  loginForm : any;
  username: FormControl;
  email: FormControl;
  password: FormControl;
  confirmPassword: FormControl;

  constructor(private api: LoginService, private token :TokenService,
    private router: Router) { }

  ngAfterViewInit(): void {
    
    
    $('#login-btn').on('click', ()=> {
      if(!this.email.errors && !this.password.errors){
        this.login().then(()=>{
          $('.navbar-head').css('display','flex')
          $('.sidebar').css('display','initial')
          this.router.navigate(['../carlist'])
        }).catch(error=>{
          $('#error').css('display','initial')
        });
      }
  })
  }

  ngOnInit(): void {
    if (this.token.getAccess() && this.token.getRefresh()){
      this.token.verifyTokenSubs().then(()=>{
        $('.navbar-head').css('display','flex')
        $('.sidebar').css('display','initial')
        this.router.navigate(['../carlist'])
      })
    }
    this.initFormControl()
    $('.navbar-head').css('display','none')
    $('.sidebar').css('display','none')
  }

  initFormControl(): void {
    this.email =  new FormControl('', ValidateServ.validateEmail)
    this.password  = new FormControl('', ValidateServ.validatePassword)

    this.loginForm = new FormGroup({
      inputGroup: new FormGroup({
        email: this.email,
        password: this.password
      })
    })
  }

  login(): any {
    var data = {
      "email" : this.email.value,
      "password": this.password.value
    }
    
    return login(this.api, this.token, data, this.router)
    
  }
}
