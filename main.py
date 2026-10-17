
from pydantic import BaseModel, EmailStr, model_validator, ValidationError
from typing import Optional


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight_kg: float
    allergies: list[str]
    phone: dict[str, str]
    emergency_contact: Optional[str] = None

    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age > 60 and not self.emergency_contact:
            raise ValueError(
                "Emergency contact is required for patients over 60 years old."
            )
        return self


def update_patient_data(patient: Patient):
    print(f"Name: {patient.name}")
    print(f"Email: {patient.email}")
    print(f"Age: {patient.age}")
    print(f"Weight: {patient.weight_kg}")
    print(f"Allergies: {patient.allergies}")
    print(f"Phone: {patient.phone}")
    print(f"Emergency Contact: {patient.emergency_contact}")


def test_patient(patient_info):
    try:
        patient = Patient(**patient_info)
        print("\nPatient created successfully!")
        update_patient_data(patient)

    except ValidationError as error:
        print("\nPatient validation failed:")
        print(error)


# Test A: Age 65 with emergency contact — should pass
patient_65_with_contact = {
    "name": "John Doe",
    "email": "john.doe@hdfc.com",
    "age": 65,
    "weight_kg": 70.5,
    "allergies": ["pollen", "dust"],
    "phone": {"home": "123-456-7890"},
    "emergency_contact": "987-654-3210",
}

# Test B: Age 65 without emergency contact — should fail
patient_65_without_contact = {
    "name": "Jane Doe",
    "email": "jane.doe@hdfc.com",
    "age": 65,
    "weight_kg": 62.0,
    "allergies": ["dust"],
    "phone": {"home": "111-222-3333"},
}

# Test C: Age 40 without emergency contact — should pass
patient_40_without_contact = {
    "name": "Ali Khan",
    "email": "ali.khan@hdfc.com",
    "age": 40,
    "weight_kg": 68.0,
    "allergies": [],
    "phone": {"home": "444-555-6666"},
}


print("========== TEST A ==========")
test_patient(patient_65_with_contact)

print("\n========== TEST B ==========")
test_patient(patient_65_without_contact)

print("\n========== TEST C ==========")
test_patient(patient_40_without_contact)
