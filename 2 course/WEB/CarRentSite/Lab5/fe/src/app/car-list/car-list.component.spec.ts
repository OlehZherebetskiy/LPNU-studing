import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CarListComponent } from './car-list.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { LogInComponent } from '../log-in/log-in.component';

describe('CarListComponent', () => {
  let component: CarListComponent;
  let fixture: ComponentFixture<CarListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CarListComponent ],
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
    fixture = TestBed.createComponent(CarListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create: CarList component', () => {
    expect(component).toBeTruthy();
  });
  it('check on event functions: CarList component', () => {
    expect(component.onDropdownLogOut()==null).toBe(true);
    expect(component.onSidebarCollapse()==null).toBe(true);
    expect(component.onSidebarTop()==null).toBe(true);
  });
  it('check promise/observ: CarList component', () => {
    expect(component.getTopRentCarError()({"massage":"msg"})==null).toBe(true);
    expect(component.getTopRentCarData()({"id":1})==null).toBe(true);
    expect(component.getCarListError()({"massage":"msg"})==null).toBe(true);
  });
});
