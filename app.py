# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:03:48 2021

@author: tpc
"""

from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('old_people_V2.html')

@app.route('/BanQiao')
def BanQiao_index():
    return render_template('old_people_BanQiao.html')

@app.route('/LuZhou')
def LuZhou_index():
    return render_template('old_people_LuZhou.html')

@app.route('/YiLan')
def YiLan_index():
    return render_template('old_people_YiLan.html')

@app.route('/HuaLian')
def HuaLian_index():
    return render_template('old_people_HuaLian.html')

@app.route('/YuLi')
def YuLi_index():
    return render_template('old_people_YuLi.html')

@app.route('/old_tpc',methods=['POST','GET'])
def old_tpc():
    if request.method == 'POST':
        Name = request.form.get('name')
        Phone = request.form.get('phone')
        Help = request.form.get('choose')
        
        if Help == '公廁急需協助':
            WC = request.form.get('wc')
            
            msg = "【台北所】" + "\n民眾: " + Name + "\n電話: " + Phone + "\n【" + Help + "】\n地點在 【" + WC + "】。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        else:
            msg = "【台北所】身心障礙停車處" + "\n民眾: " + Name + "\n電話: " + Phone + "\n需要  【" + Help + "】  的幫助。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        result = """
                    <!DOCTYPE html>
                    <html lang="zh" font-size: 100%;>
                    <head>
                    <title>台北區監理所愛心服務</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
                    </head>
                    <form method="post" action="/old_tpc">
                    <table align="center" valign="center">
                      <tr align="center" valign="center">
                      <td><label style="font-size:30px">已收到您的訊息，請稍後通知!</label></td>
                      </tr>
                    </table>
                    </form>
                    </html>
                    <!-- partial -->
                    </body>
                    </html>

                """
        
        return result

@app.route('/old_BanQiao',methods=['POST','GET'])
def old_BanQiao():
    if request.method == 'POST':
        Name = request.form.get('name')
        Phone = request.form.get('phone')
        Help = request.form.get('choose')
        
        if Help == '公廁急需協助':
            WC = request.form.get('wc')
            
            msg = "【板橋站】" + "\n民眾: " + Name + "\n電話: " + Phone + "\n【" + Help + "】\n地點在 【" + WC + "】。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        else:
            msg = "【板橋站】身心障礙停車處" + "\n民眾: " + Name + "\n電話: " + Phone + "\n需要  【" + Help + "】  的幫助。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        
        result = """
                    <!DOCTYPE html>
                    <html lang="zh" font-size: 100%;>
                    <head>
                    <title>板橋監理站愛心服務</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
                    </head>
                    <form method="post" action="/old_tpc">
                    <table align="center" valign="center">
                      <tr align="center" valign="center">
                      <td><label style="font-size:30px">已收到您的訊息，請稍後通知!</label></td>
                      </tr>
                    </table>
                    </form>
                    </html>
                    <!-- partial -->
                    </body>
                    </html>

                """
        
        return result

@app.route('/old_LuZhou',methods=['POST','GET'])
def old_LuZhou():
    if request.method == 'POST':
        Name = request.form.get('name')
        Phone = request.form.get('phone')
        Help = request.form.get('choose')
        
        if Help == '公廁急需協助':
            WC = request.form.get('wc')
            
            msg = "【蘆洲站】" + "\n民眾: " + Name + "\n電話: " + Phone + "\n【" + Help + "】\n地點在 【" + WC + "】。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        else:
            msg = "【蘆洲站】身心障礙停車處" + "\n民眾: " + Name + "\n電話: " + Phone + "\n需要  【" + Help + "】  的幫助。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        
        result = """
                    <!DOCTYPE html>
                    <html lang="zh" font-size: 100%;>
                    <head>
                    <title>蘆洲監理站愛心服務</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
                    </head>
                    <form method="post" action="/old_tpc">
                    <table align="center" valign="center">
                      <tr align="center" valign="center">
                      <td><label style="font-size:30px">已收到您的訊息，請稍後通知!</label></td>
                      </tr>
                    </table>
                    </form>
                    </html>
                    <!-- partial -->
                    </body>
                    </html>

                """
        
        return result

@app.route('/old_YiLan',methods=['POST','GET'])
def old_YiLan():
    if request.method == 'POST':
        Name = request.form.get('name')
        Phone = request.form.get('phone')
        Help = request.form.get('choose')
        
        if Help == '公廁急需協助':
            WC = request.form.get('wc')
            
            msg = "【宜蘭站】" + "\n民眾: " + Name + "\n電話: " + Phone + "\n【" + Help + "】\n地點在 【" + WC + "】。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        else:
            msg = "【宜蘭站】身心障礙停車處" + "\n民眾: " + Name + "\n電話: " + Phone + "\n需要  【" + Help + "】  的幫助。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        
        result = """
                    <!DOCTYPE html>
                    <html lang="zh" font-size: 100%;>
                    <head>
                    <title>宜蘭監理站愛心服務</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
                    </head>
                    <form method="post" action="/old_tpc">
                    <table align="center" valign="center">
                      <tr align="center" valign="center">
                      <td><label style="font-size:30px">已收到您的訊息，請稍後通知!</label></td>
                      </tr>
                    </table>
                    </form>
                    </html>
                    <!-- partial -->
                    </body>
                    </html>

                """
        
        return result

@app.route('/old_HuaLian',methods=['POST','GET'])
def old_HuaLian():
    if request.method == 'POST':
        Name = request.form.get('name')
        Phone = request.form.get('phone')
        Help = request.form.get('choose')
        
        if Help == '公廁急需協助':
            WC = request.form.get('wc')
            
            msg = "【花蓮站】" + "\n民眾: " + Name + "\n電話: " + Phone + "\n【" + Help + "】\n地點在 【" + WC + "】。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        else:
            msg = "【花蓮站】身心障礙停車處" + "\n民眾: " + Name + "\n電話: " + Phone + "\n需要  【" + Help + "】  的幫助。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        
        result = """
                    <!DOCTYPE html>
                    <html lang="zh" font-size: 100%;>
                    <head>
                    <title>花蓮監理站愛心服務</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
                    </head>
                    <form method="post" action="/old_tpc">
                    <table align="center" valign="center">
                      <tr align="center" valign="center">
                      <td><label style="font-size:30px">已收到您的訊息，請稍後通知!</label></td>
                      </tr>
                    </table>
                    </form>
                    </html>
                    <!-- partial -->
                    </body>
                    </html>

                """
        
        return result
    
@app.route('/old_YuLi',methods=['POST','GET'])
def old_YuLi():
    if request.method == 'POST':
        Name = request.form.get('name')
        Phone = request.form.get('phone')
        Help = request.form.get('choose')
        
        if Help == '公廁急需協助':
            WC = request.form.get('wc')
            
            msg = "【玉里分站】" + "\n民眾: " + Name + "\n電話: " + Phone + "\n【" + Help + "】\n地點在 【" + WC + "】。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        else:
            msg = "【玉里分站】身心障礙停車處" + "\n民眾: " + Name + "\n電話: " + Phone + "\n需要  【" + Help + "】  的幫助。"
            WEBHOOKURL ="https://discord.com/api/webhooks/1347361048566431755/Wz22jAbjw4l6x71QmuaX1he5fzk9lVPUNch65CZnYkkQhvp38LGovSUx8GIcSsym_sbR"

            response = requests.post(WEBHOOKURL, json={"content": msg})
        
        result = """
                    <!DOCTYPE html>
                    <html lang="zh" font-size: 100%;>
                    <head>
                    <title>花蓮監理站玉里分站愛心服務</title>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
                    </head>
                    <form method="post" action="/old_tpc">
                    <table align="center" valign="center">
                      <tr align="center" valign="center">
                      <td><label style="font-size:30px">已收到您的訊息，請稍後通知!</label></td>
                      </tr>
                    </table>
                    </form>
                    </html>
                    <!-- partial -->
                    </body>
                    </html>

                """
        
        return result

if __name__ == "__main__":
    app.run()