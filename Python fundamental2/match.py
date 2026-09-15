color = str(input("enter the color:-"))

match color:
    case "green":
        print ("go")
    case "red":
        print("stop")
    case "yellow":
        print("be ready")
    case _: print("wrong color")
    # case_: is called as default case
    