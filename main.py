from fastapi import FastAPI, File, UploadFile
import base64
from pydantic import BaseModel
from aws_uploader import upload_file

app = FastAPI()

class Item(BaseModel):
    PName: str
    PId: str
    Site: str
    Type: int
    file: bytes

@app.get('/')
def general():
    return 'Hi'

@app.post('/upload')
def upload(item: Item):
    try:
        file_content=base64.b64decode(item.file)
        with open(f"data/{item.PId}_{item.Site}_{item.Type}.wav","wb") as f:
            f.write(file_content)
        with open(f"data/{item.PId}_{item.Site}_{item.Type}.txt","w") as f:
            f.write(f"{item.PName}\n{item.PId}\n{item.Site}\n{item.Type}")
        upload_file('{item.PId}_{item.Site}_{item.Type}.wav')
        upload_file('{item.PId}_{item.Site}_{item.Type}.txt')
    except Exception as e:
        print(str(e))
        return str(e)

    print('Success')
    return 'Success'
