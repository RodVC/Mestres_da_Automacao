from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao_esperada
import os
from Models.db_movement import configurar_banco_de_dados, add_produtos, buscar_todos_produtos
import time


class desafio_scrapping_bd:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pr-BR')
        chrome_options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver.exe',options=chrome_options)
        self.wait = WebDriverWait(self.driver,10,1,[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
        self.num_pagina = 0
    
    def iniciar(self):
        self.navegar_pagina()
        self.scrapping()

    def navegar_pagina(self):
        self.num_pagina += 1
        self.num_pagina = str(self.num_pagina)
        self.link_pagina = f'https://cursoautomacao.netlify.app/produtos{self.num_pagina}.html'
        self.driver.get(self.link_pagina)

    def scrapping(self):
        try:
            while True:

                self.nomes = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//h5[@class="name"]')))
                self.precos = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//p[@class="price-container"]')))
                self.descricoes = self.wait.until(condicao_esperada.visibility_of_all_elements_located((By.XPATH,'//div[@class="description"]')))
                self.dados = zip(self.nomes,self.precos,self.descricoes)
                
                conexao = configurar_banco_de_dados()
                
                for nome, preco, descricao in self.dados:
                    add_produtos(conexao, nome.text,float(preco.text[1:]),descricao.text)
                
                time.sleep(2)
                self.num_pagina=int(self.num_pagina)
                self.navegar_pagina()

        except:
            buscar_todos_produtos(conexao)
            print('Web Scrapping Finalizado!')
            

if __name__ == "__main__":
    start = desafio_scrapping_bd()
    start.iniciar()

