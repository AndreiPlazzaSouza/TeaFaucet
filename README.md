
# TeaFaucet

**TeaFaucet** is a Python script to automate claiming from crypto faucets, such as [https://faucet-assam.tea.xyz/](https://faucet-assam.tea.xyz/).  
It leverages browser automation to interact with faucet web pages, enabling scheduled and unattended claims.

---

## Features

- Automates the process of claiming from supported faucets
- Headless browser operation for efficiency
- Easy to schedule via cronjob or task scheduler
- Written in Python for simplicity and extensibility

---

## Requirements

- Python 3.7+
- [pyppeteer](https://github.com/pyppeteer/pyppeteer) (or similar browser automation library)

Install dependencies:
```bash
pip install pyppeteer
```

---

## Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AndreiPlazzaSouza/TeaFaucet.git
    cd TeaFaucet
    ```

2. **Edit `tea.py`:**
    - Set your wallet address and adjust selectors if needed for the target faucet.

3. **Run the script:**
    ```bash
    python tea.py
    ```

4. **Automate with cronjob (Linux/Mac):**
    - Open your crontab:
      ```bash
      crontab -e
      ```
    - Add a line to schedule the script (e.g., every 6 hours):
      ```
      0 */6 * * * /usr/bin/python3 /path/to/TeaFaucet/tea.py
      ```

---

## Example

```python
import asyncio
from pyppeteer import launch

async def claim_faucet():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://faucet-assam.tea.xyz/', {'waitUntil': 'networkidle2'})
    await page.type('input[type="text"]', 'YOUR_WALLET_ADDRESS')
    await page.click('button')
    await page.waitFor(5000)
    await browser.close()

asyncio.get_event_loop().run_until_complete(claim_faucet())
```

---

## Notes

- **Selectors may need adjustment**: Use browser dev tools to inspect and update the input/button selectors in `tea.py` as faucet UIs change.
- **Captcha Handling**: If the faucet uses captchas, additional integration (e.g., third-party captcha solvers) is required.
- **Respect faucet rules**: Automating claims may violate some faucet terms of service. Use responsibly.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

Answer from Perplexity: https://www.perplexity.ai/search/megaeth-wallet-creator-bulk-wi-FVJ2uP5_QI2VyZkWpFz2aw?utm_source=copy_output
