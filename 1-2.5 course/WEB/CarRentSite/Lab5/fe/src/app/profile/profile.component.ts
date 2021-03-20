import { Component, OnInit, AfterViewInit } from '@angular/core';
import $ from 'node_modules/jquery'
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import { ProfileService } from './profile.service'
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
    if (!this.token.getRefresh()){
      this.router.navigate(['../login'])
      return
    } else {
      this.token.verifyTokenSubs().catch(()=>{
        this.router.navigate(['../login'])
        return
      })
    }
    this.api.getProfile().subscribe(data => { $('#username')[0].innerHTML= data.username; },error => { alert(error.massage)  })
  }
  }


