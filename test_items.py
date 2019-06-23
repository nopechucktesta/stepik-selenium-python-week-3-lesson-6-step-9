import pytest
# import time


class TestCatalogueItem(object):
    @pytest.mark.parametrize("item_link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_item_can_be_placed_into_cart(self, browser, item_link):
        browser.get(item_link)
        add_to_cart_button = browser.find_element_by_css_selector("button.btn-add-to-basket")
        # time.sleep(20)

        assert add_to_cart_button.is_enabled() is True, "Add to cart button should be enabled"

    # more tests to test catalogue item
