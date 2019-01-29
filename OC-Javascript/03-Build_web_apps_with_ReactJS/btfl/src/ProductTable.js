import React from 'react';
import ProductRow from './ProductRow.js';
import SortableColumnHeader from './SortableColumnHeader.js';

class ProductTable extends React.Component {
  constructor(props) {
    super(props);
    this.sortByKeyAndOrder = this.sortByKeyAndOrder.bind(this);
    this.handleDestroy = this.handleDestroy.bind(this);
    this.handleEdit = this.handleEdit.bind(this);
    this.handleSort = this.handleSort.bind(this);
    this.state = {
      sort: {
        column: 'name',
        direction: 'desc'
      },
      products: props.products
    };

  }

  sortByKeyAndOrder(objectA, objectB) {
    // Sorting function: return -1, 0 or 1 depending on the ordering
    // of the quantities to compare
    let isDesc = this.state.sort.direction === 'desc' ? 1 : -1;
    let [a, b] = [
      objectA[this.state.sort.column],
      objectB[this.state.sort.column]
    ];
    if (this.state.sort.column === 'price') {
      [a, b] = [a, b].map((value) => (
        parseFloat(value.replace(/[^\d\.]/g, ''), 10)
      ));
    }
    if (a > b) {
      return 1 * isDesc;
    } else if (a < b) {
      return -1 * isDesc;
    } else{
      return 0;
    }
  }

  sortProducts() {
    let productsAsArray = Object.keys(this.props.products).map((pid) => (
      this.props.products[pid]
    ));
    return productsAsArray.sort(this.sortByKeyAndOrder);
  }

  handleSort(column, direction) {
    console.log(column + direction);
    this.setState({
      sort: {
        column: column,
        direction: direction
      }
    });
  }

  handleDestroy(productId) {
    this.props.onDestroy(productId);
  }

  handleEdit(productId) {
    this.props.onEdit(productId);
  }

  render() {
    let rows = [];
    this.sortProducts().forEach((product) => {
      if (
        product.name.indexOf(this.props.filterText) === -1 ||
        (!product.stocked && this.props.inStockOnly)
      ) {
        return;
      } else {
        rows.push(
          <ProductRow
            product={product}
            key={product.id}
            onDestroy={this.handleDestroy}
            onEdit={this.handleEdit}
          />
        );
      }
    });

    return(
      <div>
        <table>
          <thead>
            <tr>
              <SortableColumnHeader
                currentSort={this.state.sort}
                column="name"
                onSort={this.handleSort}
              ></SortableColumnHeader>
              <SortableColumnHeader
                currentSort={this.state.sort}
                column="price"
                onSort={this.handleSort}
              ></SortableColumnHeader>
            </tr>
          </thead>
          <tbody>
            {rows}
          </tbody>
        </table>
      </div>
    );
  }
}

export default ProductTable;