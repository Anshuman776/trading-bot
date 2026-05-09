# Binance Futures Testnet Trading Bot

A simple Python-based trading bot for Binance Futures Testnet using a CLI interface.

## Features

- MARKET orders
- LIMIT orders
- BUY/SELL support
- CLI interface
- Logging
- Error handling
- Input validation

---

## Project Structure

```text
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── logs/
│   └── trading.log
├── screenshots/
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup

### 1. Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```env
BINANCE_API_KEY=your_key
BINANCE_SECRET_KEY=your_secret
```

---

## Example Commands

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

---

## Assumptions

- Uses Binance Futures Testnet
- LIMIT orders use GTC (Good-Till-Cancelled)
- Quantity precision depends on Binance exchange rules

---

## Requirements

```txt
python-binance==1.0.17
python-dotenv==1.0.0
rich==13.7.0
```

---
## Screenshots

### MARKET Order

![market](https://github.com/user-attachments/assets/96634f86-3919-4a57-9d9f-85bc2c4485a5)

---

### LIMIT Order

![limit](https://github.com/user-attachments/assets/1b731552-825e-4b7b-8e88-153fe20f2f14)

---

### Logging Output

![logs](https://github.com/user-attachments/assets/93f4c37c-432f-442c-8510-e618adcb09ae)
