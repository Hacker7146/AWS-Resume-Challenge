# AWS-Resume-Challenge

This repository implements the AWS Cloud Resume Challenge with:

- Resume written in HTML and styled with CSS (`/frontend`)
- Visitor counter in JavaScript calling an API Gateway endpoint
- Python Lambda function that updates visitor count in DynamoDB
- AWS SAM template for backend infrastructure as code
- GitHub Actions workflows for backend and frontend CI/CD

## Repository Structure

- `/frontend/index.html` - Resume page
- `/frontend/style.css` - Resume styling
- `/frontend/script.js` - Visitor counter JavaScript
- `/backend/app.py` - Lambda function (Python + boto3)
- `/backend/template.yaml` - SAM template (API Gateway, Lambda, DynamoDB)
- `/backend/tests/test_app.py` - Python unit tests
- `/.github/workflows/backend.yml` - Test + SAM deploy workflow
- `/.github/workflows/frontend.yml` - S3 sync + CloudFront invalidation workflow

## Deploy Frontend (S3 + CloudFront + DNS)

1. Create an S3 bucket for static website hosting.
2. Create a CloudFront distribution with the S3 bucket as origin.
3. Request an ACM certificate for your custom domain (in `us-east-1`) and attach it to CloudFront.
4. Point your domain DNS record (Route 53 or another provider) to CloudFront.
5. Set `window.VISITOR_COUNTER_API_URL` in the frontend (or inject during build) to your API Gateway endpoint output.

## Deploy Backend (SAM)

From `/backend`:

```bash
sam build
sam deploy --guided
```

The deploy output includes `VisitorCounterApiUrl`, which is the endpoint used by the frontend counter.

## GitHub Secrets Required

- `AWS_REGION`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `SAM_STACK_NAME`
- `S3_BUCKET_NAME`
- `CLOUDFRONT_DISTRIBUTION_ID`
