const customerData = [
  {
    name: "John Doe",
    purchases: [
      { product: "Laptop", price: 1200 },
      { product: "Mouse", price: 25 },
    ],
  },
  {
    name: "Jane Smith",
    purchases: [
      { product: "Smartphone", price: 800 },
      { product: "Headphones", price: 50 },
    ],
  },
  {
    name: "Sumit",
    purchases: null,
  },
  {
    name: null,
    purchases: [
      { product: "Smartphone", price: 800 },
      { product: "Headphones", price: 50 },
    ],
  },
];

/* {
        customer:"",
        product:"",
        price:""
}*/

let res = [];

for (let index = 0; index < customerData.length; index++) {
  if (customerData[index].purchases == null) {
    index += 1
  }
  for (let j = 0; j < customerData[index].purchases.length; j++) {
    let info = {
      customer: customerData[index].name,
      purchases: customerData[index].purchases[j].product,
      price: customerData[index].purchases[j].price,
    };
    res.push(info);
  }
}

console.log(res);
