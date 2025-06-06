
               
def calculate_salary(base_salary, bonus_rate=.1):
    """
    Calculate the total salary based on the base salary and bonus rate.
               
    Args:
        base_salary (float): The base salary.
        bonus_rate (float): The bonus rate. Default is .1
               
    Returns:
        float: The total salary
    """
    return base_salary * (1 + bonus_rate)   

def calculate_bonus(total_salary, base_salary):
    """
    Calculate the bonus rate based on the base salary and the total salary.
               
    Args:
        total_salary (float): The total salary.
        base_salary (float): The base salary.
               
    Returns:
        float: The bonus rate.
    """
    return (total_salary - base_salary) / base_salary                     

