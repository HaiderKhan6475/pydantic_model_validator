# Pydantic Model Validator — Patient Management System

A beginner-friendly Python project demonstrating **Pydantic v2 model validation** through a real-world patient management scenario.

## 📌 Project Overview

This project validates patient information using Pydantic's `BaseModel` and `@model_validator(mode="after")`.

The main business rule is:

> Patients older than 60 years must provide an emergency contact.

The project demonstrates how to enforce rules that depend on multiple fields in a model.

## 🚀 Features

- Define a patient data model using `BaseModel`.
- Validate patient fields using Python type annotations.
- Validate email addresses using `EmailStr`.
- Support optional emergency contact information.
- Enforce cross-field validation with `@model_validator`.
- Raise and handle `ValidationError` for invalid patient data.
- Test valid and invalid patient records.

## 🛠️ Technologies Used

- Python 3.11+
- Pydantic v2
- Email validation support

## 📂 Project Structure

```text
model-validator-project/
├── main.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd model-validator-project
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, create one with:

```text
pydantic[email]>=2.0,<3.0
```

Alternatively, install the dependency directly:

```bash
pip install "pydantic[email]"
```

## ▶️ Run the Project

Run the Python file:

```bash
python main.py
```

The program executes three test cases.

## 🧪 Test Cases

| Test case | Age | Emergency contact | Expected result |
|---|---:|---|---|
| Patient A | 65 | Provided | Valid |
| Patient B | 65 | Missing | Validation error |
| Patient C | 40 | Missing | Valid |

### Business Rule

- If `age > 60`, an emergency contact is required.
- If `age <= 60`, the emergency contact is optional.

## 💡 Key Concept: `model_validator`

Example:

```python
@model_validator(mode="after")
def validate_emergency_contact(self):
    if self.age > 60 and not self.emergency_contact:
        raise ValueError(
            "Emergency contact is required for patients over 60 years old."
        )
    return self
```

### Why use `model_validator`?

A field validator focuses on an individual field. A model validator is suitable when a validation rule depends on multiple fields, such as the relationship between a patient's age and emergency contact.

In Pydantic v2, an `after` model validator receives the validated model instance through `self` and should return that instance when validation succeeds.

## 📚 Learning Outcomes

After completing this project, you should understand:

1. How to define Pydantic models.
2. How optional fields and default values work.
3. How to validate relationships between fields.
4. How to raise and handle validation errors.
5. How to write test cases for business rules.

## 🔮 Future Improvements

- Add field constraints using `Field()` and `Annotated`.
- Add nested models for address and contact details.
- Add computed fields for BMI calculation.
- Integrate the model into a FastAPI application.
- Add automated tests using `pytest`.

## 👨‍💻 Author

Created as part of a hands-on journey into Pydantic and FastAPI backend development.
