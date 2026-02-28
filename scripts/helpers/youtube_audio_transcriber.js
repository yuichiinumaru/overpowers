const { execSync } = require('child_process');
const fs = require('fs');

async function downloadAndTranscribe(url) {
    console.log(`Processing URL: ${url}`);

    // Extract video ID
    let videoId = url;
    if (url.includes('v=')) {
        videoId = url.split('v=')[1].split('&')[0];
    } else if (url.includes('youtu.be/')) {
        videoId = url.split('youtu.be/')[1].split('?')[0];
    }

    const audioPath = `temp_${videoId}.m4a`;
    const transcriptPath = `temp_${videoId}_transcript.txt`;

    try {
        console.log("Downloading audio via yt-dlp...");
        execSync(`yt-dlp -f bestaudio -o "${audioPath}" "${url}"`, { stdio: 'inherit' });

        console.log("Transcribing audio via Whisper...");
        const pyScript = `
import whisper
import sys

def transcribe(audio_path, output_path):
    print("Loading whisper model...")
    model = whisper.load_model("base")
    print("Transcribing...")
    result = model.transcribe(audio_path)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"Transcript saved to {output_path}")

if __name__ == "__main__":
    transcribe(sys.argv[1], sys.argv[2])
`;
        fs.writeFileSync('temp_whisper_run.py', pyScript);
        execSync(`python3 temp_whisper_run.py "${audioPath}" "${transcriptPath}"`, { stdio: 'inherit' });

        // Clean up temp files
        if (fs.existsSync(audioPath)) fs.unlinkSync(audioPath);
        if (fs.existsSync('temp_whisper_run.py')) fs.unlinkSync('temp_whisper_run.py');

        console.log(`Success! Transcript available at ${transcriptPath}`);
        return true;

    } catch (e) {
        console.error("Error during download or transcription:", e.message);
        return false;
    }
}

// Support being called directly from CLI
if (require.main === module) {
    const url = process.argv[2];
    if (url) {
        downloadAndTranscribe(url).then(success => {
            if (!success) process.exit(1);
        });
    } else {
        console.log("Usage: node youtube_audio_transcriber.js <youtube_url>");
    }
}

module.exports = { downloadAndTranscribe };
