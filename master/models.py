from sre_parse import State
from typing import Optional
from unittest.util import _MAX_LENGTH
from sqlmodel import SQLModel, create_engine, Field




class Bank(SQLModel,table=True):
 name : str = Field(primary_key= True) 

 ifsc_code_prefix : Optional[str]


class City(SQLModel,table=True):
 name : str | None = Field(None, max_length=50)

 state : str = Field(foreign_key = "Buyer.id")


class state(SQLModel,table=True):
 name : str | None = Field(None, max_length=50)

 gst_code : str | None = Field(default = None)

    
class AddressTypechoices(SQLModel):
    PERMANENT : int = 1
    TEMPORARY : int = 2
    RESIDENTIAL : int = 3
    REGISTERED : int = 4
    COMMUNICATION : int = 5
    OFFICE : int = 6
    HEAD_OFFICE : int = 7
    BRANCH_OFFICE : int = 8


class DocumentTypechoices(SQLModel):
    PAN  : int = 1
    GST_CERTIFICATE : int = 2
    CANCELLED_CHEQUE : int = 3
    TAN : int = 4
    COI : int = 5
    DIN : int = 6
    AADHAAR : int = 7
    VOTER_ID : int = 8
    EDUCATION_CERTIFICATE : int = 9
    PASSPORT : int = 10
    AOA : int = 11
    MOA : int = 12
    ELECTRICITY_BILL : int = 13
    BOARD_RESOLUTION = 14
    S_AND_E : int = 15
    TRUST_DEED : int = 16
    PARTNERSHIP_DEED : int = 17
    TRUST_REGISTRATION : int = 18

class DocumentVerificationStatuschoices(SQLModel):
    DRAFT : int = 1
    PENDING_AUTOMATIC : int = 2
    PENDING_MANUAL : int = 3
    VERIFIED : int = 4
    DISCARDED : int = 5

class DocumentVerificationMethodchoices(SQLModel):
    MANUAL : int = 1
    AUTOMATED : int = 2

class OrganizationalEntityTypeschoices(SQLModel):
    PRIVATE_LIMITED : int = 1
    PUBLIC_LIMITED : int = 2
    PARTNERSHIP : int = 3
    LIMITED_LIABILITY_PARTNERSHIP : int = 4
    ONE_PERSON_COMPANY : int = 5
    SOLE_PROPRIETORSHIP : int = 6
    SECTION_8_COMPANY : int = 7
    TRUST : int = 8
    FOREIGN_ENTITY: int =  9
    ASSOCIATION_OF_PERSONS : int = 10
    BODY_OF_INDIVIDUALS : int = 11

class OrganizationKMPTypeschoices(SQLModel):
    DIRECTOR : int = 1
    PARTNER : int = 2

class EmployeeRoleschoices(SQLModel):
    ADMIN : int = 1
    USER : int = 2

class DocumentRejectionRemarkschoices(SQLModel):
    INVALID : str = "Invalid Document"
    BLURRED : str = "Blurred Image"
    MISMATCH : str =  "Information Mismatch"
    EXPIRED : str = "Document Expired"


class ProfileVerificationStatuschoices(SQLModel):
    PENDING : int = 1
    PARTIALLY_VERIFIED : int = 2
    FULLY_VERIFIED : int = 3

class InvoiceStatuschoices(SQLModel):
    NEW : int = 1
    NOT_APPROVED : int = 2
    DISCOUNT_CALCULATED : int = 3
    REJECTED_BY_VENDOR : int = 4
    PENDING_FOR_BUYER_APPROVAL : int = 5
    REJECTED_BY_BUYER : int = 6
    PENDING_FOR_KS_APPROVAL : int = 7
    REJECTED_BY_KS : int = 8
    PENDING_PAYMENT : int = 9
    PARTIAL_PAYMENT_DONE : int = 10
    PAYMENT_DONE : int = 11

class TrasactionTypeschoices(SQLModel):
    DEBIT_NOTE : int = 1
    ADVANCE : int = 2
    DISBURSEMENT : int = 3
    CREDIT_NOTE : int = 4
    RECIEVABLE : int = 5

