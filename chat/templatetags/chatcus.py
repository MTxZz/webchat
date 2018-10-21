#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import markdown
from django import template
from django.utils.html import format_html
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
import datetime
register = template.Library()
#url剪切标签
@register.filter
def chat_url(img):
    return '/static/'+img.name.split("/",maxsplit=1)[-1]
