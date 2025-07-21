def check_limits(val, low_limit, high_limit,name):
    if val < low_limit or val > high_limit:
        return False
        print(f'{name} is out of range')
    return True

def battery_is_ok(temperature, soc, charge_rate):
    return (check_limits(temperature,0,45,'Temperature') and
            check_limits(soc,0,45,'State of Charge') and
            check_limits(charge_rate,0,0.8,'Charge rate')
           )
if __name__ == '__main__':
    assert(battery_is_ok(5, 90, 0.7) is False)
    assert(battery_is_ok(50, 85, 0) is False)
