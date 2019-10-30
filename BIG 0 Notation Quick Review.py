
### ----- BIG O NOTATION Quick Review -----



### Some of the Most used BIG O:

#01 - Constant time         <=====>      O(1)
#02 - Logarithmic time      <=====>      O(log n)
#03 - Linear time           <=====>      O(n)
#04 - m log-star n time     <=====>      O(n log* n)
#05 - Quadratic time        <=====>      O(n²)
#06 - factorial time        <=====>      O(n!)


### How to find your BIG O: (Golden Rules)

#01 - Find the fastest growing term of your equation
#02 - take out the coefficient

# ----- e.g.: (Trick to find the BIG O of a code)
 
##### T = an + b = O(n) #####    
##### Breakdown of O(n) ######           
# "T" stands for "TIME"; 
# "n" is the "SIZE OF THE INPUT" or the "NUMBER OF ELEMENT IN THE ARRAY"; 
# "a" & "b" are two constants;
# "a" is the coefficient of "n";
# Since "a" is the coefficient of "n" and "b" is a constant without coefficient,...
# ... therefore "a" is the fastest growing term of the equation.
# So replace the "a" by "O()" and you have the time complexity of your code.
##### ... an ... <=====> O(n)

# T = cn² + dn + e = O(n²)



### Checkout WWW.BRILLIANT.ORG (Computer Science FUNDAMENTALS) for more in-depth explanation






