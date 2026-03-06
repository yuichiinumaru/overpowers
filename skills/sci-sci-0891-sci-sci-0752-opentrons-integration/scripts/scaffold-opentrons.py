#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Scaffold an Opentrons Protocol API script")
    parser.add_argument('--name', default="My Protocol", help="Name of the protocol")
    parser.add_argument('--author', default="Opentrons Author <author@example.com>", help="Author name and email")
    parser.add_argument('--description', default="Opentrons Protocol", help="Protocol description")
    parser.add_argument('--api-level', default="2.19", help="API Level")

    args = parser.parse_args()

    protocol = f"""from opentrons import protocol_api

metadata = {{
    'apiLevel': '{args.api_level}',
    'protocolName': '{args.name}',
    'description': '{args.description}',
    'author': '{args.author}'
}}

def run(protocol: protocol_api.ProtocolContext):
    # Load labware
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')

    # Load pipettes
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])

    # Commands
    # Example: transfer 100ul from well A1 to well A2
    p300.transfer(100, plate['A1'], plate['A2'])

"""
    print(protocol)

if __name__ == '__main__':
    main()
