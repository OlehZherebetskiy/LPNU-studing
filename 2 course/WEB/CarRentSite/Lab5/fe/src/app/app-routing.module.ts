import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LogInComponent } from './log-in/log-in.component';
import { LogUpComponent } from './log-up/log-up.component';
import { CarListComponent } from './car-list/car-list.component';
import { CarComponent } from './car/car.component';
import { ProfileComponent } from './profile/profile.component';
import { HomeComponent } from './home/home.component';
import { PartnersComponent } from './partners/partners.component';
import { AboutComponent } from './about/about.component';
import { ChangePassComponent } from './change-pass/change-pass.component';


const routes: Routes = [
  {
    path: 'login',
    component: LogInComponent
  },
  {
    path: 'registration',
    component: LogUpComponent
  },
  {
    path: 'change-password',
    component: ChangePassComponent
  },
  {
    path: 'carlist',
    component: CarListComponent
  },
  {
    path: 'car/:id',
    component: CarComponent
  },
  {
    path: 'profile',
    component: ProfileComponent
  },
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'partners',
    component: PartnersComponent
  },
  {
    path: 'about',
    component: AboutComponent
  },
  {
    path: '**',
    redirectTo: ''
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
