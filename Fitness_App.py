"""This code is a Python program that helps users calculate their body mass index (BMI),
      BMI rating, basal metabolic rate (BMR), total daily energy expenditure (TDEE), daily calorie
         needs for weight loss, and provides a summary report of their body statistics."""


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print("Your BMI is:", round(bmi, 2))
    return bmi

def rating(bmi):
    if bmi < 18.5:
        rating = "Underweight"
    elif 18.5 <= bmi < 25:
        rating = "Normal weight"
    elif 25 <= bmi < 30:
        rating = "Overweight"
    else:
        rating = "Obese"
    return rating

def calculate_bmr(weight, height, age):
    bmr = 88.362 + (13.397 * weight) + (479.9 * height) - (5.677 * age)
    print("Your BMR is:", round(bmr))
    return bmr

def tdee(bmr, activity_level):
    tdee_result = bmr * activity_level
    print(round(tdee_result, 2))
    print("\033[1;3mTotal daily energy expenditure (TDEE) estimates how many calories your body burns daily ,"
          "If you eat approximately the same number of calories you burn each day; you'll maintain your weight."
          "Essentially, you can think of TDEE as your maintenance calories. Therefore, to lose weight, you will need to eat less than your TDEE\033[m")

def calculate_daily_calorie_needs(weight_kg):
    target_weight = float(input("Enter your target weight in kilograms: "))
    time_frame = int(input("Enter the number of weeks you want to achieve your target weight: "))

    # Calculate total weight loss
    weight_loss = weight_kg - target_weight

    # Calculate total calorie deficit needed for weight loss
    calorie_deficit = weight_loss * 7700 / time_frame

    # Calculate daily calorie needs for weight loss
    daily_calorie_needs = 2000 - calorie_deficit / 7

    print("Your daily calorie needs for weight loss are:", round(daily_calorie_needs, 2))

def app():
    weight_kg = float(input("Enter your weight in kilograms, for calculation BMI: "))
    height_m = float(input("Enter your height in meters, for calculation BMI: "))
    user_age = int(input("Enter you age, for calculation BMR: "))

    bmi = calculate_bmi(weight_kg, height_m)

    bmi_rating = rating(bmi)
    print("Your BMI rating is:", bmi_rating)

    bmr = calculate_bmr(weight_kg, height_m, user_age)

    print("\033[1;3mActivity level in the Harris-Benedict equation refers to an individual's physical activity level,"
          "\nrepresented by a number from 1.2 (sedentary) to 1.9 (very active), with 1.55 being moderate activity.\033[m")

    activity_level = float(input("Enter your activity level, for calculation TDEE: "))

    tdee(bmr, activity_level)

    calculate_daily_calorie_needs(weight_kg)


def reuse():
    while True:
        app()
        answer = input("Do you want to use the app again? (yes or no): ")
        if answer.lower() == "no":
            print("Thank you for using our app!")
            break


reuse()
