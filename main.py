
from fastapi import Body, FastAPI, HTTPException, Query, Request
from sqlalchemy import ARRAY, String, Column, create_engine
from sqlmodel import Session, and_, col, Field, select
from typing import List, Set
import transaction

from transaction.models import (
    create_db_and_tables,
    engine,
    VendorBuyerRelationship,
    DiscountingRules,
    Invoice,
    Payment,
    Collection,
)

app = FastAPI()



@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/transaction/")
def make_transaction(
    vendorBuyerRelationship : VendorBuyerRelationship,
    discountingRules : DiscountingRules,
    invoice : Invoice,
    payment : Payment,
    collection : Collection, 
 
):



 with Session(engine) as session:

# VendorBuyerRelationship primary key as a foreign key in discountingrules

    session.add(vendorBuyerRelationship)
    session.commit()
    discountingRules.vendor_buyer_relationship = transaction.vendorBuyerRelationship.id 

# discountingRules primary key as a foreign key in  invoice

    session.add(discountingRules)
    session.commit()
    invoice. applied_rule = transaction.discountingRules.id

# vendorbuyerrelationship primary key  as a foreign key in invoice

    session.add()
    session.commit()
    invoice.parties_involved = transaction.vendorBuyerRelationship.id


    session.refresh(vendorBuyerRelationship)
    session.refresh(discountingRules)
    session.refresh(invoice)
    session.refresh(payment)
    session.refresh(collection)

    return (
       vendorBuyerRelationship,
       discountingRules,
       invoice,
       payment,
       collection,

    )

# invoice api

@app.post("/invoice/")
def create_invoice(invoice:Invoice):
    with Session(engine) as session:
         session.add(invoice)
         session.commit()
         session.refresh(invoice)
         return invoice

# vendorbuyerrelatioship api

@app.post("/vendorBuyerRelationship/")
def ven_buy_relationship(vendorBuyerRelationship:VendorBuyerRelationship):
    with Session(engine) as session:
         session.add(vendorBuyerRelationship)
         session.commit()
         session.refresh(vendorBuyerRelationship)
         return vendorBuyerRelationship


# discountingrules api

@app.post("/discountingRules/")
def discount_rules(discountingRules:DiscountingRules):
    with Session(engine) as session:
         session.add(discountingRules)
         session.commit()
         session.refresh(discountingRules)
         return discountingRules


# payment api

@app.post("/payment/")
def make_payment(payment:Payment):
    with Session(engine) as session:
         session.add(payment)
         session.commit()
         session.refresh(payment)
         return payment 

# collection api

@app.post("/collection/")
def collection(collection:Collection):
    with Session(engine) as session:
         session.add(collection)
         session.commit()
         session.refresh(collection)
         return collection


