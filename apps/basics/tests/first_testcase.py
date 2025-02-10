from playwright.sync_api import Playwright, sync_playwright, expect

from playwright_stealth import stealth_sync

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    # Apply the stealth settings
    stealth_sync(page)

    try:
        # Navega até o Google
        page.goto("https://www.google.com.br/")

        # Preenche a pesquisa
        page.get_by_role("combobox", name="Pesquisar").click()
        page.get_by_role("combobox", name="Pesquisar").fill("playwright documentation python")
        page.get_by_role("button", name="Pesquisa Google").first.click()

        # Aguarda o reCAPTCHA aparecer
        page.wait_for_selector("iframe[title='reCAPTCHA']")

        # Alterna para o iframe do reCAPTCHA
        recaptcha_iframe = page.frame_locator("iframe[title='reCAPTCHA']")

        # Clica na caixa de verificação do reCAPTCHA
        recaptcha_iframe.get_by_role("checkbox", name="I'm not a robot").click()

        # Aguarda o desafio do reCAPTCHA (se necessário)
        page.wait_for_timeout(5000)  # Ajuste o tempo conforme necessário

        # Continua com a interação
        page.get_by_role("link", name="Playwright Python Playwright https://playwright.dev › docs › api").click()

    except Exception as e:
        print(f"Erro durante a execução: {e}")

    finally:

        # Stop tracing and export it into a zip archive.
        context.tracing.stop(path = "trace.zip")

        # Fecha o navegador
        context.close()


        browser.close()

with sync_playwright() as playwright:
    run(playwright)