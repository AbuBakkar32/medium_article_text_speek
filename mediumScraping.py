import warnings

import bs4
import requests as req

warnings.simplefilter('ignore')

res = req.get('https://web.whatsapp.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
content = ''

if soup.find('article'):
    for i in soup.select('article'):
        content += i.getText()
        # print(i.getText())
    print(content)
else:
    print("This is not a medium article link..!")

######### Audio file generating
# from gtts import gTTS
# tts = gTTS(text = content, lang = 'en')
# tts.save("read.mp3")

'''
    https://devhints.io/js-speech,
    https://responsivevoice.org/,
    https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis
'''
