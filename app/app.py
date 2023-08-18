from fastapi import FastAPI
import uvicorn
import strawberry
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

@app.get('/')
def root():
    return {"mssg": "Hello, World!!"}

@strawberry.type
class CPU:
    AMD: str
    INTEL: str

@strawberry.type
class AMD:
    CPU: str
    CORES: int

@strawberry.type
class INTEL:
    CPU: str
    CORES: int

@strawberry.type
class query:
    @strawberry.field
    def cpu(self) -> CPU:
        return CPU(AMD= "Ryzen 5", INTEL= "Core i7")
    
schema = strawberry.Schema(query)

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")

def run():
    uvicorn.run("app:app", port=6969)