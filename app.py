from models import Base,engine 


if __name__ == "__main__":
    #create all tables 

    Base.metadata.create_all(engine)
    print("Database tables created successfully!")