import cv2, os
import numpy as np
import FoodAPI
import GlobalVar as var
from dbconnect import conncet
from numpy import ndarray

color = (0, 0, 255)

def getFoodByBarcode(barcode):
    db = conncet()
    cursor = db.cursor()
    sql = "SELECT food_name,weight,calories,fat,carbs,protein FROM Barcode WHERE barcode=%s;"
    cursor.execute(sql,(barcode))
    row = cursor.fetchone()
    food = FoodAPI.Food()
    if row:
        print(row)
        food.name = row[0]
        food.per = row[1]
        food.calories = row[2]
        food.fat = row[3]
        food.carbs = row[4]
        food.protein = row[5]
        return food
    else:
        return None

def getFoodByName(name):
    db = conncet()
    cursor = db.cursor()
    sql = "SELECT food_name,weight,calories,fat,carbs,protein FROM Barcode WHERE food_name=%s;"
    cursor.execute(sql,(name))
    row = cursor.fetchone()
    food = FoodAPI.Food()
    if row:
        print(row)
        food.name = row[0]
        food.per = row[1]
        food.calories = row[2]
        food.fat = row[3]
        food.carbs = row[4]
        food.protein = row[5]
        return food
    else:
        return None

def createBarcode(barcode,food_name,weight):
    result = True
    db = conncet()
    cursor = db.cursor()
    sql = "INSERT INTO Barcode VALUES (%s,%s,%s);"
    try:
        cursor.execute(sql,(barcode,food_name,weight))
        db.commit()
    except:
        db.rollback()
        print('create fail,please check the data')
        result = False
    db.close()
    return result

def deleteBarcode(barcode):
    result = True
    db = conncet()
    cursor = db.cursor()
    sql = "DELETE FROM Barcode WHERE barcode=%s;"
    try:
        cursor.execute(sql,(barcode))
        db.commit()
    except:
        db.rollback()
        result = False
        print('delete fail, please check the data')
    db.close()
    return result

def updateBarcode(barcode,food_name,weight):
    result = True
    db = conncet()
    cursor = db.cursor()
    sql = "UPDATE Barcode SET food_name=%s,weight=%s WHERE barcode=%s;"
    try:
        cursor.execute(sql,(food_name,weight,barcode))
        db.commit()
    except:
        db.rollback()
        result = False
        print('update fail,please check the data')
    db.close()
    return result

bardet = cv2.barcode_BarcodeDetector()
def detectBarcode(frame: ndarray):
    #  Detect and decode the barcode
    var.food = None
    ok, decoded_info, decoded_type, corners = bardet.detectAndDecode(frame)
    # draw box and text around the barcode
    if type(corners) != type(None):
        frame = cv2.polylines(frame, np.int32(corners), 1, color, 3)
        for i, barcode_num in enumerate(decoded_info):
            food = getFoodByBarcode(barcode_num)
            if food:
                x_pos, y_pos = int(corners[i][1][0]), int(corners[i][1][1]-10)
                frame = cv2.putText(frame, food.name, (x_pos, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
                var.food = food
                return frame
        print(decoded_info)
    return frame

def listFoodName(barcode):
    db = conncet()
    cursor = db.cursor()
    sql = "SELECT food_name FROM Barcode WHERE barcode LIKE '" + barcode + "%';"
    cursor.execute(sql)
    row = cursor.fetchone()
    if not row:
        return None
    return row

if __name__ == '__main__':
    img_file = ((os.path.dirname(os.path.abspath(__file__)))+'/test_img.jpg')
    img = cv2.imread(img_file)
    frame, food_name = detectBarcode(img)
    print(food_name)
    print(getFoodByBarcode('test'))