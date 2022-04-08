from pydantic import BaseModel, ValidationError, validator

class RegexValidatorStrings(SQLModel):
    AADHAAR = r"^[1-9]{1}\d{11}$"
    CIN = r"^[LU]{1}\d{5}[A-Za-z]{2}\d{4}[A-Za-z]{3}\d{6}$"  # L12312LL1234LLL123123
    DRIVING_LICENSE = r"^[A-Za-z]{2}\d{13}$"
    EMAIL = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    GSTIN = r"^\d{2}[A-Za-z]{3}[CPHFATBLJGcphfatbljg]{1}[A-Za-z]{1}\d{4}[A-Za-z]{1}\d{1}[Zz]{1}[0-9A-Za-z]{1}$"
    IFSC = r"^[A-Za-z]{4}0[A-Za-z0-9]{6}$"
    MOBILE_NUMBER = r"^[6789]\d{9}$"
    PAN = r"^[A-Za-z]{3}[CPHFATBLJGcphfatbljg]{1}[A-Za-z]{1}\d{4}[A-Za-z]{1}$"
    PASSPORT_NUMBER = r"^[A-Za-z]{1}\d{7}$"
    TAN = r"^[A-Za-z]{4}\d{5}[A-Za-z]{1}$"





