# -*- encoding:utf-8 -*-
"""
@ Created by Seven on  2018/06/23 
"""
from flask import jsonify

from app.validators.forms import SearchForm


def search(model):
    form = SearchForm().validate_for_api()
    q = form.q.data
    s_data = '%' + q + '%'
    data = model.query.filter(
        (model.title.like(s_data))).all()
    new_list = {
        'error_code': 0,
        'list': data
    }
    return jsonify(new_list)

# __exact        精确等于 like 'aaa'
# __iexact       精确等于 忽略大小写 ilike 'aaa'
# __contains     包含  like '%aaa%'
# __icontains    包含  忽略大小写 ilike '%aaa%'，但是对于sqlite来说，contains的作用效果等同于icontains。
# __gt           大于
# __gte          大于等于
# __lt           小于
# __lte          小于等于
# __in           存在于一个list范围内
# __startswith   以...开头
# __istartswith  以...开头 忽略大小写
# __endswith     以...结尾
# __iendswith    以...结尾，忽略大小写
# __range        在...范围内
# __year         日期字段的年份
# __month        日期字段的月份
# __day          日期字段的日# __isnull       = True / False
