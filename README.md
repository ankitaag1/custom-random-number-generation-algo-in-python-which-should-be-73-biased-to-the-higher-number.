# custom-random-number-generation-algo-in-python-which-should-be-73-biased-to-the-higher-number without using random no. generator function
Input from the user the starting value, ending value of the range and the number of random values to be generating and store these in the variables s,e and h respectively .
convert s, e and h into integers and store in s1,e1 and h1 respectively.
calculate mid point of the range and store in half
calculate the 73% and 27% of no of values and store in high1 and low1 respectively.
extract the fraction parts of high1 and low1 and calculate high and low according to the logic that high+low=h1(total number of random no.s to be generated)
high and low are the no of high values and low values to be generated i.e 73% are high values(more than or equal to half) and 27% are low values(less than half)
calculate the no. of digits in the ending value(e1)
initialize mor and les to 0 to keep account of their limit
extract the microsecond part of the system time and store in x1 while the condition is true
extract the no. of digits in x1 equal to the no. of digits in e(ending value)and convert it to integer and store in x3
check if x3 falls in the range of s1 and e1
then check if x3 is greater than half then increament mor and if mor has not reached the limit of high values(73% of no. of values), print x3 else continue with the next iteration.
if x3 is less than half then increament les and if les has not reached the limit of low values(27% of no. of values), print x3 else continue with the next iteration.
the loop continues till both mor and les reach their maximum value.
