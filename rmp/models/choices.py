"""
Defines choices shared by some model fields.
"""

CHEMICAL_TYPE_CHOICES = (
    ('T', 'toxic'),
    ('F', 'flammable'),
)

SUBMISSION_TYPE = (
    ('F', 'First-time submission'),
    ('R', 'Resubmission'),
    ('C', 'Correction of existing RMP'),
)