import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
key = os.environ["AZURE_LANGUAGE_KEY"]

client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

from azure.ai.textanalytics import TextAnalyticsClient
from azure.identity import DefaultAzureCredential

client = TextAnalyticsClient(
    endpoint=os.environ["AZURE_LANGUAGE_ENDPOINT"],
    credential=DefaultAzureCredential()
)

documents = [
    "I had a wonderful trip to Seattle last week!",
    "The food was terrible and the service was slow."
]

result = client.analyze_sentiment(documents, show_opinion_mining=True)

for doc in result:
    if not doc.is_error:
        print(f"Sentiment: {doc.sentiment}")
        print(f"Scores: pos={doc.confidence_scores.positive:.2f}, "
              f"neg={doc.confidence_scores.negative:.2f}, "
              f"neu={doc.confidence_scores.neutral:.2f}")

        # Opinion mining (aspect-based sentiment)
        for sentence in doc.sentences:
            for opinion in sentence.mined_opinions:
                target = opinion.target
                print(f"  Target: '{target.text}' - {target.sentiment}")
                for assessment in opinion.assessments:
                    print(f"    Assessment: '{assessment.text}' - {assessment.sentiment}")

documents = ["Microsoft was founded by Bill Gates and Paul Allen in Albuquerque."]

result = client.recognize_entities(documents)

for doc in result:
    if not doc.is_error:
        for entity in doc.entities:
            print(f"Entity: {entity.text}")
            print(f"  Category: {entity.category}")
            print(f"  Subcategory: {entity.subcategory}")
            print(f"  Confidence: {entity.confidence_score:.2f}")

documents = ["My SSN is 123-45-6789 and my email is john@example.com"]

result = client.recognize_pii_entities(documents)

for doc in result:
    if not doc.is_error:
        print(f"Redacted: {doc.redacted_text}")
        for entity in doc.entities:
            print(f"PII: {entity.text} ({entity.category})")

documents = ["Azure AI provides powerful machine learning capabilities for developers."]

result = client.extract_key_phrases(documents)

for doc in result:
    if not doc.is_error:
        print(f"Key phrases: {doc.key_phrases}")

documents = ["Ce document est en francais.", "This is written in English."]

result = client.detect_language(documents)

for doc in result:
    if not doc.is_error:
        print(f"Language: {doc.primary_language.name} ({doc.primary_language.iso6391_name})")
        print(f"Confidence: {doc.primary_language.confidence_score:.2f}")

documents = ["Patient has diabetes and was prescribed metformin 500mg twice daily."]

poller = client.begin_analyze_healthcare_entities(documents)
result = poller.result()

for doc in result:
    if not doc.is_error:
        for entity in doc.entities:
            print(f"Entity: {entity.text}")
            print(f"  Category: {entity.category}")
            print(f"  Normalized: {entity.normalized_text}")

            # Entity links (UMLS, etc.)
            for link in entity.data_sources:
                print(f"  Link: {link.name} - {link.entity_id}")

from azure.ai.textanalytics import (
    RecognizeEntitiesAction,
    ExtractKeyPhrasesAction,
    AnalyzeSentimentAction
)

documents = ["Microsoft announced new Azure AI features at Build conference."]

poller = client.begin_analyze_actions(
    documents,
    actions=[
        RecognizeEntitiesAction(),
        ExtractKeyPhrasesAction(),
        AnalyzeSentimentAction()
    ]
)

results = poller.result()
for doc_results in results:
    for result in doc_results:
        if result.kind == "EntityRecognition":
            print(f"Entities: {[e.text for e in result.entities]}")
        elif result.kind == "KeyPhraseExtraction":
            print(f"Key phrases: {result.key_phrases}")
        elif result.kind == "SentimentAnalysis":
            print(f"Sentiment: {result.sentiment}")

from azure.ai.textanalytics.aio import TextAnalyticsClient
from azure.identity.aio import DefaultAzureCredential

async def analyze():
    async with TextAnalyticsClient(
        endpoint=endpoint,
        credential=DefaultAzureCredential()
    ) as client:
        result = await client.analyze_sentiment(documents)
        # Process results...
