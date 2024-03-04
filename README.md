# FastAPI Text Summarization Service

This FastAPI service provides endpoints for text summarization and compression using pre-trained models from Hugging Face and custom algorithms.

## Dependencies
**FastAPI**: Handles HTTP requests and responses. <br>
**Transformers**: Provides pre-trained models for text summarization.<br>
**Pydantic**: Defines the request and response models.

See requirements.txt for the library versioning needed.

## Usage

*Running locally:*

1. Clone this repository
2. Create a virtual environment and install requirements.txt 
3. Run the application in your terminal
```
uvicorn src.app:app
```
4. You can either use the examples below or you can use 
```
python test.py
```
<br>

*Running using Docker:*

1. Clone this repository
2. In your terminal, run 
```
make build
```
1. Wait a minute till this is up and running. Check out the log files in the docker container by running
```
make logs
``` 
1. Then, you can either use the examples below or you can use 
```
python test.py
``` 

## Endpoints

### Summarize Text

- **Endpoint**: `/summarize/`
- **Method**: POST
- **Request Body**:
  - `text`: The text to be summarized.
  - `summary_length`: The desired length of the summary.
- **Response**: Returns a JSON object containing the summarized text.

#### Example
Send a POST request to `/summarize/` with the following JSON body:

```json
{
  "text": "This is a sample input text. It can be any lengthy document or article. This service will summarize it for you.",
  "summary_length": 50
}
```
What an example request looks like:

```bash
curl -X 'POST' \
  'http://localhost:8000/summarize/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "This is a sample input text. It can be any lengthy document or article. This service will summarize it for you.",
  "summary_length": 50
}'
```

### Compress Summary

- **Endpoint**: `/compress_summary/`
- **Method**: POST
- **Request Body**:
  - `summary`: The summary string to be compressed.
- **Response**: Returns a JSON object containing the compressed summary string.

#### Example
Send a POST request to /compress_summary/ with the following JSON body:

```json
{
  "summary": "This is a compressed summary."
}
```

What an example request looks like:
```bash
curl -X 'POST' \
  'http://localhost:8000/compress_summary/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "summary": "This is a compressed summary."
}'
```

## TODOs
* Build additional unit tests
* Decrease build time of the docker image
* Create a docker-composer.yaml file 
* Integrate load testing using Locust to evaluate system performance
* Integrate this into AWS' container registry and kubernetes cluster using Github CICD
* Set up monitoring with Cloudwatch or Datadog

## Contributors

[Sarah Floris](https://github.com/sdf94)

