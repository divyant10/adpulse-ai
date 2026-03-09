import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_recommendations(ads_report, support_report):

    prompt = f"""
You are an advertising analytics expert.

Campaign Diagnostics:
{ads_report}

Support Analytics:
{support_report}

Provide concise actionable recommendations (5 bullet points maximum)
to improve advertising campaign performance.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("AI ERROR:", e)

        return """
⚠️ AI service temporarily unavailable.

Showing analytics-based suggestions instead:

1. Improve ad creatives to increase CTR
2. Reduce high CPC keywords
3. Focus budget on high converting campaigns
4. Fix tracking errors
5. Improve targeting
"""