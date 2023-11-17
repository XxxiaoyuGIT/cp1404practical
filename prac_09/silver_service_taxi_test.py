from silver_service_taxi import silverservicetaxi
def test_silver_service_taxi():
    """Test function for the SilverServiceTaxi class."""
    silver_taxi = silverservicetaxi("silver_service", 100, 2)
    silver_taxi.drive(18)
    fare = silver_taxi.get_fare()
    print(f"Silver Service Taxi fare for 18 km trip: ${fare:.2f}")
    print(silver_taxi)
if __name__ == '__main__':
    test_silver_service_taxi()