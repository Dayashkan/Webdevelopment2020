import { Injectable } from '@angular/core';
import {product , productCategory, Product} from './products';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductServiceService {

  constructor() { }

  getProduct():Observable<Product>{
    return of(product);
  }

  getProductCategory():Observable<Product[]>{
    return of(productCategory);
  }
}
