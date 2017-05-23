# -*- coding: utf-8-*-

WORDS = [u"ECHO", u"CHUANHUA"]


def handle(text, mic, profile, wxbot=None):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        wxBot -- wechat robot
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    text = text.lower().replace('echo', '').replace(u'传话', '')
    mic.say(text)


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text.lower() for word in ["echo", u"传话"])