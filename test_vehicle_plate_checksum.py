from vehicle_plate_checksum import CheckSum

def test_plate_checksum():
    test_cases = [
        # Valid plates
        ("SNB9538E", "Valid Plate"),
        ("GBF307K",  "Valid Plate"),
        ("SLR5791E", "Valid Plate"),
        ("SHC7009U", "Valid Plate"),
        ("SBA1234G", "Valid Plate"),
        ("SDN7484U", "Valid Plate"),
        
        # Invalid plates
        ("SNB9538F", "Invalid Plate"),
        ("GBF307L",  "Invalid Plate"),
        ("SLR5791F", "Invalid Plate"),
        ("SHC7009V", "Invalid Plate"),
        ("SBA1234A", "Invalid Plate"),
        ("SDN7484V", "Invalid Plate"),
    
        # Invalid inputs
        ("SBA1234",   "Invalid Input"),
        ("1234A",     "Invalid Input"),
        ("SBA12345A", "Invalid Input"),
        ("SBAA1234A", "Invalid Input"),
        ("S3AA",      "Invalid Input"),
        ("S1B2A3C",   "Invalid Input"),
    ]

    for plate, expected_result in test_cases:
        result = CheckSum(plate)
        assert result == expected_result, f"Input: {plate}, Expected: {expected_result}, Got: {result}"

if __name__ == "__main__":
    test_plate_checksum()
