# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


import gc

import csv
import urllib.request
import ssl
import json
import requests
import os
import html
import random
import pathlib

# class action_greet_name(Action):
#
#     def name(self) -> Text:
#         return "action_greet_name"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(template = "utter_greet_name", name = "Aimee")
#
#         return []

# def load_faq():
#     q_list = []
#     a_list = []
#
#     filepath = str(pathlib.Path().absolute()) + '/crawler/data/info_faq.txt'.replace('/', os.sep)
#     with open(filepath) as fp:
#         line = fp.readline()
#         cnt = 1
#         while line:
#             # Process
#             print("Process line ", line)
#             q_list.append( line.split("|")[0].replace("\n",""))
#             a_list.append( line.split("|")[1].replace("\n",""))
#             line = fp.readline()
#             cnt += 1
#     return q_list,a_list
#
#
#
# q_list,a_list=load_faq()
# print("Loaded", len(q_list))

# --------------------------------------------------------------------KHÁI NIỆM-----------------------------------------------
# Khái niệm đồ họa máy tính
class act_khainiem_dohoa(Action):

    def name(self) -> Text:
        return "act_khainiem_dohoa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/khainiemdohoa.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Khái niệm không gian màu
class act_khainiem_khonggianmau(Action):

    def name(self) -> Text:
        return "act_khainiem_khonggianmau"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/khainiemkhonggianmau.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/khonggianmau.PNG")

        return []
# Khái niệm đồ họa con rùa
class act_khainiem_dohoaconrua(Action):

    def name(self) -> Text:
        return "act_khainiem_dohoaconrua"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/khainiemdohoaconrua.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Khái niệm đồ họa điểm
class act_khainiem_dohoadiem(Action):

    def name(self) -> Text:
        return "act_khainiem_dohoadiem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/khainiemdohoadiem.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/khainiem-dohoadiem.PNG")

        return []
# Khái niệm đồ họa vector
class act_khainiem_dohoavector(Action):

    def name(self) -> Text:
        return "act_khainiem_dohoavector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/khainiemdohoavector.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Khái niệm các kỹ thuật đồ họa
class act_khainiem_kythuatdohoa(Action):

    def name(self) -> Text:
        return "act_khainiem_kythuatdohoa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/kythuatdohoa.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/cackythuatdohoa.PNG")

        return []
# Khái niệm độ phân giải
class act_khainiem_dophangiai(Action):

    def name(self) -> Text:
        return "act_khainiem_dophangiai"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/khainiemdophangiai.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/khainiem-dophangiai.PNG")

        return []
# Khái niệm tô màu đơn giản
class act_khainiem_thuattoan_tomaudongian(Action):

    def name(self) -> Text:
        return "act_khainiem_thuattoan_tomaudongian"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/khainiem-thuattoan-tomaudongian.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Khái niệm tô màu đơn dòng quét
class act_khainiem_thuattoan_tomaudongquet(Action):

    def name(self) -> Text:
        return "act_khainiem_thuattoan_tomaudongquet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/khainiem-tomau-dongquet.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Khái niệm tô màu đơn dòng quét
class act_khainiem_thuattoan_tomauduongbien(Action):

    def name(self) -> Text:
        return "act_khainiem_thuattoan_tomauduongbien"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/khainiem-tomau-duongbien.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Khái niệm thuật toán cắt hình
class act_khainiem_thuattoan_cathinh(Action):

    def name(self) -> Text:
        return "act_khainiem_thuattoan_cathinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/khainiem-thuattoan-cathinh.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# --------------------------------------------------------------------ƯU ĐIỂM-----------------------------------------------
# Ưu điểm kỹ thuật đồ họa điểm
class act_uudiem_dohoadiem(Action):

    def name(self) -> Text:
        return "act_uudiem_dohoadiem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/uudiem-dohoadiem.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/uu-diem-dohoadiem.PNG")

        return []
#Ưu điểm kỹ thuật đồ họa vector
class act_uudiem_dohoavector(Action):

    def name(self) -> Text:
        return "act_uudiem_dohoavector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/uudiem-dohoavector.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/uudiem-dohoavector.PNG")

        return []
#Ưu điểm tô màu đơn giản
class act_uudiem_tomaudongian(Action):

    def name(self) -> Text:
        return "act_uudiem_tomaudongian"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/uudiem-tomaudongian.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# --------------------------------------------------------------------NHƯỢC ĐIỂM-----------------------------------------------
# Nhược điểm kỹ thuật đồ họa điểm
class act_nhuocdiem_dohoadiem(Action):

    def name(self) -> Text:
        return "act_nhuocdiem_dohoadiem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/nhuocdiem-dohoadiem.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/nhuocdiem-dohoadiem.PNG")

        return []
# Nhược điểm kỹ thuật đồ họa vector
class act_nhuocdiem_dohoavector(Action):

    def name(self) -> Text:
        return "act_nhuocdiem_dohoavector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/nhuocdiem-dohoavector.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
