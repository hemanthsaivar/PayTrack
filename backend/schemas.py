from pydantic import BaseModel, Field

class LineItem(BaseModel):
    description: str = Field(min_length=1)
    unit_price_paise: int = Field(gt=0, strict=True)
    quantity: int = Field(gt=0, strict=True)

class InvoiceCreate(BaseModel):
    customer: str = Field(min_length=1)
    items: list[LineItem] = Field(min_length=1)

class NoteUpdate(BaseModel):
    note: str = Field(max_length=500)

class PaymentCreate(BaseModel):
    invoice_id: int
    amount_paise: int = Field(gt=0, strict=True)
    request_key: str = Field(min_length=1)
    simulate_failure: bool = False

class RefundCreate(BaseModel):
    amount_paise: int = Field(gt=0, strict=True)
