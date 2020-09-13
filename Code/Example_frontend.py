from sqlalchemy.orm import sessionmaker
from Project_orm import UserInput,Prediction
from sqlalchemy import create_engine
import streamlit as st

engine = create_engine('sqlite:///project_db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

st.title("Using Database ")

