import mysql.connector


con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()
# add while loop
while True:

    word = input("Enter the word: ")

    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()

    # print(results) word = rain     # we will get a list of definitions in side tuples
    # [('Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.',),
    # ('To fall from the clouds in drops of water.',)]
    # tuple_list = [('apple', 'banana', 'orange'), ('people')]
    # print(tuple_list[1])      # people
    if results:
        for result in results:
            print(result[0])
    else:
        print("No word found!")