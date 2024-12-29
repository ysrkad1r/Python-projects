COST_OF_1IU_PLASMA = 0.3
COST_OF_1IU_RECOMBINANT = 0.4

total_patient_number = 0
hemophilia_A_patint_number = 0
hemophilia_B_patint_number = 0
severe_patient_number = 0
moderate_patient_number = 0
mild_patient_number = 0
greater_than_5_antibody_A_number = 0
greater_than_5_antibody_B_number = 0
prophylaxis_true_A_patients = 0
prophylaxis_true_B_patients = 0
need_prophylaxis_moderate_patients = 0
need_prophylaxis_A_plasma = 0
need_prophylaxis_B_plasma = 0
need_prophylaxis_A_recombinant = 0
need_prophylaxis_B_recombinant = 0
cost_of_medication_for_four_week = 0
need_prophylaxis_patients = 0
total_medication_amount_for_one_year = 0

total_factor8_plazma=0
total_factor8_recombinant=0
total_factor9_plazma=0
total_factor9_recombinant=0
total_factor8_plazma_2000=0
total_factor8_plazma_1500=0
total_factor8_plazma_1000=0
total_factor8_plazma_500=0
total_factor8_plazma_250=0
total_factor8_recombinant_2000=0
total_factor8_recombinant_1500=0
total_factor8_recombinant_1000=0
total_factor8_recombinant_500=0
total_factor8_recombinant_250=0
total_factor9_plazma_2000=0
total_factor9_plazma_1500=0
total_factor9_plazma_1000=0
total_factor9_plazma_500=0
total_factor9_plazma_250=0
total_factor9_recombinant_2000=0
total_factor9_recombinant_1500=0
total_factor9_recombinant_1000=0
total_factor9_recombinant_500=0
total_factor9_recombinant_250=0

#MAX MEDICATION AMOUNT INFOS
max_id_number_A = 0
max_name_surname_A = " "
max_severetiy_A = " "
max_weight_A = 0
max_produce_medication_A = " "
max_medication_amountIU_A = -1
max_medication_cost_A = 0

#MAX MEDICATION AMOUNT INFOS
max_id_number_B = 0
max_name_surname_B = " "
max_severetiy_B = " "
max_weight_B = 0
max_produce_medication_B = " "
max_medication_amountIU_B = -1
max_medication_cost_B = 0

#MAX COST OF 4 WEEK INFOS
max_cost_id_number = 0
max_cost_name_surname = " "
max_cost_severetiy = " "
max_cost_weight = 0
max_cost_produce_medication = " "
max_cost_medication_amountIU = 0
max_cost_medication_cost = 0

