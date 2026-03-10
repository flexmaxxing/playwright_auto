from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        # Launch Chromium in non-headless mode (visible browser window)
        browser = p.chromium.launch(
            channel="chrome",  # Uses your installed Google Chrome; remove this line to fall back to Playwright's Chromium
            headless=False
        )

        page = browser.new_page()

        url = "http://mlgnt104/FAReports/ReportViewer/Launcher/Launch/43"
        print(f"Navigating to: {url}")

        page.goto(url, wait_until="networkidle", timeout=30000)

        print(f"Page loaded: {page.title()}")

        # Keep the browser open until user presses Enter
        input("Press Enter to close the browser...")

        browser.close()


if __name__ == "__main__":
    main()
