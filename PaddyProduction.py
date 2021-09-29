import hashlib


class NeuralCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = " ---> ".join(transaction_list) + " ---> " + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t01 = "Farmer sells 20kg Paddy to Procurement Agent"
t02 = "Procurement Agent sends 600taka to Farmer"
t03 = "Procurement Agent sells 10kg to Rice Processing Company"
t04 = "Rice Processing Company sends 450taka to Procurement Agent"
t05 = "Rice Processing Company sells 8kg rice to Distributions Agent or Institutional Buyer"
t06 = "Distributions Agent or Institutional Buyer sends 400taka to Rice Processing Company"
t07 = "Distributions Agent or Institutional Buyer sells 5kg rice to Retailer"
t08 = "Retailer sends 350taka to Distributions Agent or Institutional Buyer"
t09 = "Retailer sells 2kg rice to Customer"
t10 = "Customer sends 200taka to Retailer"

# Transit between FARMER to PROCUREMENT AGENTS
initial_block = NeuralCoinBlock("Initial String", [t01, t02])
print(initial_block.block_data)
print(initial_block.block_hash)
print()

# Transit between PROCUREMENT AGENTS to RICE PROCESSING COMPANIES
second_block = NeuralCoinBlock(initial_block.block_hash, [t03, t04])
print(second_block.block_data)
print(second_block.block_hash)
print()

# Transit between RICE PROCESSING COMPANIES to DISTRIBUTION AGENTS or INSTITUTIONAL BUYERS
third_block = NeuralCoinBlock(second_block.block_hash, [t05, t06])
print(third_block.block_data)
print(third_block.block_hash)
print()

# Transit between DISTRIBUTION AGENTS or INSTITUTIONAL BUYERS to RETAILERS
fourth_block = NeuralCoinBlock(third_block.block_hash, [t07, t08])
print(fourth_block.block_data)
print(fourth_block.block_hash)
print()

# Transit between RETAILERS to CUSTOMERS
fifth_block = NeuralCoinBlock(fourth_block.block_hash, [t09, t10])
print(fifth_block.block_data)
print(fifth_block.block_hash)
print()
