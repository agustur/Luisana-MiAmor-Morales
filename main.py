from fastapi import FastAPI

app = FastAPI()

from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/", response_class=Response)
def amor_de_mi_vida():
    LM = "Luisana Morales te amoooooooooooooooo<3"
    return Response(LM, media_type="text/plain")
