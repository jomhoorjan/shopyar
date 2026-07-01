class ReceiptReader:

    def read(self, image_path):
        print(f"Reading receipt: {image_path}")

        return {
            "date": None,
            "items": [],
            "total": None
        }