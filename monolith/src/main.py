"""main module for account-service"""
from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager

from .database import Base, engine
from .router import main_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server start working")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("db is ready to use")
    yield
    print("server stop working")


app = FastAPI(lifespan=lifespan)
app.include_router(main_router)


@app.get("/")
async def get_homepage():
    return {
        "data": [
            {
                "_id": "66c4f1e9b377878e2594b732",
                "index": 2,
                "guid": "892241a2-572d-4970-bca4-4a27c802ebb2",
                "isActive": True,
                "balance": "$2,226.32",
                "picture": "http://placehold.it/32x32",
                "age": 24,
                "eyeColor": "green",
                "name": "Vasquez Hendricks",
                "gender": "male",
                "company": "STEELFAB",
                "email": "vasquezhendricks@steelfab.com",
                "phone": "+1 (939) 497-3656",
                "address": "454 Georgia Avenue, Fidelis, West Virginia, 3653",
                "about": "Consequat duis sint elit culpa anim esse ea occaecat amet minim occaecat do cillum tempor. Tempor deserunt mollit exercitation veniam deserunt id qui eu non sit elit non. Minim officia adipisicing ipsum non fugiat pariatur. Adipisicing labore culpa culpa aliqua laboris laborum cupidatat officia amet commodo aliqua dolor aliquip dolor. Ut aliqua reprehenderit Lorem ullamco. Ex ut officia culpa labore dolore sunt velit labore.\r\n",
                "registered": "2017-11-10T04:22:14 -03:00",
                "latitude": -72.369314,
                "longitude": -11.794034,
                "tags": [
                "velit",
                "laboris",
                "nisi",
                "sunt",
                "in",
                "ad",
                "qui"
                ],
                "friends": [
                {
                    "id": 0,
                    "name": "Charles Franco"
                },
                {
                    "id": 1,
                    "name": "Mavis Williams"
                },
                {
                    "id": 2,
                    "name": "Lora Malone"
                }
                ],
                "greeting": "Hello, Vasquez Hendricks! You have 1 unread messages.",
                "favoriteFruit": "banana"
            },
            
            {
                "_id": "66c4f1e9b07dda3ee484156b",
                "index": 4,
                "guid": "1949fd54-d568-453a-9ff0-71087b523f0a",
                "isActive": True,
                "balance": "$3,921.61",
                "picture": "http://placehold.it/32x32",
                "age": 23,
                "eyeColor": "brown",
                "name": "Golden Giles",
                "gender": "male",
                "company": "PARCOE",
                "email": "goldengiles@parcoe.com",
                "phone": "+1 (967) 411-2886",
                "address": "655 Canton Court, Sheatown, Rhode Island, 9346",
                "about": "Commodo ea laborum ut deserunt labore fugiat est qui velit veniam. Magna nulla qui eu amet cupidatat cillum. Aliqua voluptate consectetur est mollit et et ipsum do deserunt excepteur nostrud do do aliqua.\r\n",
                "registered": "2018-02-02T11:56:13 -03:00",
                "latitude": 77.920171,
                "longitude": -45.25548,
                "tags": [
                "proident",
                "excepteur",
                "nostrud",
                "cillum",
                "voluptate",
                "deserunt",
                "minim"
                ],
                "friends": [
                {
                    "id": 0,
                    "name": "Annabelle Hicks"
                },
                {
                    "id": 1,
                    "name": "Decker Mcgowan"
                },
                {
                    "id": 2,
                    "name": "Mclaughlin Fleming"
                }
                ],
                "greeting": "Hello, Golden Giles! You have 9 unread messages.",
                "favoriteFruit": "apple"
            }
        ]
    }