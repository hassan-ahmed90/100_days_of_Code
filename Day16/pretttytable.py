from prettytable import PrettyTable

table=PrettyTable()
my_name=['Hassan Ahmed',"Zohaib Ali Thaheem","Ahsan Ali","Saif Ali"]
profession=['Data Scientist','Web App Developer','UI/UX Designer','Freelancer']
table.add_column("Name",my_name)
table.add_column("Profession",profession)
table.align='l'
print(table)