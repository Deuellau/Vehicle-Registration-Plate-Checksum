# Singapore Vehicle Plate Checksum Calculator

This Python script, `vehicle_plate_checksum.py`, calculates the checksum for Singapore's vehicle registration plates. It helps determine if a given vehicle plate is valid or invalid based on Singapore's plate numbering system.

## How It Works

The script defines a function `CheckSum(plate) -> str` that takes a vehicle plate as input and returns a string indicating whether the plate is valid or invalid.

### Input Requirements

- The input plate must be a string with a length between 3 and 8 characters.
- The plate should consist of a prefix (up to 3 uppercase letters) and a numeric portion (up to 4 digits), followed by a single uppercase letter as a checksum.

### Algorithm

1. It validates the length of the plate. If it doesn't meet the length requirements, it returns "Invalid Input."

2. It separates the prefix (letters) and the numeric portion of the plate.

3. It calculates the checksum based on the provided plate using a specific [algorithm](https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Singapore#Checksum).

4. It compares the calculated checksum to the provided checksum.

5. If the calculated checksum matches the provided checksum, it returns "Valid Plate." Otherwise, it returns "Invalid Plate."

## Usage

You can use this script by calling the `CheckSum` function with a vehicle plate as the argument, like this:

```python
result = CheckSum("SNB9538E")
print(result)  # Output: "Valid Plate"

result = CheckSum("SNB9538F")
print(result)  # Output: "Invalid Plate"

result = CheckSum("SNB9538")
print(result)  # Output: "Invalid Input"
```

## Testing Accuracy
A separate test script, `test_plate_checksum.py`, is created to ensure the accuracy of the checksum calculation. It uses plate numbers found on [Vehicle registration plates of Singapore](https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Singapore) to verify whether the `CheckSum` function produces the expected results. Invalid test cases are created by modifying the checksum letter while keeping the rest of the plate valid.
