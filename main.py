# main.py
from fastapi import FastAPI
import uvicorn
import argparse
import psycopg2

def create_app():
    app = FastAPI()

    @app.get("/healthcheck")
    def healthcheck():
        return {"status": "ok"}
    @app.get("/create_db")
    def create_database(db_name, user, password, host='localhost', port='5432'):
        try:
            conn = psycopg2.connect(
                dbname='postgres',
                user=user,
                password=password,
                host=host,
                port=port
            )

            conn.autocommit = True
        
            cur = conn.cursor()
            
            cur.execute(f"CREATE DATABASE {db_name};")
            
            conn.commit()
            cur.close()
            conn.close()
            return {"status": "Yayyy, Database has been created successfully"}

        except:
            return {"status": "Something went wrong, database not created"}

            

    return app

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="FastAPI Machine Learning API")
    parser.add_argument("--port", type=int, default=8000, help="Port number to bind the FastAPI application")
    args = parser.parse_args()

    uvicorn.run("main:create_app", host="127.0.0.1", port=args.port, reload=True)
