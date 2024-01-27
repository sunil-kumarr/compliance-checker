# Compliance Checker API

## Overview

The Compliance Checker API is designed to analyze webpage content against a specified compliance policy and provide non-compliance findings in a structured JSON format. This API utilizes the OpenAI GPT-3.5 Turbo model to generate responses.

### Usage

```
curl --location 'http://127.0.0.1:5000/ai/check-compliance' \
--header 'Content-Type: application/json' \
--data '{
    "compliance_url": "https://stripe.com/docs/treasury/marketing-treasury",
    "webpage_url": "https://www.joinguava.com/",
    "webpage_identifier": "GAUVA",
    "compliance_identifier": "STRIPE"
}'
```

- **compliance_url:** URL of the compliance policy documentation.

- **webpage_url:** URL of the webpage to be analyzed.

- **webpage_identifier:** Identifier for the webpage content.

- **compliance_identifier:** Identifier for the compliance policy.

**Response**
The API response will contain non-compliance findings in the following JSON format:

<img src="/screenshots/postman_output.png"/>
