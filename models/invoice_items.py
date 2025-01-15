class Invoice_items:
    def __init__(self,invoice_item_id: int, invoice_id: int,Track_id: int,Unit_Price: int, Quantity: int):
        self.invoice_item_id=invoice_item_id
        self.invoice_id=invoice_id
        self.Track_id=Track_id
        self.Unit_Price=Unit_Price
        self.Quantity=Quantity

    def __repr__(self):
        return Invoice_items(f"invoice_id={self.invoice_item_id},invoice_id={self.invoice_id}, Track_id={ self.Track_id},Unit_Price: { self.Unit_Price},Quantity={self.Quantity}")