import time

import pytest
from pages.market_main_page import MarketPage


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
@pytest.mark.role("Admin")  # Добавляем кастомный маркер с ролью
class TestBuyAdmin:

    def test_buy_product(self, browser):
        p = MarketPage(browser)

        # p.add_to_cart()
        # p.checkout()
        print("ok")
        p.click_by_text("Текущие заявки")
        # p.is_element_present("#customersIds")
        input_id = p.wait_for_all_elements("#customersIds")
        p.click("#customersIds")
        p.get_element_dropdown_list("Test_MT")
        p.click_by_text("Применить")
        if p.is_element_present('[data-icon="check"]'):
            p.click('button.mr-1')
            print("click button")
            p.click_last_element('.ant-popover button')
        else:
            print("no button")
        time.sleep(5)
