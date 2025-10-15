CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
]

# simulate a "chai object"
chai_type = 'ML'

# print human-readable name
for code, label in CHAI_TYPE_CHOICES:
    if code == chai_type:
        print(label)   # outputs: MASALA

