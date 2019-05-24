"""
Defines choices shared by some model fields.
"""

CHEMICAL_TYPES = (
    ('T', 'toxic'),
    ('F', 'flammable'),
)

SUBMISSION_TYPES = (
    ('F', 'First-time submission'),
    ('R', 'Resubmission'),
    ('C', 'Correction of existing RMP'),
)

HORIZONTAL_DATUM_CODES = (
    ('001', 'North American Datum of 1927'),
    ('002', 'North American Datum of 1983'),
    ('003', 'World Geodetic System of 1984'),
)