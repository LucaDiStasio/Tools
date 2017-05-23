import requests

# Getting the key from tab Keys on Azure portal
key = "cc19c0350a3643a9b7214ee0ece36ad5" 

# For gettting access token
# url4authentication = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken?Subscription-Key=%s' % key
# resp4authentication = requests.post(url4authentication)

url4authentication = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
headers4authentication = {'Ocp-Apim-Subscription-Key': key}
resp4authentication = requests.post(url4authentication, headers=headers4authentication)
token = resp4authentication.text

# For calling Translate API
#text = "happy time"
text = """
Everything seems to go smoothly, and I get a 200 response (which I gather means success), yet when I try to look at the text in the response, hundreds of lines of obscure html are printed out. After looking through a few hundred of the lines (which were, for the most part, listing the dozens of languages I chose NOT to translate my text into) I couldn't find any actually translated text. All of the examples that Microsoft has on their github use the outdated DataMarket website that Microsoft is in the process of discontinuing as the authorization link. Moreover, I couldn't find any examples of the API actually being used - they were all just authorization examples. Using the token with their 'Try it Out' example gives me the correct result (though as an xml file?), so this is definitely a python problem.

So, has anyone used this service before and mind shedding some light on how to interpret or unwrap this response?

Thank you!
"""
come = "en"
to = "fr"
# url4translate = 'https://api.microsofttranslator.com/v2/http.svc/Translate?appid=Bearer %s&text=%s&from=%s&to=%s' % (token, text, come, to)
# headers4translate = {'Accept': 'application/xml'}
# resp4translate = requests.get(url4translate, headers=headers4translate)
url4translate = 'https://api.microsofttranslator.com/v2/http.svc/Translate'
params = {'appid': 'Bearer '+token, 'text': text, 'from': come, 'to': to}
headers4translate = {'Accept': 'application/xml'}
resp4translate = requests.get(url4translate, params=params, headers=headers4translate)
print(resp4translate.find('string').text)