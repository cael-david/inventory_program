from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from addresses_module import GeneralAddresses
    from batch import GeneralBatch

class Product:
    def __init__(self, code, fraction, description, addresses=None, batches=None):
        self.code = code
        self.fraction = fraction
        self.description = description   
        self.addresses: list["GeneralAddresses"] = addresses if addresses is not None else []
        self.batches: list["GeneralBatch"] = batches if batches is not None else []

    def total(self):
        return sum(batch.quantity for batch in self.batches)

    def add_address(self, new_address: "GeneralAddresses"):
        if new_address not in self.addresses:
            self.addresses.append(new_address)
            new_address.add_product(self)

    def remove_address(self, old_address: "GeneralAddresses"):
        if old_address in self.addresses:
            self.addresses.remove(old_address)
            old_address.remove_product(self)
        else:
            print(f"Address {old_address} not found")

    def update_address(self, old_address: "GeneralAddresses", updated_address: "GeneralAddresses"):
        if old_address in self.addresses:
            index = self.addresses.index(old_address)
            self.addresses[index] = updated_address
            old_address.remove_product(self)
            updated_address.add_product(self)
        else:
            print(f"Address {old_address} not found")

    def add_batch(self, new_batch: "GeneralBatch"):
        if new_batch not in self.batches:
            self.batches.append(new_batch)
            new_batch.add_product(self)

    def remove_batch_by_bcode(self, old_bcode):
        batch_to_remove = next((batch for batch in self.batches if batch.bcode == old_bcode), None)
        if batch_to_remove:
            self.batches.remove(batch_to_remove)
            batch_to_remove.remove_product(self)
        else:
            print(f"Batch with bcode {old_bcode} not found")

    def update_batch_bcode(self, old_bcode, new_bcode):
        batch_to_update = next((batch for batch in self.batches if batch.bcode == old_bcode), None)
        if batch_to_update:
            batch_to_update.bcode = new_bcode
        else:
            print(f"Batch with bcode {old_bcode} not found")

    def remove_batch_by_quantity(self, old_quantity):
        batch_to_remove = next((batch for batch in self.batches if batch.quantity == old_quantity), None)
        if batch_to_remove:
            self.batches.remove(batch_to_remove)
            batch_to_remove.remove_product(self)
        else:
            print(f"Batch with quantity {old_quantity} not found")

    def update_batch_quantity(self, old_quantity, new_quantity):
        batch_to_update = next((batch for batch in self.batches if batch.quantity == old_quantity), None)
        if batch_to_update:
            batch_to_update.quantity = new_quantity
        else:
            print(f"Batch with quantity {old_quantity} not found")
            
