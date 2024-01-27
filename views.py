import json
from flask import request, jsonify, Blueprint
import settings
import openai
from scrapers.compliance import WebScraper

client = openai.OpenAI(api_key=settings.OPEN_API_KEY, organization=settings.ORG_ID)

aiBlueprint = Blueprint("ai-routes", import_name="ai", url_prefix="/ai")


@aiBlueprint.route("/check-compliance", methods=["POST"])
def check_compliance():
    try:
        request_data = request.json

        required_fields = [
            "compliance_url",
            "compliance_identifier",
            "webpage_url",
            "webpage_identifier",
        ]
        for field in required_fields:
            if not request_data.get(field):
                return jsonify({"message": f"""{field} is required."""})

        scraper = WebScraper()
        compliance_policy = scraper.parse(
            url=request_data.get("compliance_url"),
            identifier=request_data.get("compliance_identifier"),
        )
        webpage_content = scraper.parse(
            url=request_data.get("webpage_url"),
            identifier=request_data.get("webpage_identifier"),
        )

        input_text = f"Webpage content: {webpage_content}\nCompliance Policy: {compliance_policy}"

        # Use GPT-3 to analyze and find non-compliant results
        print("Chating with Assitant MODEL")
        chatCompletion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are compliance validator assistant.",
                },
                {
                    "role": "system",
                    "content": """Given the compliance policy and the webpage content. Return the non-compliance findings in the following JSON format: 
                                {"nonComplianceFindings": ["[finding_description_here]",...]}""",
                },
                {"role": "user", "content": input_text},
            ],
        )
        print("Assitant replied:")
        print("Output choices:", len(chatCompletion.choices))
        chatCompletionMessage = chatCompletion.choices[0].message
        print("Loading reply as JSON:", len(chatCompletion.choices))
        data = json.loads(chatCompletionMessage.content)
        print("Chating complete.")
        return jsonify({"status": "success", "data": data})

    except Exception as e:
        return jsonify({"status": "failed", "error": str(e)})
