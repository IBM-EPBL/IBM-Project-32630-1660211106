from io import BytesIO
from tkinter import Image
import wolframalpha
import requests
from IPython import display
from PIL import Image

def nutrients(food): 
    food=food+"nutritional info"
    app_id="RLWKY9-EUT258WJ5X"
    client=wolframalpha.Client(app_id)
    res=client.query(food)
    url=res.pod[1].subpod.img.src
    response=requests.get(url)
    img=Image.open(BytesIO(response.content))
    ans=next(res.results).text
    return url
    