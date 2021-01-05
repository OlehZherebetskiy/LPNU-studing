import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AboutComponent } from './about.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { LogInComponent } from '../log-in/log-in.component';

describe('AboutComponent', () => {
  let component: AboutComponent;
  let fixture: ComponentFixture<AboutComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AboutComponent ],
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
    fixture = TestBed.createComponent(AboutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create: About component', () => {
    expect(component).toBeTruthy();
  });
  it('check on event functions: About component', () => {
    expect(component.onDropdownLogOut()==null).toBe(true);
    expect(component.onSidebarCollapse()==null).toBe(true);
    expect(component.onSidebarTop()==null).toBe(true);
  });
  it('check promise/observ: About component', () => {
    expect(component.verifyTokenCatch()()==null).toBe(true);
    expect(component.getProfileSubError()({"massage":"msg"})==null).toBe(true);
    expect(component.getTopRentCarData()({"id":1})==null).toBe(true);
    expect(component.getTopRentCarError()({"massage":"msg"})==null).toBe(true);
  });
});
