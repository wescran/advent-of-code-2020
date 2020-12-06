#!/usr/bin/env python3
from pathlib import Path
from contextlib import contextmanager
import requests
import os
import argparse

class NoDayError(Exception):
    def __init__(self,message):
        self.message = message

class NoSessionError(Exception):
    def __init__(self,message):
        self.message = message

class RequestError(Exception):
    def __init__(self,message):
        self.message = message

class Advent:
    def __init__(self, day=None, session=None):
        if not day:
            raise NoDayError("Need a day for input")
        if not session:
            session = os.getenv("AOCSESSION")
            if not session:
                raise NoSessionError("Need a session cookie for input access")
        self.day = day
        self.session = session
        self.url = f"https://adventofcode.com/2020/day/{self.day}/input"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        self.cookies = {"session": self.session}

    @contextmanager
    def get(self):
        try:
            response = requests.get(url=self.url, headers=self.headers, cookies=self.cookies)
            if not response.raise_for_status():
                yield response.text
        except requests.exceptions.RequestException as e:
            raise RequestError(f"requests error: {e}") from e

    def download(self,path=None):
        if not path:
            path = Path.cwd() / f"day{self.day}.txt"
        with self.get() as data:
            Path(path).resolve().write_text(data)
        print(f"day {self.day} input written to '{path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="advent of code day for input", type=int)
    parser.add_argument("--session", help="session cookie for accessing input", type=str)
    parser.add_argument("--path", help="path to download input to", type=str)
    args = parser.parse_args()

    Advent(day=args.day,session=args.session).download(args.path)
