from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Imports from Lukas
from requests import api
from requests.api import request
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
import os
import requests
import json

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from collections import Counter

NUMBER_OF_PAGES = 3
NB_LINKS = 20

def show_me():
    print("................... -- ******************************** -- ...................\n\n")
    print("................... -- Logiciel créé par Thomas Peugnet -- ...................")
    print("................... -- ******************************** -- ...................\n\n")
    print("........................... -- Search SomeBody -- ............................")
    print(".................... -- Search And Find Some people ! -- .....................\n\n")
    print("................... -- ******************************** -- ...................")


def take_infos():
    # Take all of the infos from the user to put them in a list.
    # Return the list of all of theses infos
    print("\n== Identitité générale ==\n")
    first_name = input("Prenom : ")
    last_name = input("Nom : ")
    other_name = input("Autre nom : ")
    pseudo = input("Pseudo connu : ")
    phone_number = input("Numéro de téléphone : ")
    ip_adress = input("Adresse IP (Si non dynamique) : ")

    print("\n== Mails ==\n")
    nb_mails = input("Nombre d'adresses mails connues : ")
    mails_list = []
    for i in range(int(nb_mails)):
        mail = input("Adresse mail " + str(i) + ": ")
        mails_list.append(mail)
    if mails_list != []:
        print("Liste des mails inscrits : ")
        print(mails_list)

    print("\n== Villes ==\n")
    nb_citys = input("Nombre de villes connues : ")
    citys_list = []
    for i in range(int(nb_citys)):
        city = input("Ville " + str(i) + ": ")
        citys_list.append(city)
    if citys_list != []:
        print("Liste des villes inscrites : ")
        print(citys_list)

    print("\n== Départements ==\n")
    nb_departments = input("Nombre de départements connus : ")
    departments_list = []
    for i in range(int(nb_departments)):
        department = input("[NOM ou CODE POSTAL] Département " + str(i) + ": ")
        departments_list.append(department)
    if departments_list != []:
        print("Liste des départements inscrits : ")
        print(departments_list)

    print("\n== Centres d'intérêt / Mots clés ==\n")
    keywords_list = []
    keyword_count = 0
    keyword = "Before"
    while (keyword != ""):
        keyword = input("Mot clé : " + str(keyword_count) + ": ")
        if keyword != "":
            keyword_count = keyword_count + 1
            keywords_list.append(keyword)
    if keywords_list != []:
        print("Liste des keywords inscrits : ")
        print(keywords_list)
    print("\n== Toutes les informations nécessaires ont été prises == \n")
    print("\nAffichage... \n")
    infos_list = [[first_name, last_name, other_name, pseudo, phone_number, ip_adress], mails_list, citys_list,
                  departments_list, keywords_list]
    for element in infos_list:
        time.sleep(0.5)
        print(element)
    print("\n\nTraitement en cours...\n")
    return infos_list


def request_filetype(infos_list, file_type):
    # Make the requests list for file type, as PDF, Doc etc
    # Return the requests list for the file type inserted

    # Common
    dual_name_FILE_request = ["\"" + infos_list[0][0] + " " + infos_list[0][1] + "\" filetype:" + file_type, "Prenom Nom in " + file_type.upper() + " files"]  # "prenom.nom" filettype:FILE_TYPE
    dual_name_other_FILE_request = ["\"" + infos_list[0][0] + " " + infos_list[0][1] + " " + infos_list[0][2] + "\" filetype:" + file_type, "Prenom Nom Other in " + file_type.upper() + " files"]  # "prenom nom other" filettype:FILE_TYPE
    pseudo_FILE_request = ["\"" + infos_list[0][3] + "\" filetype:" + file_type, "Pseudo in " + file_type.upper() + " files"]  # "pseudo" filettype:FILE_TYPE
    phone_number_FILE_request = ["\"" + infos_list[0][4] + "\" filetype:" + file_type, "Phone number in " + file_type.upper() + " files"]  # "phone number" filettype:FILE_TYPE
    ip_adress_FILE_request = ["\"" + infos_list[0][5] + "\" filetype:" + file_type, "IP Adress in " + file_type.upper() + " files"]  # "IP Adress" filettype:FILE_TYPE

    # Mails
    mail_list_FILE_request = []
    for mail_addr in infos_list[1]:
        mail_FILE_request = ["\"" + mail_addr + "\" filetype:" + file_type,
                             "Mail : " + mail_addr + " in " + file_type.upper() + " files"]  # "mail@mail.com" filettype:FILE_TYPE
        mail_list_FILE_request.append(mail_FILE_request)

    return [[dual_name_FILE_request, pseudo_FILE_request, phone_number_FILE_request, ip_adress_FILE_request],
            mail_list_FILE_request]


