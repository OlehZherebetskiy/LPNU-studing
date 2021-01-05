import { Component, OnInit, AfterViewInit } from '@angular/core';
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import { ProfileService } from '../profile/profile.service';
import $ from 'node_modules/jquery'
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
      this.token.verifyTokenSubs().catch(this.verifyTokenCatch())
    }
    this.profileService.getProfile().subscribe(data => { $('#username')[0].innerHTML= data.username; },this.getProfileSubError())
  }

  verifyTokenCatch() : any {
    return ()=>{this.router.navigate(['../login']);return}
  }

  getProfileSubError(): any {
    return error => { alert(error.massage)  }
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
}
