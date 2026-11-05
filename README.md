# AgriCare AI — integrated deployment starter

A single FastAPI application with a responsive web frontend and modular smart-farming features.

## Included modules
- Fertilizer recommendation: preliminary NPK/pH screening (rule-based; not a fertilizer prescription).
- Pest detection: image upload endpoint and UI. A trained pest model is **not** bundled; the API explicitly reports that no prediction is available.
- Market price intelligence: interface and API with clearly labelled sample values. Not live mandi data.
- Multilingual assistant: English, Telugu and Hindi template responses; browser speech input/output where supported.
- Farm digital twin: illustrative rule-based moisture/heat scenario, not a calibrated crop model.
- Additional dashboard sections: disease guidance and irrigation advice.

## Run locally
Requires Python 3.10 or newer.

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000

## Deploy on Render
1. Push this folder to a GitHub repository.
2. In Render, choose **New > Blueprint** and select the repository containing `render.yaml`.
3. Render reads `render.yaml`, installs requirements and starts the FastAPI server.
4. Open the generated service URL and check `/api/health`.

You can also create a Render Web Service manually:
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## API documentation
After starting the app, visit `/docs`.

## Important before real-world use
This is a new, self-contained implementation based on the feature list, not a modification of the user's original AgriCare AI source code. The original repository/source files were not provided, so the old implementation and exact existing UI could not be preserved or merged.

Before using this for real farming decisions:
- Train and validate a pest detection model on properly labelled, representative crop/pest images; integrate inference in `app/main.py`.
- Replace sample mandi values in `app/services/agriculture.py` with a verified live data provider such as an authorised Agmarknet/eNAM feed. Respect provider terms and cache/rate limits.
- Replace the rule-based digital twin with calibrated crop/soil models and local field data.
- Calibrate fertilizer logic to units, lab method, crop stage, local soil recommendations and regional agronomy guidance.
- Add authentication, authorisation, rate limiting, secure storage and HTTPS if storing farmer accounts or field records.
- Set CORS to the actual frontend origin if frontend and backend are deployed separately.

## Environment variables
Copy `.env.example` to `.env` for local secrets if you later integrate a provider. Never commit real API keys.


## Deploy on Vercel

For the Vercel-ready version and beginner deployment steps, see `VERCEL_DEPLOYMENT_GUIDE.md`. The root-level `main.py` exports the FastAPI application for Vercel's Python runtime.
