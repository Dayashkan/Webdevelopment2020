import { Component, OnInit } from '@angular/core';

import { products1, products2, products3, products4, productCategory, Product, product} from '../products';

@Component({
  selector: 'app-product-category',
  templateUrl: './product-category.component.html',
  styleUrls: ['./product-category.component.css']
})



export class ProductCategoryComponent implements OnInit {

  constructor() { }

  category = productCategory;
  products1 = products1;
  products2 = products2;
  products3 = products3;
  products4 = products4;

  selectCategory(selectedCategory): void {
    for ( let i = 0 ; i < productCategory.length ; i++){
      productCategory[i] = selectedCategory[i];
    }
  }

  ngOnInit(): void {

  //   this.category = [{
  //     categoryName:'First Category',
  //     categoryID:1,
  //     products:products1
  //   },
  //   {
  //     categoryName:'Second Category',
  //     categoryID:2,
  //     products:products2
  //   },
  //   {
  //     categoryName:'Third Category',
  //     categoryID:3,
  //     products:products3
  //   },
  //   {
  //     categoryName:'Fourth Category',
  //     categoryID:4,
  //     products:products4
  //   }
  // ]

  }

}


// export interface Category{
//   categoryName:string;
//   categoryID:number;
//   products:Product[];
// }