def request_city_hobby(infos_list, request_type):
    # Make the request list of cities and hobbies
    # Return the requests list for the request_type inserted ("hobbies" for example)

    # TODO : Recoder pour tout faire dans un seul for, si necessaire pour ajouter facilement de nouvelles requetes...
    result_requests_list = []

    # Cities
    if request_type == "city":
        common_list_CITY_request = []
        for city in infos_list[2]:
            dual_name_CITY_request = ["\"" + infos_list[0][0] + " " + infos_list[0][1] + "\" " + city,
                                      "Prenom Nom in " + city.upper()]  # "Prenom Nom" Ville
            dual_name_other_CITY_request = [
                "\"" + infos_list[0][0] + " " + infos_list[0][1] + " " + infos_list[0][2] + "\" " + city,
                "Prenom Nom Other in " + city.upper()]  # "prenom nom other" Ville
            pseudo_CITY_request = ["\"" + infos_list[0][3] + "\" " + city,
                                   "Pseudo in " + city.upper()]  # "pseudo" Ville
            common_list_CITY_request.append([dual_name_CITY_request, dual_name_other_CITY_request, pseudo_CITY_request])
        result_requests_list = common_list_CITY_request

    # Departments
    elif request_type == "department":
        common_list_DEPARTMENT_request = []
        for department in infos_list[3]:
            dual_name_DEPARTMENT_request = ["\"" + infos_list[0][0] + " " + infos_list[0][1] + "\" " + department,
                                            "Prenom Nom in " + department.upper()]  # "Prenom Nom" Ville
            dual_name_other_DEPARTMENT_request = [
                "\"" + infos_list[0][0] + " " + infos_list[0][1] + " " + infos_list[0][2] + "\" " + department,
                "Prenom Nom Other in " + department.upper()]  # "prenom nom other" Ville
            pseudo_DEPARTMENT_request = ["\"" + infos_list[0][3] + "\" " + department,
                                         "Pseudo in " + department.upper()]  # "pseudo" Ville
            common_list_DEPARTMENT_request.append(
                [dual_name_DEPARTMENT_request, dual_name_other_DEPARTMENT_request, pseudo_DEPARTMENT_request])
        result_requests_list = common_list_DEPARTMENT_request

    # Hobbies
    elif request_type == "hobby":
        common_list_HOBBY_request = []
        for hobby in infos_list[3]:
            dual_name_HOBBY_request = ["\"" + infos_list[0][0] + " " + infos_list[0][1] + "\" " + hobby,
                                       "Prenom Nom in " + hobby.upper()]  # "Prenom Nom" Ville
            dual_name_other_HOBBY_request = [
                "\"" + infos_list[0][0] + " " + infos_list[0][1] + " " + infos_list[0][2] + "\" " + hobby,
                "Prenom Nom Other in " + hobby.upper()]  # "prenom nom other" Ville
            pseudo_HOBBY_request = ["\"" + infos_list[0][3] + "\" " + hobby,
                                    "Pseudo in " + hobby.upper()]  # "pseudo" Ville
            common_list_HOBBY_request.append(
                [dual_name_HOBBY_request, dual_name_other_HOBBY_request, pseudo_HOBBY_request])
        result_requests_list = common_list_HOBBY_request

    return result_requests_list


