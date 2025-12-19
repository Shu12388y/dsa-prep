
samStr = "OpenAI   creates amazing   AI   models  "


def reverese_words(s:str)->str:
    resp = []
    resStr = ''
    res = s.split(" ")
    for i in res:
        if i != '':
            resp.append(i)  
            
    for i in reversed(resp):
        resStr += i
        resStr += ' '
    return resStr
reverese_words(samStr)