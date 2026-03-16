import os
import requests

def transcribe_audio(audio_file_path: str, language: str = "en-US") -> dict:
    """Transcribe short audio file (max 60 seconds) using REST API."""
    region = os.environ["AZURE_SPEECH_REGION"]
    api_key = os.environ["AZURE_SPEECH_KEY"]

    url = f"https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1"

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000",
        "Accept": "application/json"
    }

    params = {
        "language": language,
        "format": "detailed"  # or "simple"
    }

    with open(audio_file_path, "rb") as audio_file:
        response = requests.post(url, headers=headers, params=params, data=audio_file)

    response.raise_for_status()
    return response.json()

# Usage
result = transcribe_audio("audio.wav", "en-US")
print(result["DisplayText"])


# WAV PCM 16kHz
"Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000"

# OGG OPUS
"Content-Type": "audio/ogg; codecs=opus"


params = {"language": "en-US", "format": "simple"}


params = {"language": "en-US", "format": "detailed"}


import os
import requests

def transcribe_chunked(audio_file_path: str, language: str = "en-US") -> dict:
    """Stream audio in chunks for lower latency."""
    region = os.environ["AZURE_SPEECH_REGION"]
    api_key = os.environ["AZURE_SPEECH_KEY"]

    url = f"https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1"

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000",
        "Accept": "application/json",
        "Transfer-Encoding": "chunked",
        "Expect": "100-continue"
    }

    params = {"language": language, "format": "detailed"}

    def generate_chunks(file_path: str, chunk_size: int = 1024):
        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                yield chunk

    response = requests.post(
        url,
        headers=headers,
        params=params,
        data=generate_chunks(audio_file_path)
    )

    response.raise_for_status()
    return response.json()


headers = {
    "Ocp-Apim-Subscription-Key": os.environ["AZURE_SPEECH_KEY"]
}


import requests
import os

def get_access_token() -> str:
    """Get access token from the token endpoint."""
    region = os.environ["AZURE_SPEECH_REGION"]
    api_key = os.environ["AZURE_SPEECH_KEY"]

    token_url = f"https://{region}.api.cognitive.microsoft.com/sts/v1.0/issueToken"

    response = requests.post(
        token_url,
        headers={
            "Ocp-Apim-Subscription-Key": api_key,
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "0"
        }
    )
    response.raise_for_status()
    return response.text

# Use token in requests (valid for 10 minutes)
token = get_access_token()
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000",
    "Accept": "application/json"
}


# Mask profanity with asterisks (default)
params = {"language": "en-US", "profanity": "masked"}

# Remove profanity entirely
params = {"language": "en-US", "profanity": "removed"}

# Include profanity as-is
params = {"language": "en-US", "profanity": "raw"}


import requests

def transcribe_with_error_handling(audio_path: str, language: str = "en-US") -> dict | None:
    """Transcribe with proper error handling."""
    region = os.environ["AZURE_SPEECH_REGION"]
    api_key = os.environ["AZURE_SPEECH_KEY"]

    url = f"https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1"

    try:
        with open(audio_path, "rb") as audio_file:
            response = requests.post(
                url,
                headers={
                    "Ocp-Apim-Subscription-Key": api_key,
                    "Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000",
                    "Accept": "application/json"
                },
                params={"language": language, "format": "detailed"},
                data=audio_file
            )

        if response.status_code == 200:
            result = response.json()
            if result.get("RecognitionStatus") == "Success":
                return result
            else:
                print(f"Recognition failed: {result.get('RecognitionStatus')}")
                return None
        elif response.status_code == 400:
            print(f"Bad request: Check language code or audio format")
        elif response.status_code == 401:
            print(f"Unauthorized: Check API key or token")
        elif response.status_code == 403:
            print(f"Forbidden: Missing authorization header")
        else:
            print(f"Error {response.status_code}: {response.text}")

        return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


import os
import aiohttp
import asyncio

async def transcribe_async(audio_file_path: str, language: str = "en-US") -> dict:
    """Async version using aiohttp."""
    region = os.environ["AZURE_SPEECH_REGION"]
    api_key = os.environ["AZURE_SPEECH_KEY"]

    url = f"https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1"

    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000",
        "Accept": "application/json"
    }

    params = {"language": language, "format": "detailed"}

    async with aiohttp.ClientSession() as session:
        with open(audio_file_path, "rb") as f:
            audio_data = f.read()

        async with session.post(url, headers=headers, params=params, data=audio_data) as response:
            response.raise_for_status()
            return await response.json()

# Usage
result = asyncio.run(transcribe_async("audio.wav", "en-US"))
print(result["DisplayText"])