#Nhược điểm tô màu đơn giản
class act_nhuocdiem_tomaudongian(Action):

    def name(self) -> Text:
        return "act_nhuocdiem_tomaudongian"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/nhuocdiem-tomaudongian.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# --------------------------------------------------------------------SO SÁNH----------------------------------------------
# So sánh đồ họa điểm và vector
class act_sosanh_dohoa_diem_vector(Action):

    def name(self) -> Text:
        return "act_sosanh_dohoa_diem_vector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/sosanh-dohoa-diem-vector.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/sosanh-dohoa.PNG")

        return []
# --------------------------------------------------------------------ỨNG DỤNG-----------------------------------------------
# Ứng dụng kỹ thuật đồ họa
class act_ungdung_kythuatdohoa(Action):

    def name(self) -> Text:
        return "act_ungdung_kythuatdohoa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/ungdung-kythuatdohoa.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/ungdung-kythuatdohoa.PNG")

        return []
# Ứng dụng Phép biến đổi 2 chiều
class act_ungdung_phepbiendoi_haichieu_coban(Action):

    def name(self) -> Text:
        return "act_ungdung_phepbiendoi_haichieu_coban"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/ungdung-phepbiendoi-haichieu-coban.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/ungdung-phepbiendoi.PNG")

        return []
# --------------------------------------------------------------------KHÁC-----------------------------------------------
# Quy trình đồ họa
class act_quytrinh_dohoa(Action):

    def name(self) -> Text:
        return "act_quytrinh_dohoa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/quytrinh-dohoa.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Phần mềm đồ họa điểm
class act_phanmem_dohoadiem(Action):

    def name(self) -> Text:
        return "act_phanmem_dohoadiem"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/phanmem-dohoadiem.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/photoshop.jpg")

        return []
# Phần mềm đồ họa vector
class act_phanmem_dohoavector(Action):

    def name(self) -> Text:
        return "act_phanmem_dohoavector"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/phanmem-dohoavector.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/adobe.jpg" )

        return []
# Nguyên tắc phối màu
class act_nguyentac_phoimau(Action):

    def name(self) -> Text:
        return "act_nguyentac_phoimau"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/nguyentac-phoimau.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Các loại không gian màu
class act_loai_khonggianmau(Action):

    def name(self) -> Text:
        return "act_loai_khonggianmau"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/loai-khonggianmau.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# RGB
class act_loai_rgb(Action):

    def name(self) -> Text:
        return "act_loai_rgb"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/loai-rgb.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/rgb.PNG")

        return []
# HSL
class act_loai_hsl(Action):

    def name(self) -> Text:
        return "act_loai_hsl"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/loai-hsl.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/hsl.PNG")

        return []
# HSV
class act_loai_hsv(Action):

    def name(self) -> Text:
        return "act_loai_hsv"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/loai-hsv.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/hsv.PNG")

        return []
# CMY
class act_loai_cmy(Action):

    def name(self) -> Text:
        return "act_loai_cmy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/loai-cmy.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/cmy.PNG")

        return []
# Chuyển đổi không gian màu
class act_chuyendoi_khonggianmau(Action):

    def name(self) -> Text:
        return "act_chuyendoi_khonggianmau"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/chuyendoi-khonggianmau.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/chuyendoi-khonggianmau.PNG")

        return []
# Hệ tọa độ
class act_loai_hetoado(Action):

    def name(self) -> Text:
        return "act_loai_hetoado"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/loai-hetoado.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Đối tượng đồ họa cơ sở
class act_loai_doituong_dohoacoso(Action):

    def name(self) -> Text:
        return "act_loai_doituong_dohoacoso"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/loai-doituong-dohoacoso.txt'.replace('/', os.sep), mode='r', encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Thuật toán tô màu
class act_loai_thuattoantomau(Action):

    def name(self) -> Text:
        return "act_loai_thuattoantomau"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/loai-thuattoantomau.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
# Phép biến đổi 2 chiều
class act_phepbiendoi_haichieu_coban(Action):

    def name(self) -> Text:
        return "act_phepbiendoi_haichieu_coban"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/phepbiendoi-haichieu-coban.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it, image="https://raw.githubusercontent.com/luongthanhle/data-image/main/phepbiendoi.PNG")

        return []
# Loại thuật toán cắt hình
class act_loai_thuattoan_cathinh(Action):

    def name(self) -> Text:
        return "act_loai_thuattoan_cathinh"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        file = open(str(pathlib.Path().absolute()) + '/file-data/data/loai-thuattoan-cathinh.txt'.replace('/', os.sep), mode='r',
                    encoding="utf-8")

        # read all lines at once
        all_of_it = file.read()

        # close the file
        file.close()

        dispatcher.utter_message(text=all_of_it)

        return []
