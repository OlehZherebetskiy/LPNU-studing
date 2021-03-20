import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PartnersComponent } from './partners.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { Router } from '@angular/router';
import { LogInComponent } from '../log-in/log-in.component';

describe('PartnersComponent', () => {
  let component: PartnersComponent;
  let fixture: ComponentFixture<PartnersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PartnersComponent ],
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
    fixture = TestBed.createComponent(PartnersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create: Partners component', () => {
    expect(component).toBeTruthy();
  });
  it('check on event functions: Partners component', () => {
    expect(component.onDropdownLogOut()==null).toBe(true);
    expect(component.onSidebarCollapse()==null).toBe(true);
    expect(component.onSidebarTop()==null).toBe(true);
  });
  it('check promise/observ: Partners component', () => {
    expect(component.verifyTokenCatch()()==null).toBe(true);
    expect(component.getProfileSubError()({"massage":"msg"})==null).toBe(true);
    expect(component.getTopRentCarData()({"id":1})==null).toBe(true);
    expect(component.getTopRentCarError()({"massage":"msg"})==null).toBe(true);
  });
});
