import os
from azure.ai.translation.document import DocumentTranslationClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["AZURE_DOCUMENT_TRANSLATION_ENDPOINT"]
key = os.environ["AZURE_DOCUMENT_TRANSLATION_KEY"]

client = DocumentTranslationClient(endpoint, AzureKeyCredential(key))


from azure.ai.translation.document import DocumentTranslationClient
from azure.identity import DefaultAzureCredential

client = DocumentTranslationClient(
    endpoint=os.environ["AZURE_DOCUMENT_TRANSLATION_ENDPOINT"],
    credential=DefaultAzureCredential()
)


from azure.ai.translation.document import DocumentTranslationInput, TranslationTarget

source_url = os.environ["AZURE_SOURCE_CONTAINER_URL"]
target_url = os.environ["AZURE_TARGET_CONTAINER_URL"]

# Start translation job
poller = client.begin_translation(
    inputs=[
        DocumentTranslationInput(
            source_url=source_url,
            targets=[
                TranslationTarget(
                    target_url=target_url,
                    language="es"  # Translate to Spanish
                )
            ]
        )
    ]
)

# Wait for completion
result = poller.result()

print(f"Status: {poller.status()}")
print(f"Documents translated: {poller.details.documents_succeeded_count}")
print(f"Documents failed: {poller.details.documents_failed_count}")


poller = client.begin_translation(
    inputs=[
        DocumentTranslationInput(
            source_url=source_url,
            targets=[
                TranslationTarget(target_url=target_url_es, language="es"),
                TranslationTarget(target_url=target_url_fr, language="fr"),
                TranslationTarget(target_url=target_url_de, language="de")
            ]
        )
    ]
)


from azure.ai.translation.document import SingleDocumentTranslationClient

single_client = SingleDocumentTranslationClient(endpoint, AzureKeyCredential(key))

with open("document.docx", "rb") as f:
    document_content = f.read()

result = single_client.translate(
    body=document_content,
    target_language="es",
    content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)

# Save translated document
with open("document_es.docx", "wb") as f:
    f.write(result)


# Get all translation operations
operations = client.list_translation_statuses()

for op in operations:
    print(f"Operation ID: {op.id}")
    print(f"Status: {op.status}")
    print(f"Created: {op.created_on}")
    print(f"Total documents: {op.documents_total_count}")
    print(f"Succeeded: {op.documents_succeeded_count}")
    print(f"Failed: {op.documents_failed_count}")


# Get status of individual documents in a job
operation_id = poller.id
document_statuses = client.list_document_statuses(operation_id)

for doc in document_statuses:
    print(f"Document: {doc.source_document_url}")
    print(f"  Status: {doc.status}")
    print(f"  Translated to: {doc.translated_to}")
    if doc.error:
        print(f"  Error: {doc.error.message}")


# Cancel a running translation
client.cancel_translation(operation_id)


from azure.ai.translation.document import TranslationGlossary

poller = client.begin_translation(
    inputs=[
        DocumentTranslationInput(
            source_url=source_url,
            targets=[
                TranslationTarget(
                    target_url=target_url,
                    language="es",
                    glossaries=[
                        TranslationGlossary(
                            glossary_url="https://<storage>.blob.core.windows.net/glossary/terms.csv?<sas>",
                            file_format="csv"
                        )
                    ]
                )
            ]
        )
    ]
)


# Get supported formats
formats = client.get_supported_document_formats()

for fmt in formats:
    print(f"Format: {fmt.format}")
    print(f"  Extensions: {fmt.file_extensions}")
    print(f"  Content types: {fmt.content_types}")


# Get supported languages
languages = client.get_supported_languages()

for lang in languages:
    print(f"Language: {lang.name} ({lang.code})")


from azure.ai.translation.document.aio import DocumentTranslationClient
from azure.identity.aio import DefaultAzureCredential

async def translate_documents():
    async with DocumentTranslationClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential()
    ) as client:
        poller = await client.begin_translation(inputs=[...])
        result = await poller.result()
