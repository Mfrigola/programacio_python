#PR_pg83_05_dias.py

e = int(input("Euros: "))

r1 = e//100
r2 = e%100//50
r3 = e%100%50//20
r4 = e%100%50%20//10
r5 = e%100%500%20%10//5
r6 = e%100%500%20%10%5


print(r1,"bitllets de 100",r2,"bitllets de 50",r3,"bitllets de 20",r4,"bitllets de 10",r5,"bitllets de 5",r6,"monedes d'un euro")