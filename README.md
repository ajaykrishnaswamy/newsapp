# NewsApp Audio Pipeline

## Overview
NewsApp is a serverless application that fetches, summarizes, and generates audio files for top news stories, storing them in S3 and making them available via a simple web UI. The system is designed for scalability, cost-efficiency, and extensibility, leveraging AWS managed services.

---

## System Design: AWS Architecture

```mermaid
graph TD;
  A[User (Web UI)] -->|GET /audio/list| B(API Gateway)
  B -->|Lambda Proxy| C[Lambda: NewsAppAudioList]
  C -->|List & Sign URLs| D[S3: NewsAudioBucket]
  C --> E[Return signed URLs]
  E --> A

  subgraph News Generation
    F[Lambda: NewsAppAudioGenerator] -->|GROQ API| G[GROQ]
    F -->|PutObject| D
  end
```

- **Frontend**: React app (Vite) fetches audio file list from API Gateway.
- **API Gateway**: Exposes REST endpoints (`/audio/list`, `/audio`). Handles CORS and routes requests to Lambda.
- **Lambda (NewsAppAudioList)**: Lists audio files in S3 and returns signed URLs for secure playback/download.
- **Lambda (NewsAppAudioGenerator)**: (Optional) Calls GROQ API to generate news audio and uploads to S3.
- **S3 (NewsAudioBucket)**: Stores generated audio files.
- **IAM**: Lambda roles have least-privilege access to S3 and CloudWatch Logs.

---

## Features
- Fetch and summarize top news stories (via GROQ API)
- Generate and store audio files in S3
- Secure, temporary access to audio files via signed URLs
- Simple React-based web UI for playback
- Fully serverless and scalable

---

## Setup & Running Locally

### 1. **Clone the Repository**
```sh
git clone https://github.com/ajaykrishnaswamy/newsapp.git
cd newsapp
```

### 2. **Install Frontend Dependencies**
```sh
cd src
npm install
```

### 3. **Set Up Environment Variables**
Create a `.env` file in the project root (not committed to git):
```
VITE_API_GATEWAY_URL=https://<your-api-id>.execute-api.<region>.amazonaws.com/prod/audio
GROQ_API_KEY=sk-...   # (for Lambda, not needed for frontend)
```

### 4. **Deploy AWS Infrastructure**
- Edit `groq-lambda-docdb.yml` as needed.
- Deploy with:
```sh
aws cloudformation deploy --template-file groq-lambda-docdb.yml --stack-name newsapp-audio-stack --capabilities CAPABILITY_NAMED_IAM
```

### 5. **Run the Frontend Locally**
```sh
npm run dev
```
Visit [http://localhost:5173](http://localhost:5173)

---

## Usage
- Upload audio files to the S3 bucket (or use the Lambda to generate them).
- Visit the web UI to see and play available audio files.
- The UI fetches `/audio/list` from API Gateway, which returns signed URLs for each file.

---

## Environment Variables
- `VITE_API_GATEWAY_URL`: The base URL for your API Gateway `/audio` endpoint (used by the frontend).
- `GROQ_API_KEY`: Your GROQ API key (used by Lambda, not committed to git).

---

## Security & Best Practices
- **Never commit secrets** (API keys, .env files) to git.
- S3 bucket is private; access is only via signed URLs.
- Lambda roles are least-privilege (S3:PutObject, S3:GetObject, S3:ListBucket).
- CORS is enabled for API Gateway endpoints.

---

## Custom Domain (Optional)
- You can map your API Gateway or frontend to a custom domain (e.g., via Route53 or Vercel).
- Update DNS records as needed and ensure HTTPS is enabled.

---

## Troubleshooting
- **CORS errors**: Ensure API Gateway and Lambda return correct CORS headers and redeploy after changes.
- **AccessDenied on S3**: Ensure Lambda role has `s3:GetObject` and `s3:ListBucket` permissions.
- **No audio plays**: Check S3 file format, permissions, and that the presigned URL is valid.

---

## License
MIT
