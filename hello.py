#Question 1
def hello_name(user_name):
    user_name == "Rachel"
    print("hello_USERNAME!")

hello_name("USERNAME")

#Question 2
def first_odds():
    return ()
print("first_odds")

first_odds("odds")

#Question 3
def max_num_in_list(a_list):
      a_list == ['1','2','3','4']
      return max('a_list')

max_num_in_list()
      
#Question 4      
def is_leap_year(a_year):
      a_year = 2016
      if a_year % 4 == 0 & a_year % 100 != 0 or a_year % 400 == 0:
        return True
   
print(is_leap_year("a_year"))

#Question 5
def is_consecutive(num_list):
    return sorted(num_list) == list(range(min(num_list), max(num_list)+1))
lst = [5, 8, 1, 4, 6] 
print(is_consecutive(lst))
     