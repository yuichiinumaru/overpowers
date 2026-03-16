#!/bin/bash

# Salesforce LWC Component Scaffolder

if [ -z "$1" ]; then
    echo "Usage: $0 <componentName>"
    exit 1
fi

COMPONENT_NAME=$1
mkdir -p "$COMPONENT_NAME"

# Create HTML file
cat <<EOF > "$COMPONENT_NAME/$COMPONENT_NAME.html"
<template>
    <lightning-card title="$COMPONENT_NAME">
        <div class="slds-p-around_medium">
            Hello from $COMPONENT_NAME!
        </div>
    </lightning-card>
</template>
EOF

# Create JS file
cat <<EOF > "$COMPONENT_NAME/$COMPONENT_NAME.js"
import { LightningElement, api, wire } from 'lwc';

export default class ${COMPONENT_NAME^} extends LightningElement {
    @api recordId;
}
EOF

# Create meta.xml file
cat <<EOF > "$COMPONENT_NAME/$COMPONENT_NAME.js-meta.xml"
<?xml version="1.0" encoding="UTF-8"?>
<LightningComponentBundle xmlns="http://soap.sforce.com/2006/04/metadata">
    <apiVersion>58.0</apiVersion>
    <isExposed>true</isExposed>
    <targets>
        <target>lightning__AppPage</target>
        <target>lightning__RecordPage</target>
        <target>lightning__HomePage</target>
    </targets>
</LightningComponentBundle>
EOF

echo "LWC component $COMPONENT_NAME scaffolded successfully."
