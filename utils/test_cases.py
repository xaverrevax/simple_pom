# -*- coding: utf8 -*-


def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Blocker', 'when user goes to main page, page should be loaded'],
    ['Blocker', 'navigate to parametrized url'],
    ['Blocker', 'verify check translated text'],
    ['Blocker', 'switch lang selector'],
    ['Blocker', 'verify check translated text after switch'],
    ['Blocker', 'clear all the input fields'],
    ['Blocker', 'open virtual keyboard'],
    ['Blocker', 'type Hi!'],
]