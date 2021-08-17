csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
csv1 = csv.replace(":", ",")
csv2 = csv1.replace(";",",")
csv3 = csv2.split(",")
print(csv3)

