##This page will host a heap of responses for each type of intent
##Room for more intent as time goes on after this project submission

import random

mental_health_response_dict = {
    "bipolar": 'Bipolar disorder is a mental health problem that mainly affects your mood. If you have bipolar disorder, you are likely to have times where you experience: <ul><li>manic or hypomanic episodes (feeling high)</li><li>depressive episodes (feeling low)</li></ul>',
    "anxiety": 'Anxiety is what we feel when we are worried, tense or afraid – particularly about things that are about to happen, or which we think could happen in the future.',
    "depression": 'Depression is a low mood that lasts for a long time, and affects your everyday life.',
    "schizophrenia": 'You could be diagnosed with schizophrenia if you experience some of the following symptoms: <ul><li> lack of interest in things</li><li>feeling disconnected from your feelings</li></ul>',
    "PTSD": 'Post-traumatic stress disorder is a type of anxiety disorder which you may develop after being involved in or witnessing traumatic events.',
    "Psychosis": 'Psychosis (also called a psychotic experience or psychotic episode) is when you perceive or interpret reality in a very different way from people around you',
    "stress": 'Situations or events that put pressure on us – for example, times where we have lots to do and think about, or dont have much control over what happens' ,
    "faq_directory": 'You can check out the list of useful mental health resources here <a href="#">Mental Health Resources</a>'
}

assessment_info_response_dict = {
    "Privacy": 'privacy is important to us. All results are completely anonymous',
    "faq_link": 'You can check out the list of useful mental health resources here <a href="#">Mental Health Resources</a>'
}

greetings = ["Hello there", "hey", "*nods*", "Hiya, how can I help?", "Fancy learning about your mental health","<h1>hello</h1>"]
goodbyes = ["Bye", "Adios amigos", "Take care", "See ya", "goodbye", "<h1>BYE:(</h1>"]
affirmations = ["Indeed", "Ok", "Perfect", "That's alright", "Nice"]

def greeting():
    """If any of the words in the user's input was a greeting, return a greeting response"""
    return random.choice(greetings)


def goodbye():
    """If any of the words in the user's input was a goodbye, return a goodbye response"""
    return random.choice(goodbyes)


def affirm():
    """If any of the words in the user's input requires an affirmation, return one"""
    return random.choice(affirmations)

def start_assessment(entities):
    if not entities:
        return "Could not find out specific information about this ..." + mental_health_response_dict["faq_link"]
    if len(entities) >= 1:
        return mental_health_response_dict[entities[0]['value']]
    return "Sorry.." + mental_health_response_dict["faq_link"]

def depression_assessment(entities):
    if not entities:
        return "Could not find out specific information about this ..." + depression_response_dict["faq_link"]
    if len(entities) >= 1:
        return depression_response_dict[entities[0]['value']]
    return "Sorry.." + depression_response_dict["faq_link"]

def psychosis_assessment(entities):
    if not entities:
        return "Could not find out specific information about this ..." + pyschosis_response_dict["faq_link"]
    if len(entities) >= 1:
        return psychosis_response_dict[entities[0]['value']]
    return "Sorry.." + pyschosis_response_dict["faq_link"]