## news_us
* greet
  - utter_greetbot
* my_name_is{"name":"Pierre"}
  - slot{"name":"Pierre"}
  - utter_greetings
  - utter_greet
* news_headline
  - utter_newsheadline
* news_us
  - action_news_headline_us
  - utter_more_stories
* affirm
  - utter_greet
* news_headline
  - utter_newsheadline
* news_us
  - action_news_headline_us 
  - utter_more_stories
* deny
  - utter_goodbye

## news_india
* greet
  - utter_greetbot
* my_name_is{"name":"Rishi"}
  - slot{"name":"Rishi"}
  - utter_greetings
  - utter_greet
* news_headline
  - utter_newsheadline
* news_india
  - action_news_headline_india
  - utter_more_stories
* deny
  - utter_goodbye

## news_australia
* greet
  - utter_greetbot
* my_name_is{"name":"Soumya"}
  - slot{"name":"Soumya"}
  - utter_greetings
  - utter_greet
* news_headline
  - utter_newsheadline
* news_australia
  - action_news_headline_au
  - utter_more_stories
* affirm
  - utter_greet
* news_from_source
  - utter_newssource
* abc_news
  - action_news_abc
  - utter_more_stories
* deny
  - utter_goodbye

## bbc_news
* greet
  - utter_greetbot
* my_name_is{"name":"adiRaj"}
  - slot{"name":"adiraj"}
  - utter_greetings
  - utter_greet
* news_from_source
  - utter_newssource
* bbc_news
  - action_news_bbc
  - utter_more_stories
* deny
  - utter_goodbye

## abc_news
* greet
  - utter_greetbot
* my_name_is{"name":"sougata"}
  - slot{"name":"sougata"}
  - utter_greetings
  - utter_greet
* news_from_source
  - utter_newssource
* abc_news
  - action_news_abc
  - utter_more_stories
* deny
  - utter_goodbye

## cnn_news
* greet
  - utter_greetbot
* my_name_is{"name":"raju"}
  - slot{"name":"raju"}
  - utter_greetings
  - utter_greet
* news_from_source
  - utter_newssource
* cnn_news
  - action_news_cnn
  - utter_more_stories
* deny
  - utter_goodbye

## search_news:
* greet
  - utter_greetbot
* my_name_is{"name":"priya"}
  - slot{"name":"priya"}
  - utter_greetings
  - utter_greet
* search_news
  - search_form
  - action_news_search
  - utter_more_stories
* deny
  - utter_goodbye

## interactive_story_4
* greet
    - utter_greetbot
* my_name_is{"name": "sougata"}
    - slot{"name": "sougata"}
    - utter_greetings
    - utter_greet
* search_news
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "topic"}
* form: search_news
    - form: search_form
    - slot{"topic": "man city"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_news_search
    - utter_more_stories
* affirm
    - utter_greet
* news_headline
    - utter_newsheadline
* news_india
    - utter_more_stories
* deny
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greetbot
* my_name_is{"name": "priya"}
    - slot{"name": "priya"}
    - utter_greetings
    - utter_greet
* news_from_source
    - utter_newssource
* abc_news
    - action_news_abc
    - utter_more_stories
* affirm
    - utter_greet
* search_news
    - search_form
    - form{"name": "search_form"}
    - slot{"requested_slot": "topic"}
* form: search_news
    - form: search_form
    - slot{"topic": "virat kohli"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_news_search
    - utter_more_stories
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greetbot
* my_name_is{"name": "Neha"}
    - slot{"name": "Neha"}
    - utter_greetings
    - utter_greet
* news_headline
    - utter_newsheadline
* news_india
    - action_news_headline_india
    - utter_more_stories
* deny
    - utter_goodbye

## interactive_story_12
* greet
    - utter_greetbot
* my_name_is{"name": "animesh"}
    - slot{"name": "animesh"}
    - utter_greetings
    - utter_greet
* news_headline
    - utter_newsheadline
* news_india
    - action_news_headline_india
    - utter_more_stories
* affirm
    - utter_greet
* news_headline
    - utter_newsheadline
* news_country
    - utter_country
* my_country_is{"country": "UAE"}
    - slot{"country": "UAE"}
    - action_news_country
    - utter_more_stories
* deny
    - utter_goodbye

## interactive_story_11
* greet
    - utter_greetbot
* my_name_is{"name": "rajdeep"}
    - slot{"name": "rajdeep"}
    - utter_greetings
    - utter_greet
* news_headline
    - utter_newsheadline
* news_country
    - utter_country
* my_country_is{"country": "south africa"}
    - slot{"country": "south africa"}
    - action_news_country
    - utter_more_stories
* deny
    - utter_goodbye

## interactive_story_13
* greet
    - utter_greetbot
* my_name_is{"name": "pragya"}
    - slot{"name": "pragya"}
    - utter_greetings
    - utter_greet
* news_headline
    - utter_newsheadline
* news_country
    - utter_country
* my_country_is{"country": "singapore"}
    - slot{"country": "singapore"}
    - action_news_country
    - utter_more_stories
* affirm
    - utter_greet
* news_from_source
    - utter_newssource
* bbc_news
    - action_news_bbc
    - utter_more_stories
* deny
    - utter_goodbye

## New Story

* greet
    - utter_greetbot
* my_name_is{"name":"priya"}
    - slot{"name":"priya"}
    - utter_greetings
    - utter_greet
* news_headline
    - utter_newsheadline
* news_country
    - utter_country
* my_country_is{"country":"russia"}
    - slot{"country":"russia"}
    - action_news_country
    - utter_more_stories
* deny
    - utter_goodbye

## interactive_story_19
* greet
    - utter_greetbot
* my_name_is{"name": "aditya"}
    - slot{"name": "aditya"}
    - utter_greetings
    - utter_greet
* news_headline
    - utter_newsheadline
* news_country
    - utter_country
* my_country_is{"country": "canada"}
    - slot{"country": "canada"}
    - action_news_country
    - utter_more_stories
* deny
    - utter_goodbye
