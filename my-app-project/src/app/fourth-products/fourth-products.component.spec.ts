import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FourthProductsComponent } from './fourth-products.component';

describe('FourthProductsComponent', () => {
  let component: FourthProductsComponent;
  let fixture: ComponentFixture<FourthProductsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FourthProductsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FourthProductsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
