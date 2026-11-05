# Deployment guide

## Render (recommended single-service deployment)
The frontend is served by FastAPI, so only one web service is needed.

1. Create a GitHub repository and upload the contents of this project folder.
2. Sign in to Render and select **New > Blueprint**.
3. Connect the repository. Render detects `render.yaml`.
4. Confirm creation of the `agricare-ai` web service.
5. Wait for the build to finish, then open the service URL.
6. Verify the home page and `/api/health`.

## Local smoke test
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```
Test:
- `/` — frontend
- `/api/health` — service health
- `/docs` — interactive API documentation

## Deployment checklist
- [ ] Confirm `/api/health` returns `{"status":"ok",...}`.
- [ ] Test fertilizer form with valid soil values.
- [ ] Test image upload with a JPG/PNG.
- [ ] Confirm market page displays the DEMO DATA warning.
- [ ] Test browser voice support; typed input remains available.
- [ ] Test the digital twin and confirm its illustrative-model warning.
- [ ] Add and validate trained models and authorised live data integrations before claiming real predictions.
