from __future__ import absolute_import

import sys

long = int
basestring = str
raw_input = input
unichr = chr

class unicode(str):
    def __init__(self, string, encoding, errors):
        str.__init__(self, string)

def as_bytes(s, encoding='utf8'):
    if isinstance(s, bytes):
        return s
    else:
        return s.encode(encoding)

def as_string(s, encoding='utf8'):
    if isinstance(s, str):
        return s
    else:
        return s.decode(encoding)

def is_text_stream(stream):
    import _io
    return isinstance(stream, _io._TextIOBase)

import xmlrpc.client as xmlrpclib

import urllib.parse as urlparse
import urllib.parse as urllib

from hashlib import sha1

import syslog

import configparser as ConfigParser

from io import StringIO

from sys import maxsize as maxint

import http.client as httplib

from base64 import decodebytes as decodestring, encodebytes as encodestring

from xmlrpc.client import Fault

from string import ascii_letters as letters

from hashlib import md5

import _thread as thread

StringTypes = (str,)

from html import escape

import html.entities as htmlentitydefs

from html.parser import HTMLParser
