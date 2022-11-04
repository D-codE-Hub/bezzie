# Copyright (c) 2022, D-codE and contributors
# For license information, please see license.txt
# 418abbefb15d68e
# 37d29fd6c37279d


import frappe

from erpnext.e_commerce.api import get_product_filter_data
from erpnext.e_commerce.shopping_cart.product_info import get_product_info_for_website
from erpnext.e_commerce.doctype.item_review.item_review import add_item_review, get_item_reviews, get_customer
# erpnext.e_commerce.variant_selector.utils.get_attributes_and_values
# erpnext.e_commerce.variant_selector.utils.get_next_attribute_and_values

# tesing api 
@frappe.whitelist(allow_guest=True)
def ping_pong(ping):
    if ping == 'ping':
        frappe.response["test"] = "pong"
    else:
        frappe.response["test"] = "please ping"

# list product with group search and using other filterss
@frappe.whitelist(allow_guest=True)
def get_product_listing(query_args):
    return get_product_filter_data(query_args)

# view product
@frappe.whitelist(allow_guest=True)
def get_product_info(item_code):
    return get_product_info_for_website(item_code)

@frappe.whitelist(allow_guest=True)
def get_product_review(web_item):
    return get_item_reviews(web_item) 


@frappe.whitelist()
def add_product_review(web_item,title,rating,comment):
    return add_item_review(web_item,title,rating,comment)