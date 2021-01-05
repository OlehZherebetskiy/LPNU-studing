import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LogUpComponent } from './log-up.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { LogInComponent } from '../log-in/log-in.component';

describe('LogUpComponent', () => {
  let component: LogUpComponent;
  let fixture: ComponentFixture<LogUpComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LogUpComponent ],
      imports: [HttpClientTestingModule, RouterTestingModule.withRoutes(
        [{
          path: 'login',
          component: LogInComponent
        }]
      )]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LogUpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create: LogUp component', () => {
    expect(component).toBeTruthy();
  });
  it('check on event functions: LogUp component', () => {
    expect(component.onRegistrationBtn()==null).toBe(true);
  });
  it('check promise/observ: LogUp component', () => {
    expect(component.registerNewUser()!=null).toBe(true);
  });
});
