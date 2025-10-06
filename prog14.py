# print the pattern with * as centered pyramid



rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)



# Enter number of rows: 5
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

