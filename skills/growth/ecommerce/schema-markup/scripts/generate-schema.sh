#!/bin/bash

# Helper script to generate common Schema.org JSON-LD templates
# Usage: ./generate-schema.sh <type>

TYPE=$1

if [[ -z "$TYPE" ]]; then
  echo "Usage: $0 <type>"
  echo "Types: article, faq, product, organization"
  exit 1
fi

case $TYPE in
  article)
    cat <<EOF
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Headline",
  "image": ["https://example.com/image.jpg"],
  "datePublished": "$(date -I)",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  }
}
EOF
    ;;
  faq)
    cat <<EOF
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is the question?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "This is the answer."
    }
  }]
}
EOF
    ;;
  product)
    cat <<EOF
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": ["https://example.com/product.jpg"],
  "description": "Product Description",
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/product",
    "priceCurrency": "USD",
    "price": "99.99",
    "availability": "https://schema.org/InStock"
  }
}
EOF
    ;;
  organization)
    cat <<EOF
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Organization Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png"
}
EOF
    ;;
  *)
    echo "Invalid type: $TYPE. Use article, faq, product, or organization."
    exit 1
    ;;
esac
