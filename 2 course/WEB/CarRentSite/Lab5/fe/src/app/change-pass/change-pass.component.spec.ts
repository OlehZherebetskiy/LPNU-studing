import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChangePassComponent } from './change-pass.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { LogInComponent } from '../log-in/log-in.component';

describe('ChangePassComponent', () => {
  let component: ChangePassComponent;
  let fixture: ComponentFixture<ChangePassComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChangePassComponent ],
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
    fixture = TestBed.createComponent(ChangePassComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create: ChangePass component', () => {
    expect(component).toBeTruthy();
  });
  it('check on event functions: ChangePass component', () => {
    expect(component.onDropdownLogOut()==null).toBe(true);
    expect(component.onSidebarCollapse()==null).toBe(true);
    expect(component.onSidebarTop()==null).toBe(true);
  });
  it('check promise/observ: ChangePass component', () => {
    expect(component.change()!=null).toBe(true);
    expect(component.changeError()({"massage":"msg"})==null).toBe(true);
    expect(component.getTopRentCarError()({"massage":"msg"})==null).toBe(true);
    expect(component.getTopRentCarData()({"id":1})==null).toBe(true);
  });
});
