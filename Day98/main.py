# -----------------------------------------------------------------------------------
# File name  : t264_uart_html.py
# Company    : NVIDIA
# Group      : Silicon Solution Group (SSG)
# Site       : TDC (Taipei)
# -----------------------------------------------------------------------------------
# Revision History :
# Date       | Version | PIC    | Discription
# 2024.03.18 | 0       | Jim Li | Initial version
# 2024.04.24 | 1       | Jim Li | search html in the folder
# 2024.04.24 | 1       | Jim Li | fix search fail case
# 2024.04.24 | 1       | Jim Li | fix no html case
# -----------------------------------------------------------------------------------

import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from secret_key import NVIDIA_HTML_FOLDER, NVIDIA_REPORT_FOLDER, NVIDIA_REPORT_FILE, NVIDIA_URL
'''
Requirement:
    pip install selenium
Usage:
    Need to download the html file first and put in the html_folder
    You have to key in the account and password in 10 secs.
    You could change the loggin time by changing TIME_FOR_LOGIN.
    You could change the search time by changing TIME_FOR_SEARCH.
    Don't open csv file while executing this program.
'''
TIME_FOR_LOGIN = 10 # 10 secs
TIME_FOR_SEARCH = 2 #  2 secs
html_folder = NVIDIA_HTML_FOLDER
report_folder = NVIDIA_REPORT_FOLDER
report_file = NVIDIA_REPORT_FILE
URL_TEGRA = NVIDIA_URL

target_strings = [
    "Register_A",
    "Register_B",
    "Register_C",
    "Register_D",
    "Register_E",
    "Register_F",
    "Register_G",
    "Register_H",
    "Register_I",
    "Register_J",
    "Register_K",
]

class bcolors:
    RED          = '\033[91m'
    GREEN        = '\033[92m'
    YELLOW       = '\033[93m'
    BLUE         = '\033[94m'
    PURPLE       = '\033[95m'
    CYAN         = '\033[96m'
    BrightRED    = '\033[31;1m'
    BrightGREEN  = '\033[32;1m'
    BrightYELLOW = '\033[33;1m'
    BrightBLUE   = '\033[34;1m'
    BrightPURPLE = '\033[35;1m'
    BrightCYAN   = '\033[36;1m'
    WHITE        = '\033[0m'
    BOLD         = '\033[1m'
    UNDERLINE    = '\033[4m'

address_list = []
manual_html_list = []
offset_list = []
reset_list = []

def get_reg_reset(manual_html_list):
    found_target_line = False
    # print(file_path)
    for i in range(0, len(target_strings)):
        if manual_html_list[i] == "Not found":
            offset_value = "Not found"
            reset_value = "Not found"
        else:
            file_path = html_folder + manual_html_list[i]
            if not os.path.exists(file_path):
                # There is not html in the folder_path
                pass

            print(f"Searching {bcolors.BLUE}{target_strings[i]}{bcolors.WHITE} in the {bcolors.BLUE}{manual_html_list[i]}{bcolors.WHITE}")
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        # Check if the line contains the target string
                        if target_strings[i] in line:
                            # set flag
                            found_target_line = True
                        elif found_target_line and "Reset:" in line:
                            offset_value = line.split("<br>")[0].replace("Offset: ","")
                            reset_value = line.split("Reset: ")[-1].split(" (")[0]
                            break
            except:
                pass

        # clear flag or not found
        if found_target_line:
            found_target_line = False
        else:
            offset_value = "Not found"
            reset_value = "Not found"

        offset_list.append(offset_value)
        reset_list.append(reset_value)

    return offset_list, reset_list

def get_reg_address():
    # Keep Chrome browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL_TEGRA)

    details = driver.find_element(By.ID, value="details-button")
    details.click()

    proceed = driver.find_element(By.ID, value="proceed-link")
    proceed.click()

    for i in range(0,TIME_FOR_LOGIN):
        print(f"{bcolors.YELLOW}Counting {i}/10{bcolors.WHITE}")
        time.sleep(1)

    dropdown_element = driver.find_element(By.NAME, value="chip")
    select_t264 = Select(dropdown_element)
    select_t264.select_by_value("t264")

    for target_string in target_strings:
        print(f"Searching the address of {bcolors.BLUE}{target_string}{bcolors.WHITE} in the tegra-manuals.")
        register = driver.find_element(By.NAME, value="register")
        register.clear()
        register.send_keys(target_string, Keys.ENTER)

        search = driver.find_element(By.CSS_SELECTOR, value="input[type='submit']")
        search.click()

        for i in range(0,TIME_FOR_SEARCH):
            print(i)
            time.sleep(1)

        result = driver.find_element(By.CSS_SELECTOR, value="pre")
        result_text = result.text
        print(result_text)
        if "Did not find" in result_text:
            print(f"{bcolors.RED}Search fail.{bcolors.WHITE}")
            absolute_address = "Not found"
            manual_html = "Not found"
        else:
            print(f"{bcolors.GREEN}Search complete.{bcolors.WHITE}")
            absolute_address = result_text.split("Absolute address    = ")[-1].split(" ")[0]
            manual_html = result.find_element(By.CSS_SELECTOR, value="a").text

        # print(absolute_address)
        # print(manual_html)
        address_list.append(absolute_address)
        manual_html_list.append(manual_html)

    driver.quit()
    return address_list, manual_html_list

def uart_reg_csv(
    report_file,
    address_list,
    manual_html_list,
    offset_list,
    reset_list,
):
    with open(report_file, 'w') as file:
        file.write(f"Address, Manual html, Offset, Reset\n")
        for i in range(0, len(address_list)):
            file.write(
                f'{address_list[i]}, '
                f'{manual_html_list[i]}, '
                f'{offset_list[i]}, '
                f'{reset_list[i]}, '
                f'\n'
            )
    print(f"{bcolors.GREEN}Registers data successfully written to {report_file}.{bcolors.WHITE}")


def main():
    address_list, manual_html_list = get_reg_address()
    print(f"address_list = {address_list}")
    print(f"manual_html_list = {manual_html_list}")

    offset_list, reset_list = get_reg_reset(manual_html_list)
    print(f"offset_list = {offset_list}")
    print(f"reset_list = {reset_list}")

    print(f"lengh of register_list = {len(target_strings)}")
    print(f"lengh of address_list = {len(address_list)}")
    print(f"lengh of offset_list = {len(offset_list)}")
    print(f"lengh of reset_list = {len(reset_list)}")

    # print
    header_name = "Register"
    header_addr = "Address"
    header_html = "Html"
    header_offset = "Offset"
    header_reset = "Reset"
    print(f"-----------------------------------------------------------------")
    print(f"{bcolors.YELLOW}{header_name:<35} {header_addr:<12} {header_html:<17} {header_offset:<6} {header_reset:<10}{bcolors.WHITE}")
    for i in range(0, len(target_strings)):
        reg_name = target_strings[i]
        reg_addr = address_list[i]
        reg_html = manual_html_list[i].replace(".html","")
        reg_offset = offset_list[i]
        reg_reset = reset_list[i]
        print(f"{reg_name:<35} {reg_addr:<12} {reg_html:<17} {reg_offset:<6} {reg_reset:<10} ")

    # write in the csv file
    uart_reg_csv(
        report_file,
        address_list,
        manual_html_list,
        offset_list,
        reset_list,
    )


if __name__ == "__main__":
    main()