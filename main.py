from fastapi import FastAPI
from databases import models, database
from routes.index_routes import root_route
import uvicorn

# application factory structure run command
# uvicorn --factory main:create_app

def create_app():

    app = FastAPI()
    models.Base.metadata.create_all(bind=database.engine)
    app.include_router(root_route)
    print(f"create database engine : {database.engine}")
    return app


# app = create_app()

# if __name__ == "__main__":
    
#     uvicorn.run("app")