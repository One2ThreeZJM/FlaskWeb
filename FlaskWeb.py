#!/usr/bin/evn python
# coding: UTF-8

from flask import Flask, render_template, request
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Required, Length, Email, Regexp, EqualTo

from flask_bootstrap import Bootstrap
import base64
import re
import json

app = Flask(__name__)
# app.config.from_object('config')
bootstrap = Bootstrap(app)


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)


def upEncode(data, chars, chars1):
    CHARS = chars
    CHARS1 = chars1
    str = base64.b64encode(data)
    str = multiple_replace(data, dict(zip(CHARS1, CHARS)))
    str = base64.b64decode(str)

    return json.dumps(json.loads(str), sort_keys=True,
                      indent=2, ensure_ascii=False)


@app.route('/', methods=['GET', 'POST'])
@app.route('/salmonads', methods=['GET', 'POST'])
def index():
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    CHARS1 = 'ceM7uVqJHjxLv/NGmR8Sib31AhokWsZnDlwQ+YdPKB9EOUXFC4t5aIpr0fg2Tyz6'
    data = request.form.get('data')
    if data is None or data.strip() == "":
        return render_template('index.html', placeholder="")
    else:
        try:
            result = upEncode(data, CHARS, CHARS1)
            return render_template('index.html', data=data, content=result)
        except Exception, e:
            try:
                result = base64.b64decode(data)
                result = unicode(result, "utf-8")
                return render_template('index.html', data=data, content=result)
            except Exception, e:
                return render_template('index.html', data=data, content=e)


@app.route('/mobpower', methods=['GET', 'POST'])
def mobpower():
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    CHARS1 = 'BFkEr0JIvT7R8x3LNstC4UXa6QO92zYdMWnhbeyK5fjSqGumlpZVciPHADw1go+/'
    data = request.form.get('data')
    if data is None or data.strip() == "":
        return render_template('mobpower.html', placeholder="")
    else:
        try:
            result = upEncode(data, CHARS, CHARS1)
            # result = json.loads(result)
            # result = json.dumps(json.loads(result), sort_keys=True,
            #                     indent=2, ensure_ascii=False)

            return render_template('mobpower.html', data=data, content=result)
        except Exception, e:
            CHARS1 = 'xZnV5k+DvSoajc7dRzpHLYhJ46lt0U3QrWifGyNgb9P1OIKmCEuq8sw/XMeBAT2F'
            try:
                result = upEncode(data, CHARS, CHARS1)
                return render_template('mobpower.html', data=data, content=result)
            except Exception, e:
                return render_template('mobpower.html', data=data, content=e)


@app.route('/uparpu', methods=['GET', 'POST'])
def uparpu():
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    CHARS1 = 'dMWnhbeyKr0J+IvLNOx3BFkEuml92/5fjSqGT7R8pZVciPHAstC4UXa6QDw1gozY'
    data = request.form.get('data')
    if data is None or data.strip() == "":
        return render_template('uparpu.html', placeholder="")
    else:
        try:
            result = upEncode(data, CHARS, CHARS1)
            return render_template('uparpu.html', data=data, content=result)
        except Exception, e:
            CHARS1 = 'xZnV5k+DvSoajc7dRzpHLYhJ46lt0U3QrWifGyNgb9P1OIKmCEuq8sw/XMeBAT2F'
            try:
                result = upEncode(data, CHARS, CHARS1)
                return render_template('uparpu.html', data=data, content=result)
            except Exception, e:
                CHARS1 = 'dMWnhbeyKr0JIvLNOx3BFkEuml92Y5fjSqGT7R8pZVciPHAstC4UXa6QDw1goz+/'
                try:
                    result = upEncode(data, CHARS, CHARS1)
                    return render_template('uparpu.html', data=data, content=result)
                except Exception,e:
                    return render_template('uparpu.html', data=data, content=e)



if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port=7777)
