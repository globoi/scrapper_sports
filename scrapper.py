import serpapi  # type: ignore

import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)

results = client.search(
    engine="google_play_product",
    product_id="br.tv.horizonte.android.premierefc",
    store="apps",
    all_reviews=True,
    sort_by=2,
    num=10,
    gl="br",
)

print(results["reviews"])
