# Binance Futures Testnet Trading Bot

A simple Python-based trading bot for Binance Futures Testnet using a CLI interface.

## Features

- 📊 MARKET orders
- 🎯 LIMIT orders  
- 🔄 BUY/SELL support
- 📝 Comprehensive logging
- 🖥️ CLI interface
- ✅ Order validation
- 🌐 Binance Futures Testnet support

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py              # Binance client setup
│   ├── orders.py              # Order placement logic
│   ├── validators.py          # Input validation
│   └── logging_config.py      # Logging configuration
├── logs/
│   └── trading.log
├── cli.py                      # CLI interface
├── .env                        # API credentials
├── requirements.txt            # Python dependencies
└── README.md
```

## Setup

### 1. Clone/Download the repository
```bash
git clone <repo>
cd trading_bot
```

### 2. Create virtual environment (Python 3.10+)
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # Linux/Mac
```

### 3. Install dependencies
```bash
# Binance Futures Testnet Trading Bot

A simple Python trading bot for Binance Futures Testnet with a CLI interface.

## Features

- MARKET orders
- LIMIT orders
- BUY/SELL support
- CLI interface
- Logging
- Error handling

## Setup

1. Create and activate a virtual environment (recommended Python 3.10+):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env`:

```
BINANCE_API_KEY=your_key
BINANCE_SECRET_KEY=your_secret
```

## Example Commands

MARKET:

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

LIMIT:

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

## Assumptions

- Uses Binance Futures Testnet
- LIMIT orders use GTC (Good-Till-Cancelled)
- Quantity precision depends on Binance exchange rules

## Requirements
Ensure `requirements.txt` contains:

```
python-binance==1.0.17
python-dotenv==1.0.0
rich==13.7.0
```

## Git / Submission

Initialize and commit locally:

```powershell
git init
git add .
git commit -m "Trading bot assignment submission"
```

Create a GitHub repo, then add remote and push:

```powershell
git remote add origin YOUR_REPO_URL
git branch -M main
git push -u origin main
```

## Final Submission Checklist

Requirement	Status
MARKET order	✅
LIMIT order	⬜
BUY/SELL	✅
CLI	✅
Validation	✅
Logging	✅
Error handling	✅
README	✅
requirements.txt	✅
GitHub repo	⬜
Log files	⬜

---

You're nearly finished — run the example commands above and, if you want, I can push the repo once you provide the GitHub repo URL.
