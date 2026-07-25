# PagePulse - URL Auditor

A simple API to audit any website and get status, load time, title and word count.

Built for Digital Heroes Training Task

**Live Demo**: https://pagepulse-production-aca2.up.railway.app

**GitHub Repo**: https://github.com/holika17135/pagepulse

## Setup
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
## API Contract

**Endpoint**: `POST /audit`

**Request**:
```json
{
  "url": "https://example.com"
}

#### **2. DESIGN DECISIONS + TESTING ADD CHEY**
Daani kinda idhi kuda paste chey:
```markdown
## Design Decisions

1. **Used requests + BeautifulSoup**: Fast ga HTML fetch chesi parse cheyadaniki.
2. **Error Handling with try/except**: Invalid URLs, timeouts vaste app crash avvakunda.
3. **Railway Deployment**: PORT ni env variable nunchi tesukunnanu.

## Testing
Run: `python test_audit.py`

## Loom Demo
[Video link here after recording]

---
Built for Digital Heroes Training Task
https://digitalheroesco.com