import pytest
from pytdownload import valid_yt_url


def test_valid_yt_url_is_valid():
    assert valid_yt_url('https://www.youtube.com/watch?v=kXvmqg8hc70&list=PLtqF5YXg7GLmCvTswG32NqQypOuYkPRUE&index=11&t=324s')
    assert valid_yt_url('https://youtu.be/kXvmqg8hc70?si=h2b5daknWyqF-Wo5')
    assert valid_yt_url('m.youtube.com/watch?v=DFYRQ_zQ-gk')


def test_invalid_yt_url_is_invalid():
    assert not valid_yt_url('https://www.youtube.com/')
    assert not valid_yt_url('https://www.onet.pl/')
    assert not valid_yt_url('asdfgh')