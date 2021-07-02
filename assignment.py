
altitude=int(input("enter the altitude"))
if altitude<=1000:
  print("safe to land the plane")
elif altitude>1000 and altitude<5000:
  print("come down to 1000ft")
else:
 print("turn around")