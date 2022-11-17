from fastapi import FastAPI,Request
from routes import all_routes
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import time

origins = [
    "http://localhost:3000",
    "http://localhost:8000"
]

# app = FastAPI(
#     description='Desarrollo de apis para la aplicacion CCG',
#     version='0.0.1',
#     title='API CCG',
# )

tags_metadata = [
    dict(
        name="persona",
        description="Operation crud for the persons"
    )
]

app = FastAPI(
    title= "API CCG",
    description= "Desarrollo de apis para la aplicacion CCG",
    version='0.0.1',
    terms_of_service='http://example.com/terms/',
    contact= dict(
        name = "Israel Dillanes",
        email = "israeldillanes2@gmail.com"       
    ),
    license_info=dict(
        name="ORG 2.2",
        url = "https://www.apache.org/locense/LICENSE-2.0.html"
    ),
    openapi_tags=tags_metadata,
    openapi_url='/api/v1/openapi.json',
    docs_url="/docs",
    redoc_url="/redoct",

    )



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.middleware('http')
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     print('*****************klllllll',response)
#     return response

app.include_router(all_routes.login)
app.include_router(all_routes.registerUSer)
app.include_router(all_routes.persona)
app.include_router(all_routes.empleado)
app.include_router(all_routes.cp)
app.include_router(all_routes.departamento)
app.include_router(all_routes.pruebaImg)
app.include_router(all_routes.prueba)





app.mount('/static',StaticFiles(directory='static'),name='static')



