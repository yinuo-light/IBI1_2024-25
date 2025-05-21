# Define a function to calculate the required volume of paracetamol
def calculate(weight,strength):
# Check if user input the correct information  
   try:
        weight = float(weight)
# If user entered the wrong information, output error   
   except ValueError:
        return "Error: Weight must be a number."
# Check if the input weight is the possible weight of a child  
   if 10<weight<100 and strength in ['120mg/5ml', '250mg/5ml']: 

# Define a dictionary to map the strength strings to the actual values
     Calculate_strength={'120mg/5ml':24, '250mg/5ml':50 }
# Calculate the volumn
     drug_volume=weight*15/Calculate_strength[strength]
     return drug_volume
      
   else:
        return("Check if there are errors in the input.")

# an example of this function   
try:
    weight = 30 
    strength = '120mg/5ml' 
    drug_volume = calculate(weight, strength)
    print("If the weight is 30kg, the strength is 120mg/5ml,the volume of the drug is",drug_volume,"ml")
except Exception as e:
    print(f"An error occurred: {e}")

# Let the user input the information
weight=input("please enter children's weight(kg):")
strength=input("Please enter the strength of paracetamol in 120mg/5ml or 250mg/5ml: ")
#run our function to calculate the volume of paracetamol.
drug_volume=calculate(weight,strength)
print(drug_volume)

