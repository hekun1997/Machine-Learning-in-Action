# -*- coding: UTF-8 -*-

import requests as r
import random
import json


def getMidStr(txt, txt_start, txt_end='', seeks=0, seeke=0):
    try:
        if txt_end or seeks or seeke:
            pass
        else:
            raise 1
        s_1 = txt.find(txt_start)
        if s_1 == -1:
            raise 1
        l_1 = len(txt_start)
        if txt_end:
            s_2 = txt.find(txt_end, s_1)
            if s_1 == -1 or s_2 == -1:
                return False
            return txt[s_1 + l_1:s_2]
        if seeks:
            return txt[s_1 - seeks:s_1]
        if seeke:
            return txt[s_1 + l_1:s_1 + l_1 + seeke]
    except Exception:
        return '传参错误或未找到传参文本'


# while True:
if __name__ == '__main__':
    while True:
        hero = input("输入需要查询的英雄:")
        if hero == "":
            print("您输入无效")
        elif hero == "0":
            exit()
        else:
            source = r.get("http://s.wukongfenshen.com:9972/main/api/honour/wzpower/static/js/index.js?v=0." + str(
                random.randint(1000000, 9999999))).text
            _json = getMidStr(source, "var dictAll = ", "}}") + "}}"
            _json = json.loads(_json)
            try:
                _json[hero]
            except KeyError as reason:
                print("没有英雄:%s" % reason)
                continue
            title = _json[hero]["title"]
            content = _json[hero]["content"]
            print("英雄:%s" % title)
            content = str.replace(content, "<p><p>", "\n")
            content = str.replace(content, "<p> <p>", "\n")
            content = str.replace(content, "</p>", "\n")
            content = str.replace(content, "<p>", "")
            print(content + "\n")