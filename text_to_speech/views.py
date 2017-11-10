import json
import os
import sys
import urllib.request
import urllib.parse

from django.shortcuts import render


def send_to_naver(request):
    client_id = "Gae4R9qRa3pBYxPxh8rx"
    client_secret = "Zw7eh7BUG"

    if request.method == 'POST':

        text = request.POST.get('content')
        print(f'texttexttexttexttext : {text}')
        encText = urllib.parse.quote(text)

        # speaker, speed, 입력한 텍스트
        data = "speaker=mijin&speed=0&text=" + encText
        url = "https://openapi.naver.com/v1/voice/tts.bin"

        # request 만들기
        send_to_naver_request = urllib.request.Request(url)
        # header에 cliend_id, cliend_secret 추가
        send_to_naver_request.add_header("X-Naver-Client-Id", client_id)
        send_to_naver_request.add_header("X-Naver-Client-Secret", client_secret)

        print(f'requestrequestrequestrequestrequest : {send_to_naver_request.data}')

        response = urllib.request.urlopen(send_to_naver_request, data=data.encode('utf-8'))
        rescode = response.getcode()

        if (rescode == 200):
            print("TTS mp3 저장")
            response_body = response.read()
            with open('1111.mp3', 'wb') as f:
                f.write(response_body)
        else:
            print(f"Error Code: {rescode}")

    else:
        return render(request, 'index.html')


def load_tts_file(request):
    pass
