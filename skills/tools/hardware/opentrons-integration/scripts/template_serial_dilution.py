from opentrons import protocol_api

# Metadata
metadata = {
    'protocolName': 'Serial Dilution Template',
    'author': 'Agent',
    'description': 'Basic serial dilution protocol for Opentrons.',
    'apiLevel': '2.14'
}

def run(protocol: protocol_api.ProtocolContext):
    # 1. Load labware
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', '1')
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', '2')
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '3')

    # 2. Load instrument
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tips])

    # 3. Define liquids (optional but good practice)
    diluent = reservoir.wells()[0]
    sample = reservoir.wells()[1]

    # 4. Transfer diluent to all wells in the first row except the first well
    row = plate.rows()[0]
    p300.transfer(100, diluent, row[1:])

    # 5. Transfer sample to the first well
    p300.transfer(200, sample, row[0])

    # 6. Perform serial dilution
    p300.transfer(
        100,
        row[:11],          # Source wells (0 to 10)
        row[1:],           # Destination wells (1 to 11)
        mix_after=(3, 50), # Mix 3 times with 50uL
        new_tip='always'   # Change tip for each transfer to prevent carryover
    )

    protocol.comment("Serial dilution complete!")
