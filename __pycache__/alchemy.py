from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy .ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
from datetime import datetime

DATABASE_URL = "postgresql+psycopg2://test_user1:qwerty123!@52.78.214.236/test1"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class ExchangeRate(Base):
    __tablename__ = 'exchange_rates'
    currency_code = Column(String, primary_key=True)
    rate = Column(Float)
    timestape = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(engine)


def fetch_and_save_exchange_rates():
    url = "https://api.exchangeratesapi.io/latest?base=USD"
    response = requests.get(url)
    data = response.json()

    for currency, rate in data['rate'].items():
        exchange_rate = ExchangeRate(currency_code=currency, rate=rate)
        session.merge(exchange_rate)
    session.commit()


fetch_and_save_exchange_rates()

for rate in session.query(ExchangeRate).all():
    print(f"Currency: {rate.currency_code}, Rate: {rate.rate}")
