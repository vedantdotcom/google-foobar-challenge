def solution(s):
  char={"a":"z",
        "b":"y",
        "c":"x",
        "d":"w",
        "e":"v",
        "f":"u",
        "g":"t",
         "h":"s",
        "i":"r",
        "j":"q",
        "k":"p",
        "l":"o",
        "m":"n",
        "n":"m",
        "o":"l",
        "p":"k",
        "q":"j",
        "r":"i",
        "s":"h",
        "t":"g",
        "u":"f",
        "v":"e",
        "w":"d",
        "x":"c",
        "y":"b",
        "z":"a"}

  s=list(s)

  for index,item in enumerate(s):
      for key,value in char.items():
          if item==key:
              s[index]=value

  print("".join(s))