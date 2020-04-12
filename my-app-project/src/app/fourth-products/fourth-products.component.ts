import { Component, OnInit } from '@angular/core';
import {product, productCategory, products4, Product} from '../products';
import { ProductServiceService } from '../product-service.service';

@Component({
  selector: 'app-fourth-products',
  templateUrl: './fourth-products.component.html',
  styleUrls: ['./fourth-products.component.css']
})
export class FourthProductsComponent implements OnInit {

  constructor(private productService: ProductServiceService) { }

  products = productCategory;

  // tslint:disable-next-line:no-shadowed-variable
  share(product: Product): void {
    window.alert(`The ${product.name} has been shared!`);
  }

  // tslint:disable-next-line:no-shadowed-variable
  onNotify(product: Product) {
    alert(`You will be notified when the  ${product.name} goes on sale`);
  }

  ngOnInit(): void {
  }

  selectProduct(selectedProduct): void {
    product.name = selectedProduct.name;
    product.price = selectedProduct.price;
    product.description = selectedProduct.description;
    product.rating = selectedProduct.rating;
    product.link = selectedProduct.link;
    product.img = selectedProduct.img;
    product.categoryID = selectedProduct.categoryID;
    product.productID = selectedProduct.productID;
  }

  getProductCategory(): void {
    // tslint:disable-next-line:no-shadowed-variable
    this.productService.getProductCategory().subscribe(productCategory => this.products = productCategory);
  }

}
