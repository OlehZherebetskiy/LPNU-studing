import { Component, OnInit } from '@angular/core';
import $ from 'node_modules/jquery'
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    $('.navbar-head').css('display','none')
    $('.sidebar').css('display','none')
  }

}
