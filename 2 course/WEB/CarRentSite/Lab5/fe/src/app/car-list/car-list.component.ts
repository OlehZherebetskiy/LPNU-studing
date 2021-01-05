import { Component, OnInit, AfterViewInit } from '@angular/core';
import $ from 'node_modules/jquery'
import { TokenService } from '../token.service';
import { Router } from '@angular/router';
import { ProfileService } from '../profile/profile.service'
import { CarService } from './car.service';
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
      this.api.getTopRentCar().subscribe(
       this.getTopRentCarData(),
        this.getTopRentCarError()
      )
    }

    getTopRentCarError(): any {
      return error => {
        alert(error.massage)
      }
    }

    getTopRentCarData(): any {
      return  data => { 
        this.router.navigate(['../car/'+data.id])
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
    this.profileService.getProfile().subscribe(data => { $('#username')[0].innerHTML= data.username; },error => { alert(error.massage)  })
    
    this.api.getCarList().subscribe(
      data => { 
        this.carlist=data
        $('#car-panel-small').on('click', ()=> {
          this.router.navigate(['../car'])
        })
      },
      this.getCarListError()
    )
  }

  getCarListError(): any {
    return error => {
      alert(error.massage)
    }
  }

  }


