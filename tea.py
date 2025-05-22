import asyncio
from pyppeteer import launch

async def claim_faucet():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('https://faucet-assam.tea.xyz/', {'waitUntil': 'networkidle2'})

    # Example: Replace with actual selector for wallet input and claim button
    wallet_address = 'YOUR_WALLET_ADDRESS'

    # Wait for input field and enter wallet address
    await page.waitForSelector('input[type="text"]')
    await page.type('input[type="text"]', wallet_address)

    # Wait for and click the claim button (adjust selector as needed)
    await page.waitForSelector('button')
    await page.click('button')

    # Wait for confirmation (optional, adjust selector/message)
    await page.waitFor(5000)  # Wait 5 seconds for any confirmation

    await browser.close()

# Run the script
asyncio.get_event_loop().run_until_complete(claim_faucet())
