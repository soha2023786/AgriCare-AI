# Deploy AgriCare AI on Vercel

This version is configured for Vercel's Python runtime. The frontend and FastAPI
backend are served by the same FastAPI application.

## Deploy using GitHub (beginner-friendly)

1. Extract `AgriCare_AI_Vercel.zip` on your computer.
2. Create a new GitHub repository, for example `agricare-ai-vercel`.
3. Upload **all files inside** the extracted `AgriCare_AI_Vercel` folder to the
   repository root. Make sure `main.py`, `requirements.txt`, `.python-version`,
   and the `app` folder are at the top level.
4. Sign in to Vercel and choose **Add New → Project**.
5. Import the GitHub repository you just created.
6. Keep the detected Python/FastAPI settings. Do not enter a custom build command
   or output directory for this project.
7. Click **Deploy** and wait for the build to finish.
8. Open the generated `.vercel.app` address.

## Check that it works

- Open your Vercel project URL to view the dashboard.
- Open `https://YOUR-PROJECT.vercel.app/api/health` to check the backend.
- Open `https://YOUR-PROJECT.vercel.app/docs` to view the API documentation.

## Important notes

- Vercel's Python runtime currently supports FastAPI. This project exposes the
  FastAPI object through the root-level `main.py` entrypoint.
- Uploaded pest images are validated but not saved permanently. Vercel function
  filesystems are temporary; use object storage (for example, S3 or Cloudinary)
  if persistent image storage is needed.
- Pest detection is not a real AI prediction until a trained model is integrated.
- Market prices and digital-twin outputs remain labelled demo/sample results.
- This is a standalone starter based on the feature list, not a merge of your
  original AgriCare AI source code.

## If deployment fails

1. Open the failed deployment in Vercel.
2. Select **Build Logs**.
3. Copy the first red error message and share it; it usually identifies the issue.
4. Confirm that the repository root contains `main.py` and `requirements.txt`.
