import click
import os
import sys
from app import create_app
from app.extensions import db
from config import Config

app = create_app(Config)