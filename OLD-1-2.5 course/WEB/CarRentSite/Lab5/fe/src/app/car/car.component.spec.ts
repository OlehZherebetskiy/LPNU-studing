import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CarComponent } from './car.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { LogInComponent } from '../log-in/log-in.component';

describe('CarComponent', () => {
  let component: CarComponent;
  let fixture: ComponentFixture<CarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CarComponent ],
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
    fixture = TestBed.createComponent(CarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create: Car component', () => {
    expect(component).toBeTruthy();
  });
  it('check on event functions: Car component', () => {
    expect(component.onDropdownLogOut()==null).toBe(true);
    expect(component.onSidebarCollapse()==null).toBe(true);
    expect(component.onSidebarTop()==null).toBe(true);
  });
  it('check promise/observ: Car component', () => {
    expect(component.getTopRentCarData()({"id":1})==null).toBe(true);
    expect(component.getTopRentCarError()({"massage":"msg"})==null).toBe(true);
  });
});
