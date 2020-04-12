import { Component, OnInit } from '@angular/core';

import {product , Product} from '../products';

import { ProductServiceService } from '../product-service.service';

@Component({
  selector: 'app-product-info',
  templateUrl: './product-info.component.html',
  styleUrls: ['./product-info.component.css']
})
export class ProductInfoComponent implements OnInit {
  product = product;

  constructor(private productService:ProductServiceService) { }

  share(product: Product):void {
    window.alert(`The ${product.name} has been shared!`);
  }

  onNotify(product: Product){
    alert(`You will be notified when the  ${product.name} goes on sale`)
  }

  getProduct():void{
    this.productService.getProduct().subscribe(product=>this.product=product);
  }

  ngOnInit(): void {
    this.getProduct();
  }

}
