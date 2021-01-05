import { TestBed, async } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AppComponent } from './app.component';
import { LogInComponent } from './log-in/log-in.component';
import { LogUpComponent } from './log-up/log-up.component';
import { ChangePassComponent } from './change-pass/change-pass.component';
import { CarListComponent } from './car-list/car-list.component';
import { CarComponent } from './car/car.component';
import { ProfileComponent } from './profile/profile.component';
import { HomeComponent } from './home/home.component';
import { PartnersComponent } from './partners/partners.component';
import { AboutComponent } from './about/about.component';

describe('AppComponent', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [
        RouterTestingModule.withRoutes(
          [{
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
          }]
        )
      ],
      declarations: [
        AppComponent
      ],
    }).compileComponents();
  }));

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title 'app'`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app.title).toEqual('app');
  });
});
