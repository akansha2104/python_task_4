#books
def book(title,authors,publications,type_of_book):
    print(f'b_title={title}')
    print(f'b_authors={authors}')
    print(f'b_publications={publications}')
    print(f'b_type_of_book={type_of_book}')
    return'_E_BOOK'
print('---')
print(f'book_1{book("to kill a mockingbird","harper lee",1960,'fiction')}')
print('---')
print(f'book_2{book(1984,"george orwell",1949,"dystopian")}')
print('---')


#calculate sum of data
def calculate_sum(data):
    return sum(data)
data = [15,40,25,120]
total = calculate_sum(data)
print(f"the total sum of data is: {total}")


#substraction and multiplication
def sub_numbers (a,b):
    return a-b
result = sub_numbers(5,3)
print(result)
def mul_numbers (a,b):
   return a * b 
result = mul_numbers (10,2)
print(result)
print()

#addition and division
def add_numbers (a,b):
    return a+b
result = add_numbers(6,8)
print(result)
def div_numbers (a,b):
   return a % b 
result = div_numbers (12,6)
print(result)



