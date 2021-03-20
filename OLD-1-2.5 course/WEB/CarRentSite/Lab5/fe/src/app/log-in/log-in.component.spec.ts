import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LogInComponent } from './log-in.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';

describe('LogInComponent', () => {
  let component: LogInComponent;
  let fixture: ComponentFixture<LogInComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LogInComponent ],
      imports: [HttpClientTestingModule, RouterTestingModule]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LogInComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create: LogIn component', () => {
    expect(component).toBeTruthy();
  });
  it('check promise/observ: LogIn component', async () => {
    expect(component.login()!=null).toBe(true);
    component.login().then(data=>{expect(data!=null).toBe(true);})
    component.login().catch(error=>{expect(error!=null).toBe(true);})
    expect(component.onloginBtn()==null).toBe(true);
    expect(component.loginThen()()==null).toBe(true);
    expect(component.loginCatch()()==null).toBe(true);
  });
});
