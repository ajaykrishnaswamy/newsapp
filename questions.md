# Project Clarification Questions

Below are key questions to clarify the requirements and guide development. Please provide answers inline or below each question.

---

## 1. News Sources & APIs
- Which specific news APIs or RSS feeds do you want to use for fetching news (e.g., NewsAPI, custom scrapers, direct RSS from CNN/BBC)?
- Are there any licensing or access restrictions for these sources that we should be aware of?

## Answers: 
- 

## 2. Language & Voice Support
- Which languages should be supported at launch for both news summarization and audio/video generation? Answer: English is default for launch
- Do you have a preferred TTS (text-to-speech) provider (e.g., Google Cloud, AWS Polly, Azure, ElevenLabs), or should I recommend one? Answer: AWS Polly is default for launch, as a future feature, I would like to have an option for the user to pick his own TTS provider and the API key will be provided by the user. 

## 3. User Interface
- Should the user interface be web-based, mobile, or both?Answer: Web based
- What level of customization do you want for users (e.g., can they select multiple sources, voices, and languages in one session)? Answer: I want all of the customization maximum level of customization

## 4. Audio/Video Output
- For the video generation, do you have a preferred avatar/animation technology (e.g., D-ID, Synthesia, custom animation)? 
- Should the audio/video files be downloadable, or only streamable from the app?

## 5. Storage & Caching
- Do you have a preferred cloud storage provider (e.g., AWS S3, Google Cloud Storage) for storing summaries and generated media?
- How long should cached/generated content be retained before being deleted or refreshed?

## 6. Playback & Controls
- Should playback controls (pause, resume, skip) be available for both audio and video, or just audio?
- Is there a preferred framework or library for implementing playback controls?

## 7. Cost & Usage
- Do you have a target budget for API usage and storage costs per month?
- Should there be user authentication/limits to prevent abuse or excessive usage? 