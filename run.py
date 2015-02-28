#! /usr/bin/env python
from app import app
from flask import Flask
import os
import time
import datetime
from flask import render_template

app.run(debug=True,host="0.0.0.0",port=8080)
