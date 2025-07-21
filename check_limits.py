def battery_is_ok(temperature, soc, charge_rate):
    limits = {
        'Temperature': (temperature, 0, 45),
        'State of Charge': (soc, 20, 80),
        'Charge rate': (charge_rate, 0, 0.8)
    }
    for name, (value, low, high) in limits.items():
        if value < low or value > high:
            print(f'{name} is out of range!')
            return False
    return True

if __name__ == '__main__':
    assert(battery_is_ok(5, 90, 0.7) is False)
    assert(battery_is_ok(50, 85, 0) is False)