def list_requests(infos_list):
    # Make the list of all of the requests which have to be done
    # Return a Giga list with all requests

    # Simple requests - Search for common results
    dual_name_request = ["\"" + infos_list[0][0] + " " + infos_list[0][1] + "\"", "Prenom Nom"]  # "Prenom Nom"
    triple_name_request = ["\"" + infos_list[0][0] + " " + infos_list[0][1] + " " + infos_list[0][2] + "\"",
                           "Prenom Nom Autre"]  # "Prenom Nom Nom Nom"
    pseudo_request = ["\"" + infos_list[0][3] + "\"", "Pseudo"]  # "pseudo"
    phone_number_request = ["\"" + infos_list[0][4] + "\"", "Numéro de téléphone"]  # "numéro de téléphone"
    ip_adress_request = ["\"" + infos_list[0][5] + "\"", "Adresse IP"]  # "Adresse IP"
    index_of_request = ["intitle:\"index of\" \"" + infos_list[0][0] + " " + infos_list[0][1] + "\"",
                        "Index Of"]  # "Prenom Nom"

    # First Advanced requests -- Search for account hack in TXT files
    txt_search = request_filetype(infos_list, 'txt')
    # First Advanced requests -- Search for account hack in PDF files
    pdf_search = request_filetype(infos_list, 'pdf')
    # First Advanced requests -- Search for account hack in DOC files
    doc_search = request_filetype(infos_list, 'doc')

    # More Advanced requests -- Search for Name match with city
    city_search = request_city_hobby(infos_list, "city")
    # More Advanced requests -- Search for Name match with department
    department_search = request_city_hobby(infos_list, "department")
    # More Advanced requests -- Search for Name match with hobby
    hobby_search = request_city_hobby(infos_list, "hobby")

    return [[dual_name_request, triple_name_request, pseudo_request, phone_number_request, ip_adress_request,
             index_of_request], [txt_search, pdf_search, doc_search], [city_search, department_search, hobby_search]]


def list_processing(result_links):
    # Compare all of recovered urls and do the maths

    print("Traitement des liens en cours...\n")
    # Make a simple ist with all urls
    total_simple_urls_list = []
    for urls_list in result_links:
        for url in urls_list:
            total_simple_urls_list.append(url)

    # Use de collections.most_common() function to detect NB_LINKS links which are more common
    most_common_urls = Counter(total_simple_urls_list).most_common(NB_LINKS)
    for element in most_common_urls:
        print("Url : " + element[0] + " -> nombre d'apparitions : " + str(element[1]))

    print("\nSauvegarde en cours...")
    file_d = open("Result/RevelantList.txt", "w")
    file_d.write(str(most_common_urls))
    file_d.close()


