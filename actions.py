from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction

import requests

urlcountry = "https://newsapi.org/v2/top-headlines?country="
apikey="9d96ee122a9f420fa0edd9930f7aa6f3"
urlsource="http://newsapi.org/v2/top-headlines?sources="
urltop="https://newsapi.org/v2/everything?q="

location = {'ARGENTINA':'ar','AUSTRALIA':'au','AUSTRIA':'at','BELGIUM':'be','BRAZIL':'br','BULGARIA':'bg','CANADA':'ca','CHINA':'cn','COLOMBIA':'co','CUBA':'cu','CZECH REPUBLIC':'cz','EGYPT':'eg','FRANCE':'fr','GERMANY':'de','GREECE':'gr','HONG KONG':'hk','HUNGARY':'hu','INDIA':'in','INDONESIA':'id','IRELAND':'ie','ISRAEL':'il','ITALY':'it','JAPAN':'jp','LATVIA':'lv','LITHUANIA':'lt','MALAYSIA':'my','MEXICO':'mx','MOROCCO':'ma','NETHERLANDS':'nl','NEW ZEALAND':'nz','NIGERIA':'ng','NORWAY':'no','PHILIPPINES':'ph','POLAND':'pl','PORTUGAL':'pt','ROMANIA':'ro','RUSSIA':'ru','SAUDI ARABIA':'sa','SERBIA':'rs','SINGAPORE':'sg','SLOVAKIA':'sk','SLOVENIA':'si','SOUTH AFRICA':'za','SOUTH KOREA':'kr','SWEDEN':'se','SWITZERLAND':'ch','TAIWAN':'tw','THAILAND':'th','TURKEY':'tr','UAE':'ae','UKRAINE':'ua','UNITED KINGDOM':'gb','UK':'gb','UNITED STATED':'us','VENEZUELA':'ve'}


def newscountry(country):
	urlnews=urlcountry
	country = country.upper()
	country = location[country]
	url=urlnews+country
	urlapi=url+'&'+'apiKey='
	urlcoun=urlapi+apikey
	response=requests.get(urlcoun)
	data=response.json()
	return data
	
	
def newsapi(country):
	urlnews=urlcountry
	url=urlnews+country
	urlapi=url+'&'+'apiKey='
	urlcoun=urlapi+apikey
	response=requests.get(urlcoun)
	data=response.json()
	return data


def sourcenews(source):
  
	urlnews=urlsource
	url=urlnews+source
	urlapi=url+'&'+'apiKey='
	urlsour=urlapi+apikey
	response=requests.get(urlsour)
	data=response.json()
	return data

def topicnews(topic):
  
  urlnews=urltop
  url=urlnews+topic
  urlapi=url+'&'+'apiKey='
  urlcoun=urlapi+apikey
  response=requests.get(urlcoun)
  data=response.json()
  return data




class NewsBBc(Action):
   
 def name(self):
  return "action_news_bbc"

 def run(self,dispatcher,tracker,domain):
  data=sourcenews("bbc-news")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }
    dispatcher.utter_custom_json(gt)    
  return []  

class NewsABC(Action):
 
 def name(self):
  return "action_news_abc"

 def run(self,dispatcher,tracker,domain):
  data=sourcenews("abc-news")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }
    dispatcher.utter_custom_json(gt)    
  return []  


class NewsABC(Action):
     
 def name(self):
  return "action_news_cnn"

 def run(self,dispatcher,tracker,domain):  
  data=sourcenews("cnn")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }
    dispatcher.utter_custom_json(gt)    
  return []  


class newsHeadlineus(Action):  
 def name(self):
  return "action_news_headline_us"

 def run(self,dispatcher,tracker,domain):
  """displaying news headlines of us"""  
  data=newsapi("us")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }  
    dispatcher.utter_custom_json(gt)
  return []


class NewsheadlineIndia(Action): 
 def name(self):
  return "action_news_headline_india"

 def run(self,dispatcher,tracker,domain):
  data=newsapi("in")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        } 
    dispatcher.utter_custom_json(gt)
  return []

class NewsHeadlineAustralia(Action):
 def name(self):
  return "action_news_headline_au"

 def run(self,dispatcher,tracker,domain):
  data=newsapi("au")
  leng=len(data)
  for i in range(leng):	
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        } 
    dispatcher.utter_custom_json(gt)
  return []




class SearchForm(FormAction):
   
 def name(self): 
  return "search_form"

 def required_slots(self,tracker) -> List[Text]:
     
  return ["topic"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
    return {
            "topic": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    
    return []

class action_news_country(Action):
 def name(self):
  return "action_news_country"

 def run(self,dispatcher,tracker,domain): 
  country=tracker.get_slot("country")
  '''location = tracker.get_slot("country")'''
  data=newscountry(country)
  leng=len(data)
  for i in range(leng): 
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }
    dispatcher.utter_custom_json(gt)    
  return [] 


class NewsTopic(Action):
 def name(self):
  return "action_news_search"

 def run(self,dispatcher,tracker,domain):
  topics=tracker.get_slot("topic")  
  name = tracker.get_slot("name")
  '''location = tracker.get_slot("country")'''
  data=topicnews(topics)
  leng=len(data)
  for i in range(leng): 
    gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": data['articles'][i]['title'],
                            "image_url":data['articles'][i]['urlToImage'],
                            "subtitle": data['articles'][i]['description'],
                            "buttons": [
                                {
                                    "type": "web_url",
                                    "url": data['articles'][i]['url'],
                                    "title": "Read More"
                                },
                            ]
                        },
                    ]
                }
            }
        }
    dispatcher.utter_custom_json(gt)    
  return []      
