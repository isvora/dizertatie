import random
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By


df = pd.read_excel('formular.xlsx')
rasp1 = df['Ce resurse suplimentare v-ar ajuta să munciţi eficient în timp ce lucraţi de la distanţă/ acasă? (Completaţi)']
rasp2 = df['Aveţi şi vreun alt feedback care ar îmbunătăţi noul nostru mediu de lucru de la distanţă/ acasă? (Completaţi)']
rasp3 = df['Ce a facut organizaţia ca să sprijine tranziţia către lucrul de la distanţă/ acasă? (Completaţi)']

i = len(rasp1)
while i > 0:
    driver = webdriver.Chrome('./chromedriver')

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScjFy-6_urfwQbM0M_t-ceo_vISZRDIRF_GryEFeYAFtHMHRQ/formResponse")

    time.sleep(2)

    checkbox = driver.find_element(By.XPATH, "//div[@class='uHMk6b fsHoPb']")
    checkbox.click()

    inainte = driver.find_element(By.XPATH, "//span[@class='NPEfkd RveJvd snByac']")
    inainte.click()

    print(driver.title)

    round_checkbox = 'AB7Lab Id5V1'

    questions = driver.find_elements(By.XPATH, "//div[@class='lLfZXe fnxRtf EzyPc']")
    counter = 0
    for i in range(0, 8):
        choices = questions[i].find_elements(By.XPATH, "//div[@class='d7L4fc bJNwt  aomaEc ECvBRb']")
        choice_number = random.randint(0, 6) + counter
        counter += 7
        choices[choice_number].click()

    counter = 112
    for i in range(0, 10):
        choices = questions[i].find_elements(By.XPATH, "//div[@class='d7L4fc bJNwt  aomaEc ECvBRb']")
        choice_number = random.randint(0, 4) + counter
        counter += 5
        choices[choice_number].click()

    buttons = driver.find_elements(By.XPATH, "//span[@class='NPEfkd RveJvd snByac']")
    buttons[1].click()

    print("Second page")

    questions = driver.find_elements(By.XPATH, "//div[@class='ssX1Bd']")
    counter = 0
    for i in range(0, 9):
        choices = questions[i].find_elements(By.XPATH, "//div[@class='d7L4fc bJNwt  aomaEc ECvBRb']")
        choice_number = random.randint(0, 5) + counter
        counter += 6
        choices[choice_number].click()

    buttons = driver.find_elements(By.XPATH, "//span[@class='NPEfkd RveJvd snByac']")
    buttons[1].click()

    questions = driver.find_elements(By.XPATH, "//div[@class='lLfZXe fnxRtf EzyPc']")
    counter = 0
    for i in range(0, 6):
        choices = questions[i].find_elements(By.XPATH, "//div[@class='d7L4fc bJNwt  aomaEc ECvBRb']")
        choice_number = random.randint(0, 4) + counter
        counter += 5
        choices[choice_number].click()

    raspunsuri = driver.find_elements(By.XPATH, "//div[@class='Pc9Gce Wic03c']")

    text_area = raspunsuri[0].find_element(By.TAG_NAME, "textarea")
    random_rasp = rasp1[random.randint(0, len(rasp1))]
    text_area.send_keys(random_rasp)

    text_area = raspunsuri[1].find_element(By.TAG_NAME, "textarea")
    random_rasp = rasp2[random.randint(0, len(rasp1))]
    text_area.send_keys(random_rasp)

    text_area = raspunsuri[2].find_element(By.TAG_NAME, "textarea")
    random_rasp = rasp3[random.randint(0, len(rasp1))]
    text_area.send_keys(random_rasp)

    buttons = driver.find_elements(By.XPATH, "//span[@class='NPEfkd RveJvd snByac']")
    buttons[1].click()

    questions = driver.find_elements(By.XPATH, "//div[@class='lLfZXe fnxRtf EzyPc']")
    counter = 0
    for i in range(0, 4):
        choices = questions[i].find_elements(By.XPATH, "//div[@class='d7L4fc bJNwt  aomaEc ECvBRb']")
        choice_number = random.randint(0, 4) + counter
        counter += 5
        choices[choice_number].click()

    counter = 40
    for i in range(0, 10):
        choices = questions[i].find_elements(By.XPATH, "//div[@class='d7L4fc bJNwt  aomaEc ECvBRb']")
        choice_number = random.randint(0, 4) + counter
        counter += 5
        choices[choice_number].click()

    buttons = driver.find_elements(By.XPATH, "//span[@class='NPEfkd RveJvd snByac']")
    buttons[1].click()

    questions = driver.find_elements(By.CLASS_NAME, "N9Qcwe")
    counter = 0
    for i in range(0, 3):
        choices = questions[i].find_elements(By.XPATH, "//div[@class='d7L4fc bJNwt  aomaEc ECvBRb']")
        choice_number = random.randint(0, 6) + counter
        counter += 7
        choices[choice_number].click()

    questions = driver.find_elements(By.XPATH, "//div[@class='lLfZXe fnxRtf EzyPc']")
    counter = 21
    for i in range(0, 7):
        choices = questions[i].find_elements(By.XPATH, "//div[@class='d7L4fc bJNwt  aomaEc ECvBRb']")
        choice_number = random.randint(0, 4) + counter
        counter += 5
        choices[choice_number].click()

    buttons = driver.find_elements(By.XPATH, "//span[@class='NPEfkd RveJvd snByac']")
    buttons[1].click()

    questions = driver.find_elements(By.XPATH, "//div[@class='lLfZXe fnxRtf EzyPc']")
    counter = 0
    for i in range(0, 13):
        choices = questions[i].find_elements(By.XPATH, "//div[@class='d7L4fc bJNwt  aomaEc ECvBRb']")
        choice_number = random.randint(0, 6) + counter
        counter += 7
        choices[choice_number].click()

    buttons = driver.find_elements(By.XPATH, "//span[@class='NPEfkd RveJvd snByac']")
    buttons[1].click()

    raspunsuri = driver.find_elements(By.XPATH, "//div[@class='Xb9hP']")

    input = raspunsuri[0].find_element(By.TAG_NAME, "input")
    varsta = df['Care este vârsta dvs.?']
    random_rasp = varsta[random.randint(0, len(varsta))]
    input.send_keys(random_rasp)

    input = raspunsuri[1].find_element(By.TAG_NAME, "input")
    copii = df['Care este numărul de copii pe care îl aveți (dacă este cazul)?']
    random_rasp = copii[random.randint(0, len(copii))]
    input.send_keys(random_rasp)

    input = raspunsuri[2].find_element(By.TAG_NAME, "input")
    incadrare = df['De cât timp sunteți încadrat în această funcție? (an și luni)']
    random_rasp = incadrare[random.randint(0, len(incadrare))]
    input.send_keys(random_rasp)

    input = raspunsuri[3].find_element(By.TAG_NAME, "input")
    ani_lucru = df['Câți ani ați lucrat, în total?']
    random_rasp = ani_lucru[random.randint(0, len(ani_lucru))]
    input.send_keys(random_rasp)

    input = raspunsuri[4].find_element(By.TAG_NAME, "input")
    remote = df['Dacă lucrați în regim hibrid, menționați câte zile pe săptămână lucrați de acasă.']
    random_rasp = remote[random.randint(0, len(remote))]
    input.send_keys(random_rasp)

    # Apasa trimiteti
    # buttons = driver.find_elements(By.XPATH, "//span[@class='NPEfkd RveJvd snByac']")
    # buttons[1].click()

    i -= 1
    print("Finished")
