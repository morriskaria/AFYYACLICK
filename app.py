# app.py
from models import Base, engine

if __name__ == "__main__":
    cli = Afyyaclick()
    cli.run()
    # Create all tables
    Base.metadata.create_all(engine)
   