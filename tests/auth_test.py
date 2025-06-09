import logging
import time

from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.coworking_page import CoworkingPage

def test_login_success(driver_chrome):
    auth_page = AuthPage(driver_chrome)
    home_page = HomePage(driver_chrome)
    coworking_page = CoworkingPage(driver_chrome)

    auth_page.enter_phone_number("998976960110")
    auth_page.click_next_btn()
    auth_page.enter_password("Maha4us905ejje")
    auth_page.click_next_btn()

    try:
        auth_page.click_dropdown()
        auth_page.click_finish_btn()
    except Exception as e:
        logging.error("Ошибка при клике на кнопку сессий", exc_info=True)

    home_page.click_coworking_btn()
    home_page.click_reserve_btn()
    coworking_page.click_second_branch()
    time.sleep(2)
    coworking_page.click_choose_btn()
    coworking_page.click_next_btn()
    coworking_page.click_second_date()
    coworking_page.click_choose_group()
    coworking_page.click_choose_radio_btn_group()
    time.sleep(2)
    coworking_page.click_choose_group_btn()
    coworking_page.click_choose_time()
    coworking_page.click_first_element()
    coworking_page.click_second_element()
    coworking_page.click_choose_time_btn()
    time.sleep(2)
    coworking_page.click_choose_place()
    coworking_page.click_choose_number_place()
    coworking_page.click_choose_place_btn()
    coworking_page.click_send_btn()


    # home_page.click_profile_icon()
    # home_page.click_exit_btn()
    # home_page.click_confirm_exit_btn()


# def test_login_fail(driver_chrome):
#     auth_page = AuthPage(driver_chrome)
#
#     try:
#         auth_page.enter_phone_number("998335814123")
#         auth_page.click_next_btn()
#         auth_page.enter_password("qweqweqwe")
#         auth_page.click_next_btn()
#     except Exception as e:
#         logging.error("Success invalid test", exc_info=True)