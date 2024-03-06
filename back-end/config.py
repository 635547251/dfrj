import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')


class Config(object):
    ZHIPU_API_KEY='74ea84ef8fd735c5adcee4e7a2b467b1.7IR9LOQ9454J9tdm'
    MODEL_ZHIPU='glm-4'

    DIFY_API_KEY='app-U0OpyrRR9RalRJrLTXUjBG48'
    DIFY_URL='https://api.dify.ai/v1'