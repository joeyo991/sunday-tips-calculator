def calculate_total_hours_worked():
    joey_hours = int(input("How many hours did Joey work? "))
    hannah_hours = int(input("How many hours did Hannah work? "))
    rachel_hours = int(input("How many hours did Rachel work? "))
    ciara_hours = int(input("How many hours did Ciara work? "))
    willy_hours = int(input("How many hours did Willy work? "))
    saoirse_hours = int(input("How many hours did Saoirse work? "))
    total_hours_worked = (joey_hours + hannah_hours + rachel_hours + ciara_hours + willy_hours + saoirse_hours)
    
    print(f"The total hours worked: {total_hours_worked}")
    return total_hours_worked


def calculate_tips_per_hour():
    total_tips = int(input("What were the total tips? "))
    tips_per_hour = total_tips / total_hours_worked

    print(tips_per_hour)

def main():
    calculate_total_hours_worked()
    calculate_tips_per_hour()


main()