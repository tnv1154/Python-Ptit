
aliens = {
    "alien1" : {
        "color" : "green",
        "point" : 15
    },
    "alien2" : {
        "color" : "yellow",
        "point" : 10
    },
    "alien3" : {
        "color" : "red",
        "point" : 5
    }
}
for x, obj in aliens.items():
    print(x)
    for y in obj:
        print(y + " : " + str(obj[y]))