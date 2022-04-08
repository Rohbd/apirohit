
from dataclasses import Field
from decimal import Decimal
from email.policy import default
from typing import Optional
from unittest.util import _MAX_LENGTH
from sqlmodel import SQLModel, create_engine
from enum import Enum
from datetime import datetime
from master.models import InvoiceStatuschoices



class VendorBuyerRelationship(SQLModel,table=True):
    buyer : int | None = Field(default = None, foreign_key = "Buyer.id")

    vendor : int | None = Field(default = None, foreign_key = "Vendor.id")

    vendor_code : str | None = Field(default = None, max_length=35)

    vendor_type : int | None = Field(default = None, foreign_key = "buyer.BuyerVendorTypeMaster.id")

    vendor_bank_account : int | None = Field(default = None, foreign_key = "vendor.VendorBankAccount.id")

    annual_interest_rate : Decimal = Field(default = 0.0 )

    hold_back_amount_percentage : Decimal = Field(default = 0.0)

    redit_score : Decimal = Field(default = 0.0)

    credit_limit : Decimal = Field(default = 0.0)
    


class DiscountingRules(SQLModel, table=True): 

    vendor_buyer_relationship : int | None = Field(default = None, foreign_key = "transactions.VendorBuyerRelationship.id")



class Invoice(SQLModel, table=True):

    unique_id : str = Field(default = None, _MAX_LENGTH = 100)

    number : int = Field(None, _MAX_LENGTH = 100)

    reference_number : str = Field(None, MAX_LENGTH = 100)

    applied_rule : int = Field(None, foreign_key = "transactions.DiscountingRules.id")

    vendor_gstin_number : str = Field(None, MAX_LENGTH = 15)
    validators=[
            RegexValidator(
                regex=RegexValidatorStrings.GSTIN,
                message="Please enter a valid 15 character long GSTIN number.",
            )
        ]

    invoice_value : float = Field(default = 0.0)

    tds_amount : float = Field(default = 0.0)

    net_amount : float = Field(default = 0.0)

    service_tax_amount : float = Field(default = 0.0)

    igst_amount = float = Field(default = 0.0)

    cgst_amount : float = Field(default = 0.0)

    sgst_amount : float = Field(default = 0.0)

    vat_amount : float = Field(default = 0.0)

    hold_back_amount_base : float = Field(default = 0.0)

    hold_back_amount_gst : float = Field(default = 0.0)

    hold_back_amount_total : float = Field(default = 0.0)

    amount_available_for_discounting : float = Field(default = 0.0)

    discount_rate_per_annum : float = Field(default = 0.0)

    discount_calculation_days : float = Field(default = 0.0)

    early_payment_amount_base : float = Field(default = 0.0)

    early_payment_amount_gst : float = Field(default = 0.0)

    early_payment_amount_total : float = Field(default = 0.0)

    parties_involved : int = Field(None, foreign_key = "transactions.VendorBuyerRelationship.id")

    INVOICE_STATUS = (
        (InvoiceStatuschoices.NEW, "New"),
        (InvoiceStatuschoices.NOT_APPROVED, "Not Approved"),
        (InvoiceStatuschoices.DISCOUNT_CALCULATED, "Discount Calculated"),
        (InvoiceStatuschoices.REJECTED_BY_VENDOR, "Rejected By Vendor"),
        (InvoiceStatuschoices.PENDING_FOR_BUYER_APPROVAL, "Pending For Buyer Approval"),
        (InvoiceStatuschoices.REJECTED_BY_BUYER, "Rejected By Buyer"),
        (InvoiceStatuschoices.PENDING_FOR_KS_APPROVAL, "Pending For KS Approval"),
        (InvoiceStatuschoices.REJECTED_BY_KS, "Rejected By KS"),
        (InvoiceStatuschoices.PENDING_PAYMENT, "Pending Payment"),
        (InvoiceStatuschoices.PARTIAL_PAYMENT_DONE, "Partial Payment Done"),
        (InvoiceStatuschoices.PAYMENT_DONE, "Full Payment Done"),
    )
    status : Field (choices=INVOICE_STATUS, default=InvoiceStatuschoices.NEW,)

    vendor_invoice_date : datetime.datetime | None = Field(None)

    buyer_invoice_date : datetime.datetime | None = Field(None)

    vendor_due_date : datetime.datetime | None = Field(None)

    buyer_approval_date : datetime.datetime | None = Field(None)

    buyer_due_date : datetime.datetime | None = Field(None)

    discount_calculation_date : datetime.datetime | None = Field(None)

    vendor_early_payment_request_date : datetime.datetime | None = Field(None)

    buyer_early_payment_approval_date : datetime.datetime | None = Field(None)

    backoffice_early_payment_approval_date : datetime.datetime | None = Field(None)

    final_early_payment_approval_date : datetime.datetime | None = Field(None)

    early_payment_disbursal_date : datetime.datetime | None = Field(None)

    invoice_settlement_date : datetime.datetime | None = Field(None)

    rejection_remarks : str | None = Field(None)


class Payment(SQLModel, table = True):
    vendor_details : int = Field(None, foreign_key = "Vendor.id")
    amount : float = Field(default = 0.0 )


class Collection(SQLModel, table = True):
    buyer_details : int = Field(None, foreign_key = "Buyer.id")
    amount : float = Field(default=0.0)






sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

