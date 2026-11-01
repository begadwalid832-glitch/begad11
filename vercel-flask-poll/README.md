# Flask Poll Demo

This project is set up to deploy on Vercel.

## Local run

```bash
python -m venv .venv
. .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

## Deploy to Vercel

1. Push this folder to a GitHub repository.
2. Open Vercel and import the repository.
3. Use the default settings.
4. Deploy.

The app uses the Vercel Python serverless entry point at `api/index.py`.
