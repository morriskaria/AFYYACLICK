# app.py
from models import Base, engine

if __name__ == "__main__":
    cli = Afyyaclick()
    cli.run()
    
    Base.metadata.create_all(engine)
   