def main(s: str):
    return [
        (el.split('"')[1],
         [int(x.split(",")[0]) for x in el.split("#")[1: -1]] +
         [int(el.split("#")[-1][:-1])])
        for el in s.split(".")[:-1]
    ]


print(main('''(( opt "ramave_20"<| array(#2761, #2043 ). opt"soen_545" <|array(#-1054 ,#3804 , #-3685 ). opt "xela" <|array( #-4118, #-3554, #4473, #7071 ).))'''))
