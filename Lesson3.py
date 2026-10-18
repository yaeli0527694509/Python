# ex 1 -------- הפונקציה מקבלת נתיב לקובץ טקסט ומחזירה כמה מילים יש בו
def num_of_words(s):
    with open('Example.txt', 'r') as file:
        s = file.read()
        words = s.split()
    return len(words)

print(num_of_words(str)) # קריאה לפונקציה


# ex 2 -------- 'people.csv' הפונקציה מקבלת רשימה של רשימות ומכניסה את הנתונים לקובץ
def list_func(listOfLists):
    # כתיבה לקובץ
    with open('people.csv', 'w') as file:
        for li in listOfLists: # מעבר על הרשימה החיצונית (הרשימה של הרשימות)
            for li2 in li: # מעבר על כל הרשימות הפנימיות
                file.write(li2 + ' ') # קריאת הנתון ברשימה הפנימית ורווח לפני הנתון הבא
            file.write('\n') # מעבר שורה בין רשימה לרשימה
    # פתיחת הקובץ שוב רק כדי לקרוא את הנתונים
    with open('people.csv', 'r') as file:
        r = file.read()
        print(r)

list1 = ["Dov", "Levi", "20", "jerusalem"]
list2 = ["Avi", "Gold", "13", "Ashdod"]
list3 = ["David", "Rubin", "16", "Haifa"]

list_of_lists = [list1, list2, list3] # רשימה של רשימות
list_func(list_of_lists) # קריאה לפונקציה
