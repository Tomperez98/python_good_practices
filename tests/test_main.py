from src import main


def test_greeting():
    ans = main.greeting(name="your name")
    assert ans == "Hi your name"
