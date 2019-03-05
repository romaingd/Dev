import React from 'react';


const RESET_VALUES = {
  id: '',
  category: '',
  price: '',
  stocked: false,
  name: ''
};


class ProductForm extends React.Component {
  constructor(props) {
    super(props);
    this.handleSave = this.handleSave.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.validateName = this.validateName.bind(this);
    this.state = {
      product: Object.assign({}, RESET_VALUES),
      error: false
    };
  }

  UNSAFE_componentWillReceiveProps(nextProps) {
    let product = nextProps.formProduct;
    if (product.id) {
      this.setState({product: product});
    } else {
      this.setState({
        product: Object.assign({}, RESET_VALUES)
      });
    }
  }

  handleSave(e) {
    // If the 'name' field is empty on submission, display an error message
    // and don't save the product
    if (this.state.product['name'] === '') {
      this.setState({error: true});
      e.preventDefault();
      return false;
    }
    this.props.onSave(this.state.product);
    // Reset the input field to blank
    this.setState({
      product: Object.assign({}, RESET_VALUES)
    });
    // Prevent default submission that would trigger an HTTP Post
    e.preventDefault();
  }

  handleChange(e) {
    const target = e.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    if (name === 'name') {
      this.validateName(e);
    }

    this.setState((prevState) => {
      prevState.product[name] = value;
      return {product: prevState.product}
    });
  }

  validateName(e) {
    if (e.target.value === '') {
      this.setState({error: true});
    } else {
      this.setState({error: false});
    }
  }

  render() {
    let errorMessage;
    if (this.state.error) {
      errorMessage = <p style={{color: 'red'}}>Please enter a name</p>;
    } else {
      errorMessage = ''
    }
    return(
      <form>
        <h3>Enter a new product</h3>
        {errorMessage}
        <p>
          <label>
            Name
            <br/>
            <input
              type="text"
              name="name"
              onChange={this.handleChange}
              value={this.state.product.name}
            />
          </label>
        </p>

        <p>
          <label>
            Category
            <br/>
            <input
              type="text"
              name="category"
              onChange={this.handleChange}
              value={this.state.product.category}
            />
          </label>
        </p>

        <p>
          <label>
            Price
            <br/>
            <input
              type="text"
              name="price"
              onChange={this.handleChange}
              value={this.state.product.price}
            />
          </label>
        </p>

        <p>
          <label>
            <input
              type="checkbox"
              name="stocked"
              onChange={this.handleChange}
              value={this.state.product.stocked}
            />
            In stock?
          </label>
        </p>
        <input type="submit" value="Save" onClick={this.handleSave}/>
      </form>
    );
  }
}

export default ProductForm;