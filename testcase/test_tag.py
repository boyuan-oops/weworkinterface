#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from jsonpath import jsonpath
from api.tag import Tag
from api.wework import WeWork
import allure


@allure.feature('tag_interfaces')
class TestTag():

    def setup_class(self):
        wework = WeWork()
        self.token = wework.get_token()
        self.tag = Tag()

    def test_create_tag(self):
        r = self.tag.create_tag(self.token)
        taglist = self.tag.get_tag_list(self.token)
        print(taglist)
        tagname = jsonpath(taglist, "$..tagname")
        assert "UI" in tagname

    def test_update_tag(self):
        r = self.tag.update_tag(self.token)
        taglist = self.tag.get_tag_list(self.token)
        tagname = jsonpath(taglist, "$..tagname")
        assert "UI design" in tagname

    def test_delete_tag(self):
        r = self.tag.delete_tag(self.token)
        taglist = self.tag.get_tag_list(self.token)
        print(taglist)
        assert len(taglist["taglist"]) == 0
