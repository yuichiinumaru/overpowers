import DocumentIntelligence from "@azure-rest/ai-document-intelligence";
import { DefaultAzureCredential } from "@azure/identity";

const client = DocumentIntelligence(
  process.env.DOCUMENT_INTELLIGENCE_ENDPOINT!,
  new DefaultAzureCredential()
);

import DocumentIntelligence from "@azure-rest/ai-document-intelligence";

const client = DocumentIntelligence(
  process.env.DOCUMENT_INTELLIGENCE_ENDPOINT!,
  { key: process.env.DOCUMENT_INTELLIGENCE_API_KEY! }
);

import DocumentIntelligence, {
  isUnexpected,
  getLongRunningPoller,
  AnalyzeOperationOutput
} from "@azure-rest/ai-document-intelligence";

const initialResponse = await client
  .path("/documentModels/{modelId}:analyze", "prebuilt-layout")
  .post({
    contentType: "application/json",
    body: {
      urlSource: "https://example.com/document.pdf"
    },
    queryParameters: { locale: "en-US" }
  });

if (isUnexpected(initialResponse)) {
  throw initialResponse.body.error;
}

const poller = getLongRunningPoller(client, initialResponse);
const result = (await poller.pollUntilDone()).body as AnalyzeOperationOutput;

console.log("Pages:", result.analyzeResult?.pages?.length);
console.log("Tables:", result.analyzeResult?.tables?.length);

import { readFile } from "node:fs/promises";

const fileBuffer = await readFile("./document.pdf");
const base64Source = fileBuffer.toString("base64");

const initialResponse = await client
  .path("/documentModels/{modelId}:analyze", "prebuilt-invoice")
  .post({
    contentType: "application/json",
    body: { base64Source }
  });

if (isUnexpected(initialResponse)) {
  throw initialResponse.body.error;
}

const poller = getLongRunningPoller(client, initialResponse);
const result = (await poller.pollUntilDone()).body as AnalyzeOperationOutput;

const initialResponse = await client
  .path("/documentModels/{modelId}:analyze", "prebuilt-invoice")
  .post({
    contentType: "application/json",
    body: { urlSource: invoiceUrl }
  });

if (isUnexpected(initialResponse)) {
  throw initialResponse.body.error;
}

const poller = getLongRunningPoller(client, initialResponse);
const result = (await poller.pollUntilDone()).body as AnalyzeOperationOutput;

const invoice = result.analyzeResult?.documents?.[0];
if (invoice) {
  console.log("Vendor:", invoice.fields?.VendorName?.content);
  console.log("Total:", invoice.fields?.InvoiceTotal?.content);
  console.log("Due Date:", invoice.fields?.DueDate?.content);
}

const initialResponse = await client
  .path("/documentModels/{modelId}:analyze", "prebuilt-receipt")
  .post({
    contentType: "application/json",
    body: { urlSource: receiptUrl }
  });

const poller = getLongRunningPoller(client, initialResponse);
const result = (await poller.pollUntilDone()).body as AnalyzeOperationOutput;

const receipt = result.analyzeResult?.documents?.[0];
if (receipt) {
  console.log("Merchant:", receipt.fields?.MerchantName?.content);
  console.log("Total:", receipt.fields?.Total?.content);

  for (const item of receipt.fields?.Items?.values || []) {
    console.log("Item:", item.properties?.Description?.content);
    console.log("Price:", item.properties?.TotalPrice?.content);
  }
}

import DocumentIntelligence, { isUnexpected, paginate } from "@azure-rest/ai-document-intelligence";

const response = await client.path("/documentModels").get();

if (isUnexpected(response)) {
  throw response.body.error;
}

for await (const model of paginate(client, response)) {
  console.log(model.modelId);
}

const initialResponse = await client.path("/documentModels:build").post({
  body: {
    modelId: "my-custom-model",
    description: "Custom model for purchase orders",
    buildMode: "template",  // or "neural"
    azureBlobSource: {
      containerUrl: process.env.TRAINING_CONTAINER_SAS_URL!,
      prefix: "training-data/"
    }
  }
});

if (isUnexpected(initialResponse)) {
  throw initialResponse.body.error;
}

const poller = getLongRunningPoller(client, initialResponse);
const result = await poller.pollUntilDone();
console.log("Model built:", result.body);

import { DocumentClassifierBuildOperationDetailsOutput } from "@azure-rest/ai-document-intelligence";

const containerSasUrl = process.env.TRAINING_CONTAINER_SAS_URL!;

const initialResponse = await client.path("/documentClassifiers:build").post({
  body: {
    classifierId: "my-classifier",
    description: "Invoice vs Receipt classifier",
    docTypes: {
      invoices: {
        azureBlobSource: { containerUrl: containerSasUrl, prefix: "invoices/" }
      },
      receipts: {
        azureBlobSource: { containerUrl: containerSasUrl, prefix: "receipts/" }
      }
    }
  }
});

if (isUnexpected(initialResponse)) {
  throw initialResponse.body.error;
}

const poller = getLongRunningPoller(client, initialResponse);
const result = (await poller.pollUntilDone()).body as DocumentClassifierBuildOperationDetailsOutput;
console.log("Classifier:", result.result?.classifierId);

const initialResponse = await client
  .path("/documentClassifiers/{classifierId}:analyze", "my-classifier")
  .post({
    contentType: "application/json",
    body: { urlSource: documentUrl },
    queryParameters: { split: "auto" }
  });

if (isUnexpected(initialResponse)) {
  throw initialResponse.body.error;
}

const poller = getLongRunningPoller(client, initialResponse);
const result = await poller.pollUntilDone();
console.log("Classification:", result.body.analyzeResult?.documents);

const response = await client.path("/info").get();

if (isUnexpected(response)) {
  throw response.body.error;
}

console.log("Custom model limit:", response.body.customDocumentModels.limit);
console.log("Custom model count:", response.body.customDocumentModels.count);

import DocumentIntelligence, {
  isUnexpected,
  getLongRunningPoller,
  AnalyzeOperationOutput
} from "@azure-rest/ai-document-intelligence";

// 1. Start operation
const initialResponse = await client
  .path("/documentModels/{modelId}:analyze", "prebuilt-layout")
  .post({ contentType: "application/json", body: { urlSource } });

// 2. Check for errors
if (isUnexpected(initialResponse)) {
  throw initialResponse.body.error;
}

// 3. Create poller
const poller = getLongRunningPoller(client, initialResponse);

// 4. Optional: Monitor progress
poller.onProgress((state) => {
  console.log("Status:", state.status);
});

// 5. Wait for completion
const result = (await poller.pollUntilDone()).body as AnalyzeOperationOutput;

import DocumentIntelligence, {
  isUnexpected,
  getLongRunningPoller,
  paginate,
  parseResultIdFromResponse,
  AnalyzeOperationOutput,
  DocumentClassifierBuildOperationDetailsOutput
} from "@azure-rest/ai-document-intelligence";
