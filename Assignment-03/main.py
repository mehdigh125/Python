from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from pathlib import Path
app = FastAPI()

chess= {
     "king": {
      
        "image" :'image/king.jpg',
        "fact": "شاه در شطرنج مهم‌ترین مهرهٔ بازی است. اگر مورد حملهٔ حریف قرار گیرد در وضعیت کیش قرار می‌گیرد و اگر نتوان کیش را برطرف نمود، مات یا کیش‌ومات اتفاق افتاده و بازی با پیروزی حریف به پایان رسیده‌است"
    },

     "queen": {
      
        "image" :'image/queen.jpg',
        "fact": "وزیر در شطرنج قوی‌ترین مهرهٔ بازی است که ترکیبی از حرکت رخ و فیل را با هم انجام می‌دهد"
    },
     "rook": {
      
        "image" :'image/rook.jpg',
        "fact": "رُخ یکی از مهره‌های شطرنج است که می‌تواند به‌طور نامحدود در طول و عرض صفحهٔ شطرنج حرکت کند."
    },
     "bishop": {
      
        "image" :'image/bishop.jpg',
        "fact": "فیل یکی از مهره‌های شطرنج است که می‌تواند به‌طور نامحدود به‌طور مورب حرکت کند. هر یک از بازیکنان دو فیل دارد که یکی بین شاه و اسب و دیگری بین وزیر و اسب قرار می‌گیرد."
    },
     "Knight": {
      
        "image" :'image/Knight.jpg',
        "fact": "اسب متفاوت‌ترین روش حرکت را در میان مهره‌های شطرنج دارد و حرکت آن با دو خانه حرکت عمودی و یک خانه حرکت افقی یا دو خانه حرکت افقی و یک خانه حرکت عمودی انجام می‌شود که به حرف ال در الفبای لاتین شباهت دارد."
    },
    "pawn": {
      
        "image" :'image/pawn.jpg',
        "fact": "سرباز یا پیاده پرتعدادترین مهره در بازی شطرنج است. این مهره با نماد پیاده‌نظام در شطرنج شناخته می‌شود. هر بازیکن در ابتدای بازی دارای هشت پیاده است. پیاده‌های سفید در آغاز بازی در ردیف (صف) دوم و پیاده‌های سیاه در ردیف هفتم قرار دارند."
    }

}
@app.get("/")
def read_root():
    return "Hi, welcome to my api In this api there is about chess"

@app.get("/chess")
def get_chess():
    return chess

@app.get("/chess/{name_piece}/")
def read_piece_info(name_piece: str):
    if name_piece=='king' or name_piece=='bishop' or name_piece=='knight' or name_piece=='pawn' or name_piece=='queen' or name_piece=='rook' :
        return chess[name_piece]
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="name_piece must king or bishop or knight or pawn or queen or rook")
@app.get("/chess/image")
def read_default_image():
     image_path = Path("image/6pieces.jpg")
     return FileResponse(image_path)

@app.get("/chess/image/{name_piece}")
def read_piece_image(name_piece: str):
    if name_piece=='king' or name_piece=='bishop' or name_piece=='knight' or name_piece=='pawn' or name_piece=='queen' or name_piece=='rook' :
        images= chess[name_piece]
        image_path = images["image"]
        return FileResponse(image_path)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="name_piece must  king or bishop or knight or pawn or queen or rook")



