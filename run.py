def main():
    """
    Runs main function
    """
    joey_hours = int(input("How many hours did Joey work? "))
    hannah_hours = int(input("How many hours did Hannah work? "))
    rachel_hours = int(input("How many hours did Rachel work? "))
    willian_hours = int(input("How many hours did Willian work? "))
    ciara_hours = int(input("How many hours did Ciara work? "))
    saoirse_hours = int(input("How many hours did Saoirse work? "))
    total_hours = (
        joey_hours + hannah_hours + rachel_hours +
        willian_hours + ciara_hours + saoirse_hours
    )
    print(f"The total amount of hours worked was {total_hours}")
    total_tips = int(input("What were the total tips today? "))
    tips_per_hour = total_tips / total_hours
    rounded_tips_per_hour = round(tips_per_hour, 2)
    print(f"The tips per hour is {rounded_tips_per_hour}")
    print("Calculationg everyones tips...")
    print(f"Joey's tips today were {joey_hours * rounded_tips_per_hour}")
    print(f"Hannah's tips today were {hannah_hours * rounded_tips_per_hour}")
    print(f"Rachel's tips today were {rachel_hours * rounded_tips_per_hour}")
    print(f"Willian's tips today were {willian_hours * rounded_tips_per_hour}")
    print(f"Ciara's tips today were {ciara_hours * rounded_tips_per_hour}")
    print(f"Saoirse's tips today were {saoirse_hours * rounded_tips_per_hour}")

main()