import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv", dtype={"id": str})


class Purchase:
    def __init__(self, product_id):
        self.id = product_id
        self.product_name = df.loc[df["id"] == self.id, "name"].squeeze()
        self.product_price = df.loc[df["id"] == self.id, "price"].squeeze()

    def available(self):
        # Check for the availability of the product
        availability = df.loc[df["id"] == self.id, "in stock"].squeeze()
        if availability > 0:
            return True
        else:
            return False


class Receipt:
    def __init__(self, buy):
        self.buy = buy

    def generate_receipt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.buy.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.buy.product_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.buy.product_price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
prompt = input("Choose an article to buy: ")
buy = Purchase(product_id=prompt)

if buy.available():
    receipt = Receipt(buy)
    receipt.generate_receipt()
else:
    print("No such product in stock")
