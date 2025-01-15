class Invoices:
    def __init__(self, invoce_id, customer_id, invoce_date, billing_add, billing_city,billing_state,billing_country,billing_postal_code,total):
        self.invoce_id=invoce_id
        self.customer_id=customer_id
        self.invoce_date=invoce_date
        self.billing_add=billing_add
        self.billing_city=billing_city
        self.billing_state=billing_state
        self.billing_country=billing_country
        self.billing_postal_code=billing_postal_code
        self.total=total

    def __repr__(self):
        return f"Invoices(ID:{self.invoce_id}, Customer id:{self.customer_id}, Invoce date={self.invoce_date},Billing add:{self.billing_add}, Billing city:{self.billing_city}, Billing State:{self.billing_state}, Billing Country:{self.billing_country}, Billing Postal Code:{self.billing_postal_code}, Total:{self.total})"
        