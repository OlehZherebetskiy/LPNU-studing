import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfileComponent } from './profile.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AboutComponent } from '../about/about.component';
import { LogInComponent } from '../log-in/log-in.component';

describe('ProfileComponent', () => {
  let component: ProfileComponent;
  let fixture: ComponentFixture<ProfileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProfileComponent ],
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
    fixture = TestBed.createComponent(ProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create: Profile component', () => {
    expect(component).toBeTruthy();
  });
  it('check on event functions: Profile component', () => {
    expect(component.onDropdownLogOut()==null).toBe(true);
    expect(component.onSidebarCollapse()==null).toBe(true);
    expect(component.onSidebarTop()==null).toBe(true);
  });
  it('check promise/observ: Profile component', () => {
    expect(component.getTopRentCarData()({"id":1})==null).toBe(true);
    expect(component.getTopRentCarError()({"massage":"msg"})==null).toBe(true);
  });
});
