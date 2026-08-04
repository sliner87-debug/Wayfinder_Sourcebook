import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("file:///H:/Antigravity/Ahoy Matey/Wayfinder_Sourcebook/index.html")
        # Added tagged=True and outline=True for native PDF bookmarks
        await page.pdf(path="Wayfinder_Sourcebook.pdf", format="A4", print_background=True, tagged=True, outline=True)
        await browser.close()
        print("PDF generated successfully.")

asyncio.run(main())
