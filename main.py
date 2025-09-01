import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

# Database connection string - replace with your actual database details
DSN = 'postgresql://username:password@localhost:5432/database_name'

def main():
    # Create database engine
    engine = sqlalchemy.create_engine(DSN)
    
    # Create tables
    create_tables(engine)
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Load data from JSON file
        with open('fixtures/tests_data.json', 'r', encoding='utf-8') as fd:
            data = json.load(fd)
        
        # Process each record
        for record in data:
            model = {
                'publisher': Publisher,
                'shop': Shop,
                'book': Book,
                'stock': Stock,
                'sale': Sale,
            }[record.get('model')]
            
            # Create model instance and add to session
            session.add(model(id=record.get('pk'), **record.get('fields')))
        
        # Commit all changes
        session.commit()
        print("Данные успешно загружены в базу данных")
        
    except FileNotFoundError:
        print("Файл fixtures/tests_data.json не найден")
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    main() 