from driverFactory import DriverFactory

driver1 = DriverFactory.get_driver('chrome')
print(driver1)

try:
    driver2 = DriverFactory.get_driver('edge')
    print(driver2)
except ValueError as e:
    print('Lỗi:', e)
