from behave import given, when, then
from selenium import webdriver

from features.steps.pages import *


@given('a user visit google')
def step_impl(context):
    page = SearchPage(context)
    page.load('http://www.google.com')


@when('the user searches for the "{search}" phrase')
def step_impl(context, search):
    page = SearchPage(context)
    page.search(search)

@when('the user searches for the')
def step_impl(context):
    page = SearchPage(context)
    page.search(context.text)

@when('user do the search of "{phrase}"')
def step_impl(context, phrase):
    context.execute_steps(u"""
            given a user visit google
             when the user searches for the "{search}" phrase
        """.format(search=phrase))


@then('one of the results contains: "{result}"')
def step_impl(context, result):
    page = ResultPage(context)
    results = page.phrase_result_count(result)
    assert results > 0


