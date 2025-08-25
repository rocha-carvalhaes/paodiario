from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

class ScrapperMensagem:
    def __init__(self):
        pass

    def coletar_mensagem(self):
        """
        Coleta a mensagem do dia do site Vatican News.
        """

        data = datetime.now().strftime("%Y/%m/%d")  # formata "2025/08/08"
        url = f"https://www.vaticannews.va/pt/palavra-do-dia/{data}.html"

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # modo sem interface gráfica
        driver = webdriver.Chrome(options=options)

        try:
            driver.get(url)
            time.sleep(2)  # espera carregar a página

            div = driver.find_element(By.CLASS_NAME, "section__content")

            paragrafos = div.find_elements(By.TAG_NAME, "p")

            paragrafos = [p.text for p in paragrafos if p.text.strip() != ""]
            mensagem = " ".join(p.replace("\n", " ") for p in paragrafos)

        except Exception as e:
            print("Ocorreu um erro:", e)
        finally:
            driver.quit()
        return mensagem

ScrapperMensagem().coletar_mensagem()
