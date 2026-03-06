#!/bin/bash

# Helper script to generate Shopify GraphQL queries
# Usage: ./generate-shopify-query.sh <type> <limit>

TYPE=$1
LIMIT=${2:-10}

if [[ -z "$TYPE" ]]; then
  echo "Usage: $0 <type> [limit]"
  echo "Types: products, orders, customers"
  exit 1
fi

case $TYPE in
  products)
    cat <<EOF
{
  products(first: $LIMIT) {
    edges {
      node {
        id
        title
        handle
        status
        variants(first: 5) {
          edges {
            node {
              id
              title
              price
              inventoryQuantity
            }
          }
        }
      }
    }
  }
}
EOF
    ;;
  orders)
    cat <<EOF
{
  orders(first: $LIMIT) {
    edges {
      node {
        id
        name
        createdAt
        totalPriceSet {
          shopMoney {
            amount
            currencyCode
          }
        }
        displayFinancialStatus
        displayFulfillmentStatus
      }
    }
  }
}
EOF
    ;;
  customers)
    cat <<EOF
{
  customers(first: $LIMIT) {
    edges {
      node {
        id
        firstName
        lastName
        email
        ordersCount
        totalSpent
      }
    }
  }
}
EOF
    ;;
  *)
    echo "Invalid type: $TYPE."
    exit 1
    ;;
esac