response = "y"
while response == "y" or response == "Y":
    total_patient_number += 1
    id_number=input("Enter your identification number :")
    name_surname=input("Enter your name and surname :")
    deficient_factor=int(input("Enter your deficient factor protein's number :"))

    while deficient_factor!=9 and deficient_factor!=8 :
        print("Your deficient factor protein's number must be 8 or 9 !!!")
        deficient_factor=int(input("Enter your deficient factor protein's number :"))

    factor_in_blood=float(input(f"Enter the factor {deficient_factor} level in your blood :"))
    amount_of_antibody=float(input("Enter the amount of antibody in your blood (BU) :"))
    
    type_of_disease = ""
    need_prophylaxis = False #as default this is false until infos calculated
    

    while factor_in_blood >=50 or factor_in_blood < 0:
        print(f"The factor {deficient_factor} level in your blood must be 0 or greater than 0 and less than 50 !!!")
        factor_in_blood=float(input(f"Enter the factor {deficient_factor} level in your blood :"))

    if factor_in_blood > 0 and factor_in_blood < 1 :
        severity_of_disease= "Severe"
        severe_patient_number += 1
    elif factor_in_blood <= 5 and factor_in_blood >= 1:
        severity_of_disease = "Moderate"
        moderate_patient_number += 1
    elif factor_in_blood > 5 and factor_in_blood < 50 :
        severity_of_disease = "Mild"
        mild_patient_number += 1

    if severity_of_disease == "Moderate" :
        number_of_bleeding=int(input("Enter the number of bleeding episodes in the past year :"))
        while number_of_bleeding <0:
            print("The number of bleeding episodes in the past year must be 0 or greater than 0 !!!")
            number_of_bleeding=int(input("Enter the number of bleeding episodes in the past year :"))

    while amount_of_antibody<0 :
        print("the amount of antibody in your blood must be 0 or greater than 0 !!")
        amount_of_antibody=float(input("Enter the amount of antibody in your blood :"))

    if (severity_of_disease=="Severe" and amount_of_antibody < 5) or (severity_of_disease=="Moderate" and number_of_bleeding >=3 and amount_of_antibody < 5) :
        need_prophylaxis = True
        weight=float(input("Enter your weight :"))
        while weight < 0:
            print("Your weight must be 0 or greater than 0 !!!")
            weight=float(input("Enter your weight :"))
        production_type_of_medication=input("Enter what type of medication you will use (P/p/R/r) :")
        while production_type_of_medication !="R" and production_type_of_medication!="r" and production_type_of_medication!= "P" and production_type_of_medication!="p" :
            print(" the production type of factor medication to be used must be plazma or recombinant (P/p/R/r) !!!")
            production_type_of_medication = input("Enter what type of medication you will use (P/p/R/r) :")
        

    if deficient_factor == 8:
        type_of_disease = "A"
        hemophilia_A_patint_number += 1
        if need_prophylaxis == True:
            prophylaxis_true_A_patients += 1
            if production_type_of_medication == "P" or production_type_of_medication == "p":
                need_prophylaxis_A_plasma += 1
            elif production_type_of_medication == "R" or production_type_of_medication == "r":
                need_prophylaxis_A_recombinant += 1
    elif deficient_factor == 9:
        type_of_disease = "B"
        hemophilia_B_patint_number += 1
        if need_prophylaxis == True:
            prophylaxis_true_B_patients += 1
            if production_type_of_medication == "P" or production_type_of_medication == "p":
                need_prophylaxis_B_plasma += 1
            elif production_type_of_medication == "R" or production_type_of_medication == "r":
                need_prophylaxis_B_recombinant += 1

    if amount_of_antibody > 5:
        need_prophylaxis = False
        if type_of_disease == "A":
            greater_than_5_antibody_A_number += 1
        elif type_of_disease == "B":
            greater_than_5_antibody_B_number += 1

    need_min_medication = 0
    bottle_2000 = 0
    bottle_1500 = 0
    bottle_1000 = 0
    bottle_500 = 0
    bottle_250 = 0
    cost_of_medication = 0
    amount_of_medicate_of_4_week = 0

    print(f"TR identification number : {id_number}")
    print(f"name and surname is {name_surname}")
    print(f"Type of disease {type_of_disease} and {severity_of_disease}")
    #Just printing.
    if need_prophylaxis:
        print("Prophylaxis will be applied")
    else:
        print("Prophylaxis will not be applied")

    if need_prophylaxis:
        need_prophylaxis_patients += 1
        print(f"deficient factor is {deficient_factor}")
        if production_type_of_medication == 'p' or production_type_of_medication == "P":
            print(f"production type of medication is plasma")
        else:
            print(f"production type of medication is recombinant")
            
        if type_of_disease == "A":
            print(f"Weekly usage of medicine : {3}")
        elif type_of_disease == "B":
            print(f"Weekly usage of medicine : {2}")
        if type_of_disease == "A":
            need_min_medication = ((40 - factor_in_blood)/2)*weight
            total_medication_amount_for_one_year += need_min_medication*156 #one year 52 week and type A patients using 3 per week
        elif type_of_disease == "B":
            need_min_medication = (40 - factor_in_blood)*weight
            total_medication_amount_for_one_year += need_min_medication*104  #one year 52 week and type A patients using 2 per week
        print(f"Mininum need of medicine is {round(need_min_medication,2)} IU")
        # Thıs part calculates the max vial number
        if need_min_medication % 250 != 0:
            max_piece_amount = (need_min_medication // 250) + 1
        else:
            max_piece_amount = (need_min_medication // 250)
        # Thıs part calculates the number of vials via using max number of vials
        while max_piece_amount > 0:
            if max_piece_amount >= 8:
                bottle_2000 += max_piece_amount // 8
                max_piece_amount -= 8*(max_piece_amount // 8)
            elif max_piece_amount >= 6:
                bottle_1500 += max_piece_amount // 6
                max_piece_amount -= 6*(max_piece_amount // 6)
            elif max_piece_amount >= 4:
                bottle_1000 += max_piece_amount // 4
                max_piece_amount -= 4*(max_piece_amount // 4)
            elif max_piece_amount >= 2:
                bottle_500 += max_piece_amount // 2
                max_piece_amount -= 2*(max_piece_amount // 2)
            elif  max_piece_amount > 0 and max_piece_amount <= 1 :
                bottle_250 += 1
                max_piece_amount -= 1

        print(f'Amount of medication to be used at one time is {round(need_min_medication,2)} IU')
        #list is definitely need to here and this writes the number of vials just if vial number not equals 0
        if bottle_2000 != 0:
            print(f"{int(bottle_2000)} 2000's bottle")
        if bottle_1500 != 0:
            print(f"{int(bottle_1500)} 1500's bottle")
        if bottle_1000 != 0:
            print(f"{int(bottle_1000)} 1000's bottle")
        if bottle_500 != 0:
            print(f"{int(bottle_500)} 500's bottle")
        if bottle_250 != 0:
            print(f"{int(bottle_250)} 250's bottle")

        if production_type_of_medication == "P" or production_type_of_medication == "p":
            cost_of_medication = COST_OF_1IU_PLASMA * need_min_medication
            if type_of_disease == "A":
                cost_of_medication_for_four_week += cost_of_medication*12
            elif type_of_disease == "B":
                cost_of_medication_for_four_week += cost_of_medication*8
        elif production_type_of_medication == "R" or production_type_of_medication == "r":
            cost_of_medication = COST_OF_1IU_RECOMBINANT * need_min_medication
            if type_of_disease == "A":
                cost_of_medication_for_four_week += cost_of_medication*12
            elif type_of_disease == "B":
                cost_of_medication_for_four_week += cost_of_medication*8

        if type_of_disease == "A":
            amount_of_medicate_of_4_week = 12 * need_min_medication
            cost_of_medication_of_4_week = 12 * cost_of_medication
            print(f"amount of medicate for 4 week is {round(amount_of_medicate_of_4_week,2)} IU")
            #list is definitely need to here
            if bottle_2000 != 0:
                print(f"{12*int(bottle_2000)} 2000's bottle for 4 week")
            if bottle_1500 != 0:
                print(f"{12*int(bottle_1500)} 1500's bottle for 4 week")
            if bottle_1000 != 0:
                print(f"{12*int(bottle_1000)} 1000's bottle for 4 week")
            if bottle_500 != 0:
                print(f"{12*int(bottle_500)} 500's bottle for 4 week")
            if bottle_250 != 0:
                print(f"{12*int(bottle_250)} 250's bottle for 4 week")
            if amount_of_medicate_of_4_week > max_medication_amountIU_A:
                max_medication_amountIU_A = need_min_medication
                max_id_number_A = id_number
                max_name_surname_A = name_surname
                max_severetiy_A = severity_of_disease
                max_weight_A = weight
                max_produce_medication_A = production_type_of_medication
                max_medication_cost_A = cost_of_medication_of_4_week
                max_medication_amountIU_A = amount_of_medicate_of_4_week

            print(f"Cost of medication for 4 weeks is {round(cost_of_medication_of_4_week,2)} $")
        elif type_of_disease == "B":
            amount_of_medicate_of_4_week = 8 * need_min_medication
            cost_of_medication_of_4_week = 8 * cost_of_medication
            print(f"amount of medicate for 4 week is {round(amount_of_medicate_of_4_week,2)} IU")
            #list is definitely need to here
            if bottle_2000 != 0:
                print(f"{8*int(bottle_2000)} 2000's bottle for 4 week")
            if bottle_1500 != 0:
                print(f"{8*int(bottle_1500)} 1500's bottle for 4 week")
            if bottle_1000 != 0:
                print(f"{8*int(bottle_1000)} 1000's bottle for 4 week")
            if bottle_500 != 0:
                print(f"{8*int(bottle_500)} 500's bottle for 4 week")
            if bottle_250 != 0:
                print(f"{8*int(bottle_250)} 250's bottle for 4 week")
            if amount_of_medicate_of_4_week > max_medication_amountIU_B:
                max_medication_amountIU_B = need_min_medication
                max_id_number_B = id_number
                max_name_surname_B = name_surname
                max_severetiy_B = severity_of_disease
                max_weight_B = weight
                max_produce_medication_B = production_type_of_medication
                max_medication_cost_B = cost_of_medication_of_4_week
                max_medication_amountIU_B = amount_of_medicate_of_4_week

            print(f"Cost of medication for 4 weeks is {round(cost_of_medication_of_4_week,2)} $")
        
        if need_prophylaxis == True and severity_of_disease == "Moderate":
            need_prophylaxis_moderate_patients += 1
        
        if cost_of_medication_of_4_week > max_cost_medication_cost:
                max_cost_id_number = id_number
                max_cost_name_surname = name_surname
                max_cost_severetiy = severity_of_disease
                max_cost_weight = weight
                max_cost_produce_medication = production_type_of_medication
                max_cost_medication_amountIU = amount_of_medicate_of_4_week
                max_cost_medication_cost = cost_of_medication_of_4_week
        
        if deficient_factor==8 and (production_type_of_medication =="p" or production_type_of_medication=="P"):
            total_factor8_plazma+=amount_of_medicate_of_4_week
            total_factor8_plazma_2000+=bottle_2000
            total_factor8_plazma_1500+=bottle_1500
            total_factor8_plazma_1000+=bottle_1000
            total_factor8_plazma_500+=bottle_500
            total_factor8_plazma_250+=bottle_250
        elif deficient_factor==8 and (production_type_of_medication=="r" or production_type_of_medication=="R"):
            total_factor8_recombinant+=amount_of_medicate_of_4_week
            total_factor8_recombinant_2000+=bottle_2000
            total_factor8_recombinant_1500+=bottle_1500
            total_factor8_recombinant_1000+=bottle_1000
            total_factor8_recombinant_500+=bottle_500
            total_factor8_recombinant_250+=bottle_250
        elif deficient_factor==9 and (production_type_of_medication=="P" or production_type_of_medication=="p"):
            total_factor9_plazma+=amount_of_medicate_of_4_week
            total_factor9_plazma_2000+=bottle_2000
            total_factor9_plazma_1500+=bottle_1500
            total_factor9_plazma_1000+=bottle_1000
            total_factor9_plazma_500+=bottle_500
            total_factor9_plazma_250+=bottle_250
        elif deficient_factor==9 and (production_type_of_medication=="R" or production_type_of_medication=="r"):
            total_factor9_recombinant+=amount_of_medicate_of_4_week
            total_factor9_recombinant_2000+=bottle_2000
            total_factor9_recombinant_1500+=bottle_1500
            total_factor9_recombinant_1000+=bottle_1000
            total_factor9_recombinant_500+=bottle_500
            total_factor9_recombinant_250+=bottle_250

    cost_of_medication_for_one_year = cost_of_medication_for_four_week * 13

    response = input("Do you calculate for any other patient? (y/Y/n/N)") 
    while response != "y" and response != "Y" and response != "n" and response != "N":
        print("Incorrect info entry please try again!") 
        response = input("Do you calculate for any other patient? (y/Y/n/N)")

print(f"Hemophilia A patients are {hemophilia_A_patint_number} person, hemophilia B patients are {hemophilia_B_patint_number} person and total patient number is {total_patient_number}")
print(f"Severe patient number is {severe_patient_number} and {round((severe_patient_number/total_patient_number)*100,2)}, moderate patient number is {moderate_patient_number} and percentage {round((moderate_patient_number/total_patient_number)*100,2)} and mild patient number is {mild_patient_number} and percentage {round((mild_patient_number/total_patient_number)*100,2)}")
if hemophilia_A_patint_number != 0 and hemophilia_B_patint_number != 0 :
    print(f"percentage of hemophilia-A patients who has antibody greater than 5 is {round((greater_than_5_antibody_A_number/hemophilia_A_patint_number)*100,2)}, hemophilia-B patients' is {round((greater_than_5_antibody_B_number/hemophilia_B_patint_number)*100,2)}")
elif hemophilia_A_patint_number == 0 and hemophilia_B_patint_number != 0:
    print(f"percentage of hemophilia-B patients' who has antibody greater than 5 is {round((greater_than_5_antibody_B_number/hemophilia_B_patint_number)*100,2)}")
elif hemophilia_A_patint_number != 0 and hemophilia_B_patint_number == 0 :
    print(f"percentage of hemophilia-A patients who has antibody greater than 5 is {round((greater_than_5_antibody_A_number/hemophilia_A_patint_number)*100,2)}")

if prophylaxis_true_A_patients != 0 and prophylaxis_true_B_patients == 0:
    print(f"number of receive prophylaxis true A patient is {prophylaxis_true_A_patients} percentage of hemophilia-A patients who receive prophylaxis is {round((prophylaxis_true_A_patients/hemophilia_A_patint_number)*100,2)}")
elif prophylaxis_true_A_patients == 0 and prophylaxis_true_B_patients != 0:
    print(f"number of receive prophylaxis true B patient is {prophylaxis_true_B_patients} percentage of hemophilia-B patients who receive prophylaxis is {round((prophylaxis_true_B_patients/hemophilia_B_patint_number)*100,2)}")
elif prophylaxis_true_A_patients == 0 and prophylaxis_true_B_patients == 0:
    print("There are no patients receiving prophylaxis treatment!")
else:
    print(f"number of receive prophylaxis true A patient is {prophylaxis_true_A_patients} percentage of hemophilia-A patients who receive prophylaxis is {round((prophylaxis_true_A_patients/hemophilia_A_patint_number)*100,2)} number of receive prophylaxis true B patient is {prophylaxis_true_B_patients} and percentage of hemophilia-B patients who receive prophylaxis is {round((prophylaxis_true_B_patients/hemophilia_B_patint_number)*100,2)}")

if (prophylaxis_true_A_patients+prophylaxis_true_B_patients) != 0:
    print(f"The percentage of patients receiving prophylaxis among hemophilia patients whose disease severitiy is moderate is {round((need_prophylaxis_moderate_patients/(prophylaxis_true_A_patients+prophylaxis_true_B_patients))*100,2)}")

if prophylaxis_true_A_patients != 0 and prophylaxis_true_B_patients == 0:
    print(f"Percentage of patients using plasma-derivered Hemophilia A patients number is {round((need_prophylaxis_A_plasma/prophylaxis_true_A_patients)*100,2)} and recombinant patient percentage is {round((need_prophylaxis_A_recombinant/prophylaxis_true_A_patients)*100,2)}")
elif prophylaxis_true_A_patients == 0 and prophylaxis_true_B_patients != 0:
    print(f"Percentage of patients using plasma-derivered Hemophilia B patients number is {round((need_prophylaxis_B_plasma/prophylaxis_true_B_patients)*100,2)} and recombinant-derivered patient number is {round((need_prophylaxis_B_recombinant/prophylaxis_true_B_patients)*100,2)}")
elif prophylaxis_true_A_patients == 0 and prophylaxis_true_B_patients == 0:
    print("There is no patient who see prophylaxis treatment!")
else:
    print(f"Percentage of patients using plasma-derivered Hemophilia A patients number is {round((need_prophylaxis_A_plasma/prophylaxis_true_A_patients)*100,2)} and recombinant patient percentage is {round((need_prophylaxis_A_recombinant/prophylaxis_true_A_patients)*100,2)} Percentage of patients using plasma-derivered Hemophilia B patients number is {round((need_prophylaxis_B_plasma/prophylaxis_true_B_patients)*100,2)} and recombinant-derivered patient number is {round((need_prophylaxis_B_recombinant/prophylaxis_true_B_patients)*100,2)}")

print(f"Total plasma-derived factor8 meducation amounts for 4 week is {total_factor8_plazma} IU, {12*int(total_factor8_plazma_2000)} 2000's bottle, {12*int(total_factor8_plazma_1500)} 1500's bottle for 4 week, {12*int(total_factor8_plazma_1000)} 1000's bottle for 4 week, {12*int(total_factor8_plazma_500)} 500's bottle for 4 week, {12*int(total_factor8_plazma_250)} 250's bottle for 4 week")
print(f"Total recombiant factor8 meducation amounts for 4 week is {total_factor8_recombinant} IU, {12*int(total_factor8_recombinant_2000)} 2000's bottle, {12*int(total_factor8_recombinant_1500)} 1500's bottle for 4 week, {12*int(total_factor8_recombinant_1000)} 1000's bottle for 4 week, {12*int(total_factor8_recombinant_500)} 500's bottle for 4 week, {12*int(total_factor8_recombinant_250)} 250's bottle for 4 week")
print(f"Total plasma-derived factor9 meducation amounts for 4 week is {total_factor9_plazma} IU, {8*int(total_factor9_plazma_2000)} 2000's bottle, {8*int(total_factor9_plazma_1500)} 1500's bottle for 4 week, {8*int(total_factor9_plazma_1000)} 1000's bottle for 4 week, {8*int(total_factor9_plazma_500)} 500's bottle for 4 week, {8*int(total_factor9_plazma_250)} 250's bottle for 4 week")
print(f"Total recombiant factor9 meducation amounts for 4 week is {total_factor9_recombinant} IU, {8*int(total_factor9_recombinant_2000)} 2000's bottle, {8*int(total_factor9_recombinant_1500)} 1500's bottle for 4 week, {8*int(total_factor9_recombinant_1000)} 1000's bottle for 4 week, {8*int(total_factor9_recombinant_500)} 500's bottle for 4 week, {8*int(total_factor9_recombinant_250)} 250's bottle for 4 week")
print(f"4 weeks factor medication costs for prophylaxis is {round(cost_of_medication_for_four_week,2)}$ and 1 year factor medication costs for prophylaxis is {round(cost_of_medication_for_one_year,2)}$")

if need_prophylaxis_patients != 0:
    print(f"Average annual total medication amount per patient is {round(total_medication_amount_for_one_year/need_prophylaxis_patients,2)} IU and average annual cost per patient is {round(cost_of_medication_for_one_year/need_prophylaxis_patients,2)}$")
else:
    print("There is no patient who see prophylaxis treatment!")

print(f"TR identification number is {max_id_number_A}, name and surname is {max_name_surname_A}, disease severities is {max_severetiy_A}, weight is {max_weight_A} kg, production types of medications used (plasma-derived/recombinant) is {max_produce_medication_A}, 4-weeks total medication amounts (IU) is {max_medication_amountIU_A} IU and cost is ($) {round(max_medication_cost_A,2)} $ of patients with the highest 4-weeks medication amount for Hemophilia-A ")
print(f"TR identification number is {max_id_number_B}, name and surname is {max_name_surname_B}, disease severities is {max_severetiy_B}, weight is {max_weight_B} kg, production types of medications used (plasma-derived/recombinant) is {max_produce_medication_B}, 4-weeks total medication amounts (IU) is {max_medication_amountIU_B} IU and cost is ($) {round(max_medication_cost_B,2)} $ of patients with the highest 4-weeks medication amount for Hemophilia-B ")
print(f"TR identification number is {max_cost_id_number}, name and surname is {max_cost_name_surname}, disease severities is {max_cost_severetiy}, weight is {max_cost_weight} kg, production types of medications used (plasma-derived/recombinant) is {max_cost_produce_medication}, 4-weeks total medication amounts (IU) is {max_cost_medication_amountIU} IU and cost is ($) {round(max_cost_medication_cost,2)} $ of patients with the highest 4-weeks medication cost.")

