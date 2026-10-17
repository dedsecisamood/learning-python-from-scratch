info = {
    "name" : "SiamAbdullah",
    "active_id" : True,
    "age" : 22, 
    "gpa" :4.00,
    "subs" : ["cse","eee","it","eng"],
    "marks" : ("91", "54", "78",)
}


print(((info.get("gpa"))))
print(type((info.items())))

dict = {"name":"Abdullah"}
info.update(dict)
print(info)