def do_the_request(list_of_requests_list):
    print("Suppression des résultats précédents et initialisation du dossier...\n")
    os.system("rm -rf Result")
    os.system("mkdir Result && mkdir Result/All_Pictures/ && mkdir Result/Images/")

    driver = webdriver.Chrome(options=open_browser())
    driver.get("http://www.google.com/search?q=test")  # => Do the first request

    # First part : make and collect all requests

    simple_requests_list = list_of_requests_list[0]
    filetype_requests_list = list_of_requests_list[1]
    advanced_request_list = list_of_requests_list[2]
    result_links = []
    links_counter = 0

    print("\nDémarrage de la recherche commune...\n")
    # First round : Simple requests
    for request in simple_requests_list:
        query = request[0]
        links = []
        n_pages = NUMBER_OF_PAGES
        for page in range(1, n_pages):
            if query.find("\"\"") == -1:
                url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10) + "&filter=0"
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                search = soup.find_all('div', class_="yuRUbf")
                for h in search:
                    links.append(h.a.get('href'))
                # Downloading pictures
                driver.get('http://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl&q=' + query)
                box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
                box.send_keys(Keys.ENTER)
                print("Requête terminée : Image téléchargée !")
                driver.save_screenshot("Result/Images/" + query+ ".png")
                # End downloading pictures
        result_links.append(links)
        links_counter += len(links)
    print("------------ Requêtes communes terminées. (" + str(links_counter) + ") ------------\n")
    links_counter = 0
    print("\nDémarrage de la recherche de fichiers...\n")

    # Second round : filetype request
    for file_type_request_elm in filetype_requests_list:
        for file_type_elm in file_type_request_elm:
            for request in file_type_elm:
                query = request[0]
                links = []
                n_pages = NUMBER_OF_PAGES
                for page in range(1, n_pages):
                    # Verification that the query field is not empty
                    if query.find("\"\"") == -1:
                        url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10) + "&filter=0"
                        driver.get(url)
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        search = soup.find_all('div', class_="yuRUbf")
                        for h in search:
                            links.append(h.a.get('href'))
                result_links.append(links)
                links_counter += len(links)

    print("------------ Recherche de fichiers terminée. (" + str(links_counter) + ") ------------\n")
    links_counter = 0
    print("\nDémarrage de la recherche par mots clés...\n")

    # Third round : hobbies, cities and department search
    for file_type_request_elm in advanced_request_list:
        for element in file_type_request_elm:
            for request in element:
                query = request[0]
                links = []
                n_pages = NUMBER_OF_PAGES
                for page in range(1, n_pages):
                    # Verification that the query field is not empty
                    if query.find("\"\"") == -1:
                        url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10) + "&filter=0"
                        driver.get(url)
                        soup = BeautifulSoup(driver.page_source, 'html.parser')
                        search = soup.find_all('div', class_="yuRUbf")
                        for h in search:
                            links.append(h.a.get('href'))
                result_links.append(links)
                links_counter += len(links)

    print("------------ Recherche par mots-clés terminée. (" + str(links_counter) + ") ------------\n")
    links_counter = 0
    print("\nDémarrage de la recherche des images sur des serveurs...\n")

    # Fourth round : Download all Pictures on Index Of servers
    query = simple_requests_list[5][0]
    links = []
    n_pages = NUMBER_OF_PAGES
    count_folder = 0
    for page in range(1, n_pages):
        # Verification that the query field is not empty
        if query.find("\"\"") == -1:
            url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 10) + "&filter=0"
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            search = soup.find_all('div', class_="yuRUbf")
            for h in search:
                print("\nTéléchargement en cours...\n")
                os.system("mkdir Result/pictures_folder_n_" + str(count_folder))
                os.system("wget -r -A jpeg,jpg,bmp,gif,png --no-parent \"" + h.a.get(
                    'href') + "\" -P Result/pictures_folder_n_" + str(count_folder) + " >> log.txt")
                count_folder = count_folder + 1
    # Extraction des images
    os.system("cd Result && find . -type f -name \"*jpeg\" -exec cp {} All_Pictures/ \\; && cd .. >> log.txt")
    os.system("cd Result && find . -type f -name \"*jpg\" -exec cp {} All_Pictures/ \\; && cd .. >> log.txt")
    os.system("cd Result && find . -type f -name \"*bmp\" -exec cp {} All_Pictures/ \\; && cd .. >> log.txt")
    os.system("cd Result && find . -type f -name \"*gif\" -exec cp {} All_Pictures/ \\; && cd .. >> log.txt")
    os.system("cd Result && find . -type f -name \"*png\" -exec cp {} All_Pictures/ \\; && cd .. >> log.txt")
    # Sauvegarde
    print("\nSauvegarde en cours...")
    file_d = open("Result/AllUrls.txt", "w")
    file_d.write(str(result_links))
    file_d.close()

    # Second part : Urls Lists processing

    list_processing(result_links)
    driver.close()

    # Switching off the software
    print("Fermeture en cours...")


def open_browser():
    global browser
    option = webdriver.ChromeOptions()
    option.add_argument('--disable-blink-features=AutomationControlled')  # Delete Automation detection flag
    option.add_argument("user-data-dir=selenium")  # Store cookies
    # option.add_argument("window-size=1920,1080")
    option.add_argument("--mute-audio")
    option.add_argument("--disable-logging")
    option.add_argument("--log-level=3")
    option.add_argument("--output=/dev/null")
    option.add_argument('--headless')
    option.add_argument("--disable-gpu")
    option.add_argument("--disable-site-isolation-trials")
    option.add_argument("--enable-low-end-device-mode")
    option.add_argument("--max_old_space_size=330")
    option.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")
    return option  # Apply previous options

show_me()
infos = take_infos()
requests_list = list_requests(infos)
do_the_request(requests_list)
